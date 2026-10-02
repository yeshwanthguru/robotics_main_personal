"""Simplify the acmart manuscript so pandoc can convert it to Word.

Strips ACM-only front-matter commands, moves title/authors/abstract into a
YAML metadata block, and normalises the table column specs.
"""
import re, sys, json

src, out_tex, out_yaml = sys.argv[1:4]
prefix = sys.argv[4] if len(sys.argv) > 4 else ''   # 'S' for the supplement
s = open(src, encoding='utf-8').read()

m = re.search(r'\\title(?:\[[^\]]*\])?\{(.*?)\}\n', s)
title = m.group(1)
authors = []
for m in re.finditer(r'\\author\{(.*?)\}\s*\n\\email\{(.*?)\}\s*\n(?:\\orcid\{(.*?)\}\s*\n)?\\affiliation\{%?\s*\n?\s*(?:\\department\{(.*?)\}\s*\n?\s*)?\\institution\{(.*?)\}\s*\n?\s*\\city\{(.*?)\}\s*\n?\s*\\country\{(.*?)\}\}', s):
    name, email, orcid, dept, inst, city, country = m.groups()
    authors.append(f'{name}, ' + (f'{dept}, ' if dept else '') + f'{inst}, {city}, {country} ({email}' + (f'; ORCID {orcid}' if orcid else '') + ')')
if not authors:
    for m in re.finditer(r'\\author\{(.*?)\}\s*\n\\affiliation\{(?:\\department\{(.*?)\})?\\institution\{(.*?)\}\\city\{(.*?)\}\\country\{(.*?)\}\}', s):
        authors.append(', '.join(g for g in m.groups() if g))
m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', s, re.S)
abstract = m.group(1).strip() if m else ''
m = re.search(r'\\keywords\{(.*?)\}\n', s)
keywords = m.group(1) if m else ''

body = s[s.index('\\maketitle') + len('\\maketitle'):s.index('\\bibliographystyle')]
body = body.replace('\\begin{acks}', '\\section*{Acknowledgments}').replace('\\end{acks}', '')
body = re.sub(r'\\Description\{.*?\}\n', '', body)
# >{\raggedright\arraybackslash}p{0.160\dimexpr\linewidth-16\tabcolsep\relax} -> p{0.160\linewidth}
body = re.sub(r'>\{\\raggedright\\arraybackslash\}p\{([0-9.]+)\\dimexpr[^}]*\}', r'p{\1\\linewidth}', body)
body = re.sub(r'\\fillin\{([^{}]*)\}', r'[\1]', body)
if prefix:
    # supplement: resolve its own table/figure references as S1, S2, ... in order of appearance
    for kind in ('tab', 'fig'):
        labels = re.findall(r'\\label\{(%s:[^}]*)\}' % kind, body)
        for i, lab in enumerate(labels, 1):
            body = body.replace('\\ref{%s}' % lab, '%s%d' % (prefix, i))
    body = re.sub(r'\\begin\{landscape\}|\\end\{landscape\}', '', body)

pre = '\\documentclass{article}\n\\usepackage{natbib}\n\\usepackage{graphicx}\n\\begin{document}\n'
open(out_tex, 'w', encoding='utf-8').write(pre + body + '\n\\end{document}\n')

def latex_text(t):
    return t.replace('``', '\u201c').replace("''", '\u201d').replace('~', ' ').replace('\\%', '%')
meta = {
    'title': latex_text(title),
    'author': authors,
    'caption-prefix': prefix,
    'reference-section-title': 'References',
    'link-citations': False,
}
if abstract:
    meta['abstract'] = latex_text(abstract)
if keywords:
    meta['keywords'] = keywords
open(out_yaml, 'w', encoding='utf-8').write('---\n' + json.dumps(meta, ensure_ascii=False, indent=1) + '\n---\n')
