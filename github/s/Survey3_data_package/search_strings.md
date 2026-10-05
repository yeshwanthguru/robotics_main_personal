# Search strategy

## Stage 1: initial list (108 works)

A curated reading list assembled while the orchestration framework was being designed. Every item was
checked against its arXiv or publisher record; 30 items needed a correction to year, venue, title or
authors (listed in `../Survey3_method_workbook/OSF_protocol.md`, Section 6).

## Stage 2: structured searches, September 2026 (72 works added)

Searches of arXiv, the proceedings of CoRL, RSS, ICRA, IROS, NeurIPS, ICML and ICLR, and publisher
sites, in ten topic streams:

1. uncertainty-aware LLM and VLA planning, help-seeking and conformal planning;
2. efficient, small and edge VLAs (quantisation, distillation, compact backbones);
3. budget-aware model routing and cascades;
4. RL fine-tuning of large policies and residual RL on imitation policies;
5. failure detection and recovery with foundation models;
6. uncertainty fusion and calibration across modalities;
7. continual and on-device learning (PEFT, replay, memory-limited training);
8. adaptive computation and mixture of experts in robot policies;
9. safe learning (shields, simplex, safety filters);
10. low-cost hardware and real-robot evaluation methodology.

Backward citation chasing from the reviews in the corpus (Gawlikowski et al. 2023; Hospedales et al.
2022; De Lange et al. 2022; Yu et al. 2025; Brunke et al. 2022) supplemented the streams.

The exact strings and the number of records each search returned were **not logged**. The concept
blocks below reproduce the scope of the streams; they are a reconstruction, not a log.

```
Block A (agent):      robot* OR embodied OR "mobile manipulat*" OR "vision-language-action" OR VLA
Block B (mechanism):  orchestrat* OR routing OR router OR gating OR "mixture of experts" OR cascade
                      OR "meta-learn*" OR "adaptive computation" OR "early exit" OR "tool use"
Block C (signal):     uncertainty OR confidence OR calibrat* OR conformal OR "failure detection"
                      OR anomaly OR "out-of-distribution"
Block D (constraint): edge OR on-device OR embedded OR "Raspberry Pi" OR Jetson OR "low-cost"
                      OR quantiz* OR "parameter-efficient" OR LoRA OR budget

Streams 1, 5, 6:  A AND C          Streams 3, 8: B AND (C OR D)
Streams 2, 7:     A AND D          Stream 4: A AND ("reinforcement learning" AND (fine-tun* OR residual))
Stream 9:         A AND (shield OR simplex OR "safety filter")
Stream 10:        A AND D AND (benchmark OR evaluation OR "statistical")
```

Limits: English; 1991–2026 for foundational methods, 2021–2026 for robot foundation models.

## Stage 3: targeted search, 4 October 2026

Seven topic and verification queries on the title topic (meta-learning orchestration on
resource-constrained robots). Exact queries, results and decisions:
`../Survey3_method_workbook/targeted_search_record.md`. No work was added; four candidates are
recorded for full-text screening.

Corpus closed on 4 October 2026.
