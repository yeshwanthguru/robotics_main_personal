"""qlmodel: order-aware models of human answers and trust for robots that ask questions.

Modules
  quantum_like  projective (quantum-like) question-order model and the QQ equality
  classical     classical baselines: Bayesian joint, Bayesian with response noise, anchoring
  trust         trust dynamics: Markov chain against an open-system (Lindblad) model
  fitting       maximum-likelihood fitting, BIC and held-out log-likelihood
  domains       the three robot domains used in the experiments
  planner       question-order planning and estimation of first-position answer rates
  circuits      quantum-circuit versions (Qiskit) for ideal, noisy and cloud execution
"""
__version__ = '1.0.0'
