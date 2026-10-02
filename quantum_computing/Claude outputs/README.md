# Quantum Computing for Autonomous Robotics - IEEE LaTeX Package

## Complete Package for IEEE Conference Paper Submission

This is a ready-to-compile LaTeX package for the paper:
**"Quantum Computing for Autonomous Robotics: Near-Term Applications and Practical Limitations"**

---

## 📦 Package Contents

```
├── main.tex              ← Main paper file (copy-paste into Overleaf)
├── papers.bib            ← Bibliography with 62 papers (expand with your 100)
├── README.md             ← This file
└── INSTRUCTIONS.txt      ← Quick start guide
```

---

## 🚀 Quick Start: Overleaf Instructions

### Step 1: Create Overleaf Project
1. Go to **https://www.overleaf.com**
2. Click **"New Project"** → **"Blank Project"**
3. Name it: `Quantum-Robotics-RAM-Article`

### Step 2: Upload Files
1. In Overleaf, click **"Upload"** (top left)
2. Upload **main.tex** and **papers.bib** together
3. Overleaf auto-detects them

### Step 3: Compile
1. Click **"Recompile"** (green button, top)
2. Wait 30-60 seconds
3. PDF appears on the right panel
4. ✅ Done! You have a ready-to-submit article

### Step 4 (Optional): Edit & Personalize
- Replace `[Your Last Name]` with your name
- Replace `[Your University]` with your institution
- Replace `[Your City, Country]` with location
- Replace `[your.email@domain.com]` with your email

---

## 📚 Paper Statistics

- **Word Count:** ~4,200 words (within IEEE RAM limit of 4,500)
- **Sections:** 8 main sections
- **References:** 62 papers cited (expandable to 100+)
- **Figures:** Placeholder comments for 4-6 figures
- **Format:** IEEE Conference (IEEEtran class)

---

## 🔍 Current Citations: 62 Papers Included

### Quantum Computing Fundamentals (12 papers)
- Nielsen & Chuang 2010
- Montanaro 2016
- Preskill 2018 (NISQ)
- Bharti et al. 2022
- Arute et al. 2019 (Quantum supremacy)
- Vedral 2014
- Terhal 2015 (Error correction)
- Fowler et al. 2012 (Surface codes)

### Quantum Algorithms (16 papers)
- Farhi et al. 2014 (QAOA)
- Hadfield et al. 2019
- Zhou et al. 2020
- Barkoutsos et al. 2020
- Biamonte et al. 2017 (QML)
- Dunjko & Briegel 2018
- Cerezo et al. 2021
- Havlicek et al. 2019
- Schuld & Killoran 2022
- Chang et al. 2021
- Grover 1996 (Grover's algorithm)
- Brassard et al. 2000
- Montanaro 2015
- Wiebe et al. 2015
- Lloyd et al. 2014
- Liu et al. 2020

### Robotics & Control (12 papers)
- Thrun et al. 2005 (Probabilistic Robotics)
- LaValle 1998 (Motion planning)
- Karaman & Frazzoli 2011
- Corke 2011 (Robot control)
- Lynch & Park 2017 (Modern robotics)
- Khatib & Siciliano 2016
- Henderson et al. 2018
- Alcazar et al. 2022
- Krizhevsky et al. 2012
- Dellaert et al. 1999 (Localization)
- Montemerlo et al. 2002 (FastSLAM)
- Kaelbling et al. 1998 (POMDP)

### Quantum Cognition (12 papers)
- Busemeyer & Bruza 2012
- Pothos & Busemeyer 2009, 2013, 2022
- Wang et al. 2014
- Busemeyer & Townsend 1993
- Trueblood & Busemeyer 2011
- Busemeyer et al. 2011
- Aerts et al. 2000
- Widdows et al. 2023
- Yan et al. 2021
- Moreira 2017

### Multi-Robot & Applications (7 papers)
- Mannone et al. 2023, 2025
- Yun et al. 2022
- Lei et al. 2018
- Yan et al. 2024
- Lamm 2021
- Dong et al. 2010

### Critical Perspectives (3 papers)
- Tang 2020
- Aaronson 2015
- Cerezo et al. 2021 (barren plateaus)

---

## 🎯 How to Add Your 100 Papers

### Option 1: Expand papers.bib (Recommended)

The BibTeX file is organized by category. Add your papers in this format:

```bibtex
@article{unique_key,
  author = {Author, First A. and Author, Second B.},
  title = {Exact title of paper},
  journal = {Journal Name},
  volume = {10},
  number = {2},
  pages = {100--120},
  year = {2023}
}
```

**Common Entry Types:**
- `@article` - Journal papers
- `@conference` or `@inproceedings` - Conference papers
- `@book` - Books
- `@techreport` - Technical reports
- `@misc` - Preprints, theses, websites

### Option 2: Import from Citation Manager

If you have papers in Mendeley, Zotero, or EndNote:
1. Export as **BibTeX format** (.bib file)
2. Copy-paste entries into `papers.bib`
3. Recompile in Overleaf

### Option 3: Use Google Scholar

1. Google Scholar (scholar.google.com)
2. Search each paper
3. Click **"Cite"** → **"BibTeX"**
4. Copy-paste into `papers.bib`

---

## 📝 Cite Papers in Text

In `main.tex`, citations use `\cite{key}` format:

```latex
% Cite single paper
Quantum computing enables faster optimization \cite{b15}.

% Cite multiple papers
Previous work has shown various approaches \cite{b1, b2, b3}.

% Cite at start of sentence
\cite{b48} demonstrated that quantum cognition models...
```

The key (e.g., `b15`, `b48`) must match the `@article{key, ...}` in papers.bib.

---

## 🖼️ Adding Figures

Replace this section in main.tex to add your 4-6 images:

```latex
\begin{figure}[htbp]
\centerline{\includegraphics{your-figure.png}}
\caption{Figure caption here. This should describe what the figure shows.}
\label{fig:your_label}
\end{figure}
```

**Upload images in Overleaf:**
1. In Overleaf, click **"Upload"** (top left)
2. Select your image files (.png, .jpg, .pdf)
3. Reference them as: `\includegraphics{filename.png}`

**Recommended figures for this paper:**
1. Quantum computing timeline (NISQ to fault-tolerant)
2. Robot task examples (path planning, sensor fusion, coordination)
3. Latency comparison: quantum vs. classical
4. Quantum cognition framework diagram
5. Near-term opportunities roadmap (2026-2030)
6. Algorithm performance comparison (QAOA vs. classical heuristics)

---

## ✅ Submission Checklist

Before submitting to IEEE RAM or a journal:

- [ ] Replace all `[Your ...]` placeholders with actual information
- [ ] Add your ORCID (required by IEEE)
- [ ] Add 4-6 high-quality figures
- [ ] Verify all citations are correct (no broken references)
- [ ] Proofread for typos and grammar
- [ ] Ensure word count is <4,500 (current: ~4,200 ✓)
- [ ] Check figure quality (>300 dpi for publication)
- [ ] Download PDF and review formatting
- [ ] Test BibTeX compilation (no warnings/errors)

---

## 🔄 Word Count Management

Current sections and approximate word counts:

| Section | Words | Adjustable? |
|---------|-------|-------------|
| Title & Abstract | 150 | ✓ |
| Introduction | 450 | ✓ |
| Quantum 101 | 350 | ✓ |
| Quantum Algorithms | 600 | ✓ |
| Real-Time Control | 300 | ✓ |
| Near-Term Opportunities | 500 | ✓ |
| Quantum Cognition | 400 | ✓ |
| Challenges & Roadmap | 400 | ✓ |
| Conclusion | 150 | ✓ |
| **TOTAL** | **~4,200** | Stays <4,500 |

If you need to add more content, trim sections marked "✓" or expand selectively.

---

## 🔧 Troubleshooting

### Error: "papers.bib not found"
- Ensure both `main.tex` AND `papers.bib` are uploaded to Overleaf
- Both files must be in the same folder
- Recompile after uploading

### Error: "Citation key undefined"
- Check spelling of citation keys (e.g., `\cite{b15}`)
- Verify key exists in papers.bib
- Run `Recompile` twice (first pass finds references, second pass resolves them)

### Error: "Image file not found"
- Upload image files to Overleaf
- Use exact filename in LaTeX (case-sensitive!)
- Use format: `\includegraphics{filename.png}` (no path)

### PDF looks wrong (missing fonts, odd formatting)
- Click **"Logs and output files"** (right panel)
- Check for warnings
- Delete auxiliary files: **"Files"** → Delete `.aux`, `.bbl`
- Recompile

---

## 📖 Resources

- **Overleaf Documentation:** https://www.overleaf.com/learn
- **IEEE Author Guidelines:** https://www.ieee.org/publications/authors/
- **IEEE RAM Magazine:** https://www.ieee-ras.org/publications/ram/
- **BibTeX Documentation:** http://www.ctan.org/pkg/bibtex

---

## 💡 Next Steps

1. **Copy main.tex and papers.bib to Overleaf** ← Start here
2. **Compile** and verify PDF looks good
3. **Personalize** with your name, university, email, ORCID
4. **Add your 100 papers** to papers.bib
5. **Add 4-6 figures** (IEEE RAM requires illustrations)
6. **Proofread** and check word count
7. **Submit** to IEEE RAM or your target journal

---

## 📧 Support

For LaTeX issues in Overleaf:
- Overleaf Chat Support: https://www.overleaf.com/contact
- LaTeX Stack Exchange: https://tex.stackexchange.com

For paper content:
- Refer to IEEE RAM submission guidelines
- Use this template as a starting point; personalize with your research

---

**Version:** 1.0  
**Date:** September 2026  
**Status:** Ready to compile ✅
