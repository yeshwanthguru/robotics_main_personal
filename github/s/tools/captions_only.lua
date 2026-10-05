-- Plain review version: citations stay as formatted text (no fields, no highlight);
-- only number table and figure captions the way the LaTeX version does.
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
return { { Meta = Meta }, { Table = Table, Figure = Figure } }
