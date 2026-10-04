"""Turn simple inline LaTeX math ($...$) into Unicode text for the Word version of Survey 2,
so Word does not break lines around separate equation objects. Anything still complex is left
as an equation."""
import re

SUP = str.maketrans('0123456789-+n()', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ⁽⁾')
SUB = str.maketrans('0123456789ijkn+-', '₀₁₂₃₄₅₆₇₈₉ᵢⱼₖₙ₊₋')
SYM = [(r'\varepsilon', 'ε'), (r'\epsilon', 'ε'), (r'\psi', 'ψ'), (r'\phi', 'φ'), (r'\alpha', 'α'),
       (r'\beta', 'β'), (r'\gamma', 'γ'), (r'\delta', 'δ'), (r'\theta', 'θ'), (r'\rho', 'ρ'),
       (r'\sigma', 'σ'), (r'\pi', 'π'), (r'\mu', 'µ'), (r'\Sigma', 'Σ'), (r'\sum', 'Σ'),
       (r'\rangle', '⟩'), (r'\langle', '⟨'), (r'\lVert', '‖'), (r'\rVert', '‖'), (r'\|', '‖'),
       (r'\times', '×'), (r'\approx', '≈'), (r'\leq', '≤'), (r'\geq', '≥'), (r'\le', '≤'), (r'\ge', '≥'),
       (r'\pm', '±'), (r'\in', '∈'), (r'\otimes', '⊗'), (r'\rightarrow', '→'), (r'\mapsto', '↦'),
       (r'\wedge', '∧'), (r'\neg', '¬'), (r'\cdot', '·'), (r'\cos', 'cos'), (r'\exp', 'exp'),
       (r'\checkmark', '✓'), (r'^{\dagger}', '†'), (r'^\dagger', '†'), (r'\dagger', '†'),
       (r'^{*}', '*'), (r'\lfloor', '⌊'), (r'\rfloor', '⌋'), (r'\,', ' '), (r'\{', '{'), (r'\}', '}'),
       ('{,}', ','), ('~', ' ')]


def to_unicode(m):
    t = m.group(1)
    t = re.sub(r'\\ket\{([^{}]*)\}', r'|\1⟩', t)
    t = re.sub(r'\\bra\{([^{}]*)\}', r'⟨\1|', t)
    t = re.sub(r'\\(?:mathrm|text)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\mathbb\{C\}', 'ℂ', t)
    t = re.sub(r'\\hat\{x\}', 'x̂', t)
    t = re.sub(r'\\bar\{([A-Z])\}', '\\1\u0304', t)
    t = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1/\2)', t)
    t = re.sub(r'\\tfrac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', t)
    t = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', t)
    for a, b in SYM:
        t = t.replace(a, b)
    t = re.sub(r'\^\{([0-9n()+-]+)\}', lambda s: s.group(1).translate(SUP), t)
    t = re.sub(r'\^([0-9n])', lambda s: s.group(1).translate(SUP), t)
    t = re.sub(r'_\{([0-9ijkn+-]+)\}', lambda s: s.group(1).translate(SUB), t)
    t = re.sub(r'_([0-9ijkn])', lambda s: s.group(1).translate(SUB), t)
    if '\\' in t or '^' in t or '_' in t:
        return m.group(0)          # leave anything still complex (e.g. P_A) as an equation
    t = re.sub(r'\s*([=+×≈<>≤≥±→])\s*', r' \1 ', t).replace('  ', ' ').replace('⟨ ', '⟨').strip()
    return t


def convert(body):
    return re.sub(r'(?<![\\$])\$([^$\n]+?)\$(?!\$)', to_unicode, body)
