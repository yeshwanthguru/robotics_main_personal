# Codebook for extraction_table.csv

One row per primary study (72 rows: 65 graded studies and 7 reviews). UTF-8 with BOM, comma-separated, CRLF line endings.

| Column | Definition |
|---|---|
| Study | Study label (first author et al. [year]); the full reference is in refs.bib of the article. |
| Evidence level | L1 theoretical; L2 simulation; L3 at least part run on quantum hardware (QPU) or quantum sensor/link hardware; L4 quantum computation in a closed loop with a robot or high-fidelity robot simulator; L5 physical robot, vehicle or mechanical control system; L6 end-to-end field deployment with a measured advantage over a classical baseline; Review. "(sim.)" marks a simulated robot environment; "(lab)" a laboratory set-up; "+ real data" simulated quantum circuits on real robot data. |
| Quantum execution | Where the quantum component ran: None (analysis only); Simulated (circuits, annealing or sensors simulated classically); QPU (gate-based processor or quantum annealer); Sensor or link hardware; Classical (quantum-inspired algorithm on conventional hardware); n/a (review). |
| Publication status | Status of the version graded: Journal article; Conference paper; Book or book chapter; Preprint. |
| Robotic task | Robotic function and task addressed. |
| Quantum type | Quantum technology and platform as reported. |
| Method | Method in brief. |
| Setup and data | Experimental set-up, data and baselines. |
| Key result | Main quantitative or qualitative result. |
| Limitation | Principal limitation, including quality criteria not met. |
| DOI or identifier | DOI, arXiv identifier or venue. |
