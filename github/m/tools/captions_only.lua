-- Plain review version: citations stay as formatted text (no fields, no highlight);
-- only number table and figure captions the way the LaTeX version does.
local cap_prefix = ''
function Meta(meta)
  if meta['caption-prefix'] then cap_prefix = pandoc.utils.stringify(meta['caption-prefix']) end
end
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
return { { Meta = Meta }, { Table = Table, Figure = Figure } }
