"""Writes Survey3_source_drafts/Survey3_Paper_Writeups.docx: one structured write-up per reviewed work
(summary, extraction fields, verification note), grouped by topic. Run from github/s (needs pandoc)."""
import csv, os, subprocess, tempfile
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
ext = list(csv.DictReader(open(S + 'Survey3_data_package/extraction_table.csv', encoding='utf-8-sig')))
summ = {r['Key']: r for r in csv.DictReader(open(S + 'Survey3_data_package/study_summaries.csv', encoding='utf-8-sig'))}
topics = []
for r in ext:
    if r['Topic'] not in topics: topics.append(r['Topic'])
md = ['---', 'title: "Survey 3 — structured write-ups of the 180 reviewed works"',
      'subtitle: "Meta-Learning Orchestration of Learning Modalities on Resource-Constrained Robots: A Systematic Review"',
      'author: "Yeshwanth Guru and Dev Kunwar Singh Chauhan"', '---', '',
      'One write-up per work, grouped by topic: summary, extraction fields, edge and signal coding, and the details still '
      'to be verified. Basis gives the source of the write-up (full text, abstract or standard reference); figures not '
      'given in an abstract are not quoted. The same content is in the data package (Survey3_data_package).', '']
F = ['Task', 'Method', 'Setup and data', 'Key result', 'Limitation', 'Edge footprint (as published)', 'Edge class',
     'Confidence signal class', 'Role in the framework', 'DOI or identifier']
for t in topics:
    rows = [r for r in ext if r['Topic'] == t]
    md += ['# %s (%d)' % (t, len(rows)), '']
    for r in rows:
        sm = summ[r['Key']]
        md += ['## %s' % r['Study'], '',
               '*Key* `%s` · *role* %s · *source* %s · *basis* %s · *level* %s' % (r['Key'], r['Role'].lower(), r['Source stream'].lower(), r['Basis'].lower(), r['Evidence level']), '',
               sm['Summary'], '', '| Field | Content |', '|---|---|']
        md += ['| %s | %s |' % (k, r[k].replace('|', '/')) for k in F if r.get(k)]
        if sm['Verification_note']: md += ['', '**To verify:** ' + sm['Verification_note']]
        md.append('')
d = tempfile.mkdtemp(); open(d + '/w.md', 'w', encoding='utf-8').write('\n'.join(md))
subprocess.run(['pandoc', d + '/w.md', '-o', S + 'Survey3_source_drafts/Survey3_Paper_Writeups.docx'], check=True)
print('wrote Survey3_Paper_Writeups.docx')
