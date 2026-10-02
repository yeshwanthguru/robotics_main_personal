"""Simplify the acmart manuscript so pandoc can convert it to Word.

Strips ACM-only front-matter commands, moves title/authors/abstract into a
YAML metadata block, and normalises the table column specs.
"""
import re, sys, json

src, out_tex, out_yaml = sys.argv[1:4]
s = open(src, encoding='utf-8').read()

title = re.search(r'\\title\[[^\]]*\]\{(.*?)\}\n', s).group(1)
authors = []
for m in re.finditer(r'\\author\{(.*?)\}\s*\n\\email\{(.*?)\}\s*\n\\affiliation\{%?\s*\n?\s*\\institution\{(.*?)\}\s*\n?\s*\\city\{(.*?)\}\s*\n?\s*\\country\{(.*?)\}\}', s):
    name, email, inst, city, country = m.groups()
    authors.append(f'{name}, {inst}, {city}, {country} ({email})')
abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', s, re.S).group(1).strip()
keywords = re.search(r'\\keywords\{(.*?)\}\n', s).group(1)

body = s[s.index('\\maketitle') + len('\\maketitle'):s.index('\\bibliographystyle')]
body = body.replace('\\begin{acks}', '\\section*{Acknowledgments}').replace('\\end{acks}', '')
body = re.sub(r'\\Description\{.*?\}\n', '', body)
# >{\raggedright\arraybackslash}p{0.160\dimexpr\linewidth-16\tabcolsep\relax} -> p{0.160\linewidth}
body = re.sub(r'>\{\\raggedright\\arraybackslash\}p\{([0-9.]+)\\dimexpr[^}]*\}', r'p{\1\\linewidth}', body)
body = re.sub(r'\\fillin\{([^{}]*)\}', r'[\1]', body)

pre = '\\documentclass{article}\n\\usepackage{natbib}\n\\usepackage{graphicx}\n\\begin{document}\n'
open(out_tex, 'w', encoding='utf-8').write(pre + body + '\n\\end{document}\n')

def latex_text(t):
    return t.replace('``', '\u201c').replace("''", '\u201d').replace('~', ' ').replace('\\%', '%')
meta = {
    'title': latex_text(title),
    'author': authors,
    'abstract': latex_text(abstract),
    'keywords': keywords,
    'reference-section-title': 'References',
    'link-citations': False,
}
open(out_yaml, 'w', encoding='utf-8').write('---\n' + json.dumps(meta, ensure_ascii=False, indent=1) + '\n---\n')
