"""Turn simple inline LaTeX math ($...$) into Unicode text for the Word version,
so Word does not break lines around separate equation objects."""
import re

SUP = str.maketrans('0123456789-+n()', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ⁽⁾')
SYM = [(r'\psi', 'ψ'), (r'\alpha', 'α'), (r'\beta', 'β'), (r'\rangle', '⟩'), (r'\langle', '⟨'),
       (r'\times', '×'), (r'\approx', '≈'), (r'\mu', 'µ'), (r'\pi', 'π'), (r'\epsilon', 'ε'),
       (r'\le', '≤'), (r'\ge', '≥'), (r'\pm', '±'), (r'\in', '∈'), (r'\top', 'ᵀ'),
       (r'\checkmark', '✓'), (r'^\circ', '°'), (r'^\dagger', '†'), (r'\dagger', '†'), (r'\{', '{'), (r'\}', '}'), ('{,}', ','), ('~', ' ')]


def to_unicode(m):
    t = m.group(1)
    t = re.sub(r'\\mathrm\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1/\2)', t)
    t = re.sub(r'\\sqrt\{([^{}]*)\}', r'√\1', t)
    if t.startswith('\\min_'):  # QUBO objective
        return 'min xᵀQx over x ∈ {0,1}ⁿ'
    for a, b in SYM:
        t = t.replace(a, b)
    t = re.sub(r'\^\{\s*(?:\\top|ᵀ)\s*\}', 'ᵀ', t)
    t = re.sub(r'\^\{([0-9n()+-]+)\}', lambda s: s.group(1).translate(SUP), t)
    t = re.sub(r'\^([0-9n])', lambda s: s.group(1).translate(SUP), t)
    if '\\' in t or '_' in t or '^' in t:
        return m.group(0)          # leave anything still complex as an equation
    t = re.sub(r'\s*([=+×≈<>≤±])\s*', r' \1 ', t).replace('  ', ' ').strip()
    t = re.sub(r'([⟩|]) \+ ', r'\1 + ', t)
    return t


def convert(body):
    return re.sub(r'(?<![\\$])\$([^$\n]+?)\$(?!\$)', to_unicode, body)
