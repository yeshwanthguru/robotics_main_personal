-- Variant of mendeley_fields.lua for re-citing by hand in Mendeley Cite:
-- each citation becomes yellow-highlighted plain text (no fields), and the
-- reference list is replaced by a highlighted placeholder for Mendeley's bibliography.

local function esc(s)
  return (s:gsub('&', '&amp;'):gsub('<', '&lt;'):gsub('>', '&gt;'))
end

local function yellow(text)
  return pandoc.RawInline('openxml',
    '<w:r><w:rPr><w:highlight w:val="yellow"/></w:rPr><w:t xml:space="preserve">' ..
    esc(text) .. '</w:t></w:r>')
end

function Cite(el)
  local text = pandoc.utils.stringify(el.content)
  -- Narrative citation: keep the author names as normal text, highlight the year part.
  if #el.citations == 1 and el.citations[1].mode == 'AuthorInText' then
    local a, rest = text:match('^(.-)%s(%(.*%))$')
    if a then return { pandoc.Str(a), pandoc.Space(), yellow(rest) } end
  end
  return { yellow(text) }
end

function Div(el)
  if el.identifier ~= 'refs' then return nil end
  return pandoc.Para({ yellow('[Insert the Mendeley bibliography here: Mendeley Cite > Insert Bibliography]') })
end

-- Number table and figure captions the way the LaTeX version does.
local cap_prefix = ''
function Meta(meta)
  if meta['caption-prefix'] then cap_prefix = pandoc.utils.stringify(meta['caption-prefix']) end
end
local ntab, nfig = 0, 0
local function prefix(caption, label)
  if caption.long[1] then
    local first = caption.long[1].content[1]
    if first and first.t == 'Str' and first.text:match('^APPNUM') then   -- appendix table, e.g. C1
      label = 'Table ' .. first.text:match('^APPNUM(.-)APPNUM') .. '.'
      caption.long[1].content:remove(1)
      if caption.long[1].content[1] and caption.long[1].content[1].t == 'Space' then caption.long[1].content:remove(1) end
    end
    caption.long[1].content:insert(1, pandoc.Strong(pandoc.Str(label)))
    caption.long[1].content:insert(2, pandoc.Space())
  end
  return caption
end
function Table(el)
  local first = el.caption.long[1] and el.caption.long[1].content[1]
  if not (first and first.t == 'Str' and first.text:match('^APPNUM')) then ntab = ntab + 1 end
  el.caption = prefix(el.caption, 'Table ' .. cap_prefix .. ntab .. '.'); return el
end
function Figure(el) nfig = nfig + 1; el.caption = prefix(el.caption, 'Fig. ' .. cap_prefix .. nfig .. '.'); return el end

return { { Meta = Meta }, { Cite = Cite, Div = Div }, { Table = Table, Figure = Figure } }
