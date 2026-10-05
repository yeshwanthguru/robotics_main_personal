"""Builds paper/Model_Paper_Manuscript.docx (review copy, IEEE numbered citations) from paper/main.tex.
Run from github/model (needs pandoc >= 3)."""
import os, re, shutil, subprocess, tempfile
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'paper')
s = open(os.path.join(P, 'main.tex')).read()
for f in ('abstract', 'part1_intro_methods', 'part2_results'):
    s = s.replace('\\input{%s}' % f, open(os.path.join(P, f + '.tex')).read())
for i, lab in enumerate(re.findall(r'\\label\{(eq:[^}]*)\}', s), 1):
    s = s.replace('\\ref{%s}' % lab, str(i))
s = s.replace('\\begin{figure*}', '\\begin{figure}').replace('\\end{figure*}', '\\end{figure}')
s = re.sub(r'\\IEEEPARstart\{(\w)\}\{(\w*)\}', r'\1\2', s)
s = re.sub(r'\\fillin\{([^{}]*)\}', r'[FILL: \1]', s)
s = re.sub(r'\\begin\{IEEEbiographynophoto\}.*?\\end\{IEEEbiographynophoto\}', '', s, flags=re.S)
s = re.sub(r'\\begin\{IEEEkeywords\}(.*?)\\end\{IEEEkeywords\}', r'\\paragraph{Index Terms} \1', s, flags=re.S)
d = tempfile.mkdtemp(); open(os.path.join(d, 'body.tex'), 'w').write(s)
shutil.copytree(os.path.join(P, 'figures'), os.path.join(d, 'figures'))
csl = os.path.join(os.path.dirname(P), 'tools', 'ieee.csl')
subprocess.run(['pandoc', 'body.tex', '-f', 'latex', '-t', 'docx', '--number-sections', '--bibliography', os.path.join(P, 'refs.bib'),
                '--citeproc', '--csl', csl, '-o', os.path.join(P, 'Model_Paper_Manuscript.docx')], cwd=d, check=True,
               stderr=subprocess.DEVNULL)
shutil.rmtree(d); print('wrote paper/Model_Paper_Manuscript.docx')
