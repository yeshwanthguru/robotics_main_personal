-- Wrap pandoc citations and the bibliography in Mendeley (legacy CSL) Word fields.
-- Run after --citeproc so each Cite already holds its formatted text.
-- Field codes: ADDIN CSL_CITATION {json} and ADDIN Mendeley Bibliography CSL_BIBLIOGRAPHY.

local items = {}

local function xml_escape(s)
  return (s:gsub('&', '&amp;'):gsub('<', '&lt;'):gsub('>', '&gt;'))
end

local function field_begin(instr)
  return pandoc.RawInline('openxml',
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r>' ..
    '<w:r><w:instrText xml:space="preserve">' .. xml_escape(instr) .. '</w:instrText></w:r>' ..
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
end

local field_end = pandoc.RawInline('openxml', '<w:r><w:fldChar w:fldCharType="end"/></w:r>')

local cap_prefix = ''
function Meta(meta)
  if meta['caption-prefix'] then cap_prefix = pandoc.utils.stringify(meta['caption-prefix']) end
  local path = meta['csl-items-file'] and pandoc.utils.stringify(meta['csl-items-file'])
  local fh = io.open(path, 'r')
  for _, it in ipairs(pandoc.json.decode(fh:read('a'), false)) do items[it.id] = it end
  fh:close()
end

local counter = 0
-- Same structure as Mendeley Desktop's legacy CSL fields (which Mendeley Cite converts):
-- item ids numbered ITEM-1.. within each citation, itemData.id equal to that id,
-- and only the citationItems / mendeley / properties / schema keys.
local function copy(t) local r = {} for k, v in pairs(t) do r[k] = v end return r end
function Cite(el)
  local cits = {}
  for n, c in ipairs(el.citations) do
    counter = counter + 1
    local iid = 'ITEM-' .. n
    local data = copy(items[c.id])
    data.id = iid
    table.insert(cits, { id = iid, itemData = data })
  end
  local text = pandoc.utils.stringify(el.content)
  local payload = {
    citationItems = cits,
    mendeley = { formattedCitation = text, plainTextFormattedCitation = text, previouslyFormattedCitation = text },
    properties = { noteIndex = 0 },
    schema = 'https://github.com/citation-style-language/schema/raw/master/csl-citation.json',
  }
  local out = { field_begin('ADDIN CSL_CITATION ' .. pandoc.json.encode(payload)) }
  for _, i in ipairs(el.content) do table.insert(out, i) end
  table.insert(out, field_end)
  return out
end

function Div(el)
  if el.identifier ~= 'refs' then return nil end
  local n = 0
  el:walk({ Para = function(p) n = n + 1 end })
  if n == 0 then return nil end
  local i = 0
  return el:walk({ Para = function(p)
    i = i + 1
    if i == 1 then p.content:insert(1, field_begin('ADDIN Mendeley Bibliography CSL_BIBLIOGRAPHY')) end
    if i == n then p.content:insert(field_end) end
    return p
  end })
end

-- Number table and figure captions the way the LaTeX version does.
local ntab, nfig = 0, 0
local function prefix(caption, label)
  if caption.long[1] then
    caption.long[1].content:insert(1, pandoc.Strong(pandoc.Str(label)))
    caption.long[1].content:insert(2, pandoc.Space())
  end
  return caption
end
function Table(el) ntab = ntab + 1; el.caption = prefix(el.caption, 'Table ' .. cap_prefix .. ntab .. '.'); return el end
function Figure(el) nfig = nfig + 1; el.caption = prefix(el.caption, 'Fig. ' .. cap_prefix .. nfig .. '.'); return el end

return { { Meta = Meta }, { Cite = Cite, Div = Div }, { Table = Table, Figure = Figure } }
