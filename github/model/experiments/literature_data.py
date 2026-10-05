"""Published aggregate data used in Experiment 5. Only the numbers below are human data; they are
copied from the sources named and were checked against secondary reports on 5 October 2026.

Clinton-Gore order effect (Gallup poll of 6-7 September 1997, reported by Moore, 2002, and analysed by
Wang and Busemeyer, 2013): 'Do you generally think [Bill Clinton / Al Gore] is honest and
trustworthy?' Proportion answering yes: Clinton asked first 0.50, Gore asked first 0.68; Clinton
asked second (after Gore) 0.57, Gore asked second (after Clinton) 0.60.

Prisoner's dilemma disjunction effect (Shafir and Tversky, 1992): proportion of players who
cooperate when the opponent is known to have defected 0.03, known to have cooperated 0.16, and when
the opponent's move is unknown 0.37 (defection 0.97, 0.84 and 0.63)."""

CLINTON_GORE = dict(A='Clinton', B='Gore', pA_first=0.50, pB_first=0.68, pA_second=0.57, pB_second=0.60,
                    source='Moore (2002); Wang and Busemeyer (2013)')
PRISONERS_DILEMMA = dict(defect_given_defect=0.97, defect_given_cooperate=0.84, defect_unknown=0.63,
                         source='Shafir and Tversky (1992)')
