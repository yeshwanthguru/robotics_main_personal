"""Simplify the Survey 2 LaTeX (Springer sn-jnl manuscript or article-class supplement) so pandoc
can convert it to Word. Title, authors, abstract and keywords go to a YAML metadata block.
Usage: prep_tex_for_word.py <in.tex> <out.tex> <out.yaml> [S]"""
import json
import os
import re
import sys

src, out_tex, out_yaml = sys.argv[1:4]
prefix = sys.argv[4] if len(sys.argv) > 4 else ''   # 'S' for the supplement
s = open(src, encoding='utf-8').read()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inline_math_unicode import convert as inline_math

AUTHORS = ['Yeshwanth Guru, Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India '
           '(g_yeshwanth@ch.students.amrita.edu; ORCID 0009-0007-6353-4033; corresponding author)',
           'Dev Kunwar Singh Chauhan, Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India '
           '(c_devsingh@ch.amrita.edu; ORCID 0000-0002-1466-4567)']


def latex_text(t):
    return (t.replace('``', '\u201c').replace("''", '\u201d').replace('~', ' ').replace('\\%', '%')
             .replace('--', '\u2013').replace('\\_', '_'))


if not prefix:
    title = re.search(r'\\title(?:\[[^\]]*\])?\{(.*?)\}\n', s).group(1)
    abstract = re.search(r'\\abstract\{(.*?)\}\n', s, re.S).group(1).strip()
    keywords = re.search(r'\\keywords\{(.*?)\}\n', s).group(1)
    body = s[s.index('\\maketitle') + len('\\maketitle'):s.index('\\bibliography{refs}')]
    if '\\begin{appendices}' in body:   # number appendix headings A, A.1, B, ... as in the PDF
        head, app = body.split('\\begin{appendices}', 1)
        app = app.replace('\\end{appendices}', '')
        parts = re.split(r'(\\section\{[^}]*\}|\\subsection\{[^}]*\})', app)
        letter, sub, outp = '@', 0, []
        ntab, applabels = {}, {}
        for part in parts:
            m = re.match(r'\\(sub)?section\{([^}]*)\}', part)
            if m and not m.group(1):
                letter, sub = chr(ord(letter) + 1), 0
                part = '\\section*{Appendix %s. %s}' % (letter, m.group(2))
            elif m:
                sub += 1
                part = '\\subsection*{%s.%d %s}' % (letter, sub, m.group(2))
            else:   # appendix tables are numbered C1, C2, ... as in the PDF; the Lua filter reads the marker
                def mark(t, letter=letter):
                    ntab[letter] = ntab.get(letter, 0) + 1
                    num = '%s%d' % (letter, ntab[letter])
                    lab = re.search(r'\\label\{(tab:[^}]*)\}', t.group(0))
                    if lab:
                        applabels[lab.group(1)] = num
                    return t.group(0).replace('\\caption{', '\\caption{APPNUM%sAPPNUM ' % num, 1)
                part = re.sub(r'\\begin\{table\}.*?\\end\{table\}', mark, part, flags=re.S)
            outp.append(part)
        body = head + ''.join(outp)
        for lab, num in applabels.items():
            body = body.replace('\\ref{%s}' % lab, num)
    body = re.sub(r'\\bmhead\{(.*?)\}', r'\\subsection*{\1}', body)
    body = re.sub(r'\\surveypart\{(.*?)\}', r'\\section*{\1}', body)  # Part A-E headings
else:
    title = ('Online Resource 1. Supplementary material for \u201cQuantum-Inspired Cognition and Decision-Making for '
             'Autonomous Agents, from Robotics to AI/ML Systems: A Systematic Review\u201d')
    abstract, keywords = '', ''
    body = s[s.index('\\end{center}') + len('\\end{center}'):s.index('\\bibliographystyle')]
    body = re.sub(r'\\begin\{landscape\}|\\end\{landscape\}|\\footnotesize|\\normalsize', '', body)
    # longtable -> tabular, which pandoc reads reliably; drop the repeated-header blocks
    def lt(m):
        spec, inner = m.group(1), m.group(2)
        cap = re.search(r'\\caption\{(.*?)\}\\label\{(.*?)\}\\\\', inner, re.S)
        inner = inner[cap.end():] if cap else inner
        inner = re.sub(r'\\endfirsthead.*?\\endhead', '', inner, flags=re.S)
        inner = re.sub(r'\\endfirsthead|\\endhead|\\endfoot|\\endlastfoot', '', inner)
        inner = inner.replace('\\bottomrule', '', 1) if inner.count('\\bottomrule') > 0 else inner
        return ('\\begin{table}\n\\caption{%s}\\label{%s}\n\\begin{tabular}{%s}\n%s\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'
                % (cap.group(1), cap.group(2), spec, inner)) if cap else m.group(0)
    body = re.sub(r'\\begin\{longtable\}\{(.*?)\}\n(.*?)\\end\{longtable\}', lt, body, flags=re.S)
    body = body.replace('P{', 'p{')
    for kind in ('tab', 'fig'):
        for i, lab in enumerate(re.findall(r'\\label\{(%s:[^}]*)\}' % kind, body), 1):
            body = body.replace('\\ref{%s}' % lab, '%s%d' % (prefix, i))

body = re.sub(r'\\ket\{([^{}]*)\}', r'|\1\\rangle', body.replace('\\ket{\\psi}', '|\\psi\\rangle'))
body = re.sub(r'\\bra\{([^{}]*)\}', r'\\langle \1|', body)
# pandoc cannot convert \left( ... \{ ... \} \right) in the Lindblad equation; simplify it
body = body.replace(r'\left(L_k \rho L_k^{\dagger} - \tfrac{1}{2}\{L_k^{\dagger}L_k, \rho\}\right)',
                    r'(L_k \rho L_k^{\dagger} - \frac{1}{2}\lbrace L_k^{\dagger}L_k, \rho\rbrace)')
body = inline_math(body)
body = re.sub(r'>\{\\raggedright\\arraybackslash\}p\{([0-9.]+)\\dimexpr[^}]*\}', r'p{\1\\linewidth}', body)
body = re.sub(r'\\fillin\{([^{}]*)\}', r'[FILL: \1]', body)
body = body.replace('\\botrule', '\\bottomrule')

pre = '\\documentclass{article}\n\\usepackage{natbib}\n\\usepackage{graphicx}\n\\begin{document}\n'
open(out_tex, 'w', encoding='utf-8').write(pre + body + '\n\\end{document}\n')

meta = {'title': latex_text(title), 'author': AUTHORS, 'caption-prefix': prefix,
        'reference-section-title': 'References', 'link-citations': False}
if abstract:
    meta['abstract'] = latex_text(abstract)
if keywords:
    meta['keywords'] = keywords
open(out_yaml, 'w', encoding='utf-8').write('---\n' + json.dumps(meta, ensure_ascii=False, indent=1) + '\n---\n')
