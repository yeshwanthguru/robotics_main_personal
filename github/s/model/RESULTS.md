# Results summary

All numbers come from `results/*.json` (30 repetitions per condition, fixed seeds) and are quoted in
`paper/main.tex`. Simulated people only, except the published aggregates in Experiment 5. No quantum
hardware has been used.

| Experiment | Main result |
|---|---|
| 1. Model recovery | Homogeneous populations: the QL generator is identified in 86%, 93% and 100% of data sets with 100, 400 and 1,600 people per order; Bayes 30/71/98%; anchoring 27/64/97%. With 100 people per order, Bayes data are taken for QL in 63 of 90 data sets. With individual differences, QL recovery falls to 66–79%. The QQ test detects the anchoring generator in 31–62% of data sets. |
| 2. Cross-order prediction | When people follow QL and are alike, QL predicts the unasked order best (median KL 0.004 vs 0.014 for Bayes at N = 400). With individual differences the advantage shrinks to a tie (N = 400) or a small margin (N = 4,000). When people follow anchoring, QL is the worst model (KL 0.23–0.26, about ten times Bayes). Bayes is never worse than 0.03. |
| 3. Questioning design | Randomizing the question order (half each order) and using first answers gives RMSE 0.028–0.037 under every generator. A fixed order gives 0.050–0.076 when order effects exist. Model-based correction helps only with the right model; a wrong model gives up to 0.24. |
| 4. Trust | Under open-system dynamics a midway trust question lowers final trust from 0.725 to 0.649 (−0.076); the Markov model predicts no change. The open-system generator is identified in 3%, 27% and 93% of data sets with 100, 400 and 1,600 people per condition. A robot that always asks cannot learn the effect (bias −0.06 to −0.08). |
| 5. Published data | Clinton–Gore poll: QL (SSE 1.4e-5) and one-weight anchoring (2.5e-5) fit the four rates; Bayes cannot (5.7e-3). Prisoner's Dilemma: the observed 0.63 defection rate lies outside the classical range 0.84–0.97; the quantum-like law reaches it with one interference phase (1.88 rad). |
| 6. Circuits | Ideal simulators reproduce the analytic distributions (TVD 0.003–0.007). FakeTorino noise: TVD 0.037–0.041 (dynamic), 0.044–0.056 (deferred); QQ value within 0.012 of zero; trust query effect preserved (−0.077). FakeBrisbane: TVD 0.052–0.055. Depolarizing 2% per gate: TVD 0.105–0.119. |

## Final conclusion

Quantum-like models are a useful but conditional part of a robot's model of people. They capture
order effects and question-induced changes that classical models cannot, they can be identified with
a few hundred people per question order when people are alike, and they run on current quantum
hardware noise models with small distortion. But they are the worst predictor when people follow a
classical order effect, and individual differences erode their advantage. A robot should therefore
(1) randomize its question order when it needs unprimed answers, (2) weight quantum-like and classical
models by evidence rather than commit to one, and (3) treat a trust question as an action that can
change trust, collecting data with and without it. Whether real people in human–robot interaction
follow these models is the open question; the proposed human study (PUBLICATION_PLAN.md, Section 5)
would answer it.
