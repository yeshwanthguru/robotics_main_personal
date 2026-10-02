# IEEE RAM Magazine Format - LaTeX Package

## Magazine vs. Conference Format

You now have **two versions** of your paper:

### 1. **main_complete.tex** (Conference Format)
- Two-column layout
- Compact, dense formatting
- Better for conference proceedings
- Page count: ~4-5 pages

### 2. **main_magazine.tex** (Magazine Format) ✅ RECOMMENDED FOR IEEE RAM
- **Single-column layout** 
- Magazine-style presentation
- More readable, professional appearance
- Better for IEEE RAM submissions
- Page count: ~8-10 pages (more space)
- Figures and sidebars flow naturally

---

## Key Differences in Magazine Format

| Aspect | Conference | Magazine |
|--------|-----------|----------|
| Layout | 2 columns | 1 column (wider text) |
| Text width | Narrow | Wide and readable |
| Visual appeal | Dense, academic | Clean, magazine-style |
| Page count | 4-5 pages | 8-10 pages |
| Ideal for | IEEE conferences | IEEE RAM, journals |
| Figure placement | Constrained | Flexible |

---

## 🚀 Quick Start: Magazine Format for IEEE RAM

### Step 1: Upload to Overleaf
1. Go to **https://www.overleaf.com**
2. Click **"New Project"** → **"Blank Project"**
3. Name it: `Quantum-Robotics-RAM-Magazine`

### Step 2: Upload Files
1. Click **"Upload"** (top left)
2. Upload **main_magazine.tex** and **papers.bib** together
3. Overleaf auto-detects them

### Step 3: Compile & Preview
1. Click **"Recompile"** (green button)
2. Wait 30-60 seconds
3. PDF appears on right panel
4. **Compare the layout** with conference version

### Step 4: Personalize
- Replace `[Your Last Name]` with your name
- Replace `[Your University]` with institution
- Replace `[Your City, Country]` with location
- Replace `[your.email@domain.com]` with email
- Add ORCID (required for IEEE)

---

## 📄 Paper Statistics (Magazine Format)

- **Word Count:** ~4,200 words (fits well in magazine)
- **Page Length:** 8-10 pages with figures
- **Sections:** 9 main sections + Acknowledgments
- **References:** 62 papers (expandable to 100+)
- **Figures:** Placeholder comments for 4-6 figures
- **Format:** IEEE Journal (IEEEtran journal class)

---

## ✅ IEEE RAM Submission Checklist

Before submitting to IEEE RAM via PaperCept:

- [ ] Use **main_magazine.tex** (not main_complete.tex)
- [ ] Replace all `[Your ...]` placeholders
- [ ] Add your ORCID (required)
- [ ] Add 4-6 high-resolution figures
  - Figure 1: Quantum bit diagram
  - Figure 2: Your robotic system photo (required)
  - Figure 3: Development phases timeline
  - Figure 4: QAOA vs. classical performance graph
  - Figure 5: Quantum cognition decision model
  - Figure 6: Real-time latency requirements
- [ ] Verify all citations are correct (no broken [b#] references)
- [ ] Proofread for typos and grammar
- [ ] Ensure word count stays <4,500 (current: ~4,200 ✓)
- [ ] Check figure quality (≥300 dpi for publication)
- [ ] Download PDF and review formatting
- [ ] Test BibTeX compilation (no warnings/errors)
- [ ] Submission format: PDF (max 2 MB) via PaperCept system

---

## 🔄 Adding Your 100 Papers

Both versions use the same **papers.bib** file. To expand from 62 to 100 papers:

### Option 1: Google Scholar (Easiest)
1. Go to scholar.google.com
2. Search for each paper
3. Click **"Cite"** → **"BibTeX"**
4. Copy-paste into papers.bib

### Option 2: Citation Manager
1. Export from Mendeley/Zotero as .bib
2. Copy entries into papers.bib
3. Recompile in Overleaf

### Format Template
```bibtex
@article{b63,
  author = {Author, First A. and Author, Second B.},
  title = {Exact paper title},
  journal = {Journal Name},
  volume = {10},
  number = {2},
  pages = {100--120},
  year = {2023}
}
```

**Important:** Update citation keys (b63, b64, ..., b100) and update \cite{} commands in text.

---

## 📊 Recommended Figure Details

Since magazine format has more space, figures can be larger and more impactful:

1. **Figure 1: Quantum Bit Concept**
   - Show superposition visually
   - Include measurement collapse
   - 1-column width (fits nicely in single column)

2. **Figure 2: Your Robot System**
   - High-quality photograph
   - Clear labeling of key components
   - Professional appearance required by IEEE

3. **Figure 3: Development Timeline**
   - Show historical progression (1980s → present)
   - Include NISQ era
   - Highlight quantum-robotics convergence

4. **Figure 4: Algorithm Performance**
   - Bar or line graph
   - Compare QAOA vs. classical heuristics
   - Include error bars/confidence intervals

5. **Figure 5: Decision Models**
   - Bayesian model vs. quantum cognition
   - Show interference effects
   - Visual comparison is clearer in magazine format

6. **Figure 6: Latency Requirements**
   - Timeline of robot control frequencies
   - Show incompatibility with quantum latency
   - Make the point visually obvious

---

## 🖼️ Uploading Figures in Overleaf

1. Click **"Upload"** in Overleaf
2. Select image files (.png, .jpg, .pdf)
3. In LaTeX, reference as:

```latex
\begin{figure}[htbp]
\centerline{\includegraphics[width=0.8\columnwidth]{your-figure.png}}
\caption{Figure caption describing what is shown.}
\label{fig:your_label}
\end{figure}
```

**For magazine format:** Use `width=0.9\columnwidth` to make figures wider and more readable.

---

## 🔧 Troubleshooting

### "Citation key undefined [b63]"
- Add the new entry to papers.bib
- Ensure key matches exactly in \cite{}
- Recompile twice

### "Image file not found"
- Verify image is uploaded to Overleaf
- Use exact filename (case-sensitive)
- No file paths, just filename.png

### "PDF looks too wide" or "text too loose"
- This is normal for magazine format
- Single-column layout has wider margins
- IEEE RAM expects this appearance

### "How many pages will it be?"
- Expected: 8-10 pages with 4-6 figures
- Word count stays ~4,200
- Pages adjust based on figure sizes and placement

---

## 📎 File Descriptions

| File | Purpose |
|------|---------|
| main_magazine.tex | Main paper (IEEE RAM magazine format) |
| papers.bib | Bibliography with 62 papers |
| README_MAGAZINE.md | This file |

---

## 📝 Submission Steps (IEEE RAM via PaperCept)

1. **Compile to PDF** in Overleaf
2. **Download PDF** (max 2 MB)
3. Go to **PaperCept.net** (IEEE's submission system)
4. Log in / create account
5. Select **IEEE RAM** as journal
6. Fill metadata (title, authors, keywords)
7. Upload PDF
8. Review submission
9. **Submit**

---

## 💡 Why Magazine Format for IEEE RAM?

IEEE RAM is a **magazine**, not a conference proceedings journal:

✅ Magazine format reads better for practitioners  
✅ Single column is easier to read  
✅ Figures have more breathing room  
✅ Better visual presentation  
✅ Professional appearance  
✅ Aligns with IEEE RAM's published style  

---

## 📖 Resources

- **IEEE RAM Homepage:** https://www.ieee-ras.org/publications/ram/
- **IEEE Author Guidelines:** https://www.ieee.org/publications/authors/
- **Overleaf Help:** https://www.overleaf.com/learn
- **PaperCept Submissions:** https://papercept.net

---

**Version:** 1.0 Magazine Format  
**Date:** September 2026  
**Status:** Ready to compile ✅  
**Recommended for:** IEEE RAM submission
