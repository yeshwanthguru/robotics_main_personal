"""Write Survey2_Word_for_Mendeley/Survey2_reference_lookup.docx: every reference in refs.bib
(key, authors, year, title, DOI or arXiv id), to find each one in Mendeley. Run from github/m."""
import os
import re
import subprocess
import tempfile

bib = open('Survey2_AIR_LaTeX_Overleaf/refs.bib', encoding='utf-8').read()
rows = []
for e in re.split(r'\n(?=@)', bib):
    m = re.match(r'@\w+\{([^,]+),', e.strip())
    if not m:
        continue
    def f(name):
        mm = re.search(name + r'\s*=\s*\{(.+?)\},?\s*\n', e, re.S)
        return re.sub(r'\s+', ' ', re.sub(r'[{}\\]|\\[a-z]+', '', mm.group(1))) if mm else ''
    ident = f('doi') and 'doi:' + f('doi') or (f('eprint') and 'arXiv:' + f('eprint')) or ''
    authors = f('author').replace(' and ', '; ')
    rows.append((m.group(1), authors, f('year'), f('title'), ident))
rows.sort(key=lambda r: r[0].lower())
md = ['# Survey 2 reference lookup', '', f'All {len(rows)} references of the manuscript, sorted by citation key.', '',
      '| Key | Authors | Year | Title | DOI / arXiv |', '|---|---|---|---|---|']
md += ['| ' + ' | '.join(x.replace('|', '/') for x in r) + ' |' for r in rows]
with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as t:
    t.write('\n'.join(md) + '\n')
os.makedirs('Survey2_Word_for_Mendeley', exist_ok=True)
subprocess.run(['pandoc', t.name, '-o', 'Survey2_Word_for_Mendeley/Survey2_reference_lookup.docx'], check=True)
os.unlink(t.name)
print('wrote Survey2_Word_for_Mendeley/Survey2_reference_lookup.docx (%d references)' % len(rows))
