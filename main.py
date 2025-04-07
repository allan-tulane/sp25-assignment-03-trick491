import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]

    if T == "":
        return len(S)
    if S == "":
        return len(T)

    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    
    if S == "":
        result = ("-" * len(T), T)
        MED[(S, T)] = result
        return result
    elif T == "":
        result = (S, "-" * len(S))
        MED[(S, T)] = result
        return result
    
    if S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        result = (S[0] + align_S, T[0] + align_T)
        MED[(S, T)] = result
        return result
    
    ins_cost = fast_MED(S, T[1:], {})  
    del_cost = fast_MED(S[1:], T, {})    
    sub_cost = fast_MED(S[1:], T[1:], {}) 
    
    ins_S, ins_T = fast_align_MED(S, T[1:], {})
    del_S, del_T = fast_align_MED(S[1:], T, {})
    sub_S, sub_T = fast_align_MED(S[1:], T[1:], {})
    
    min_cost = min(ins_cost, del_cost, sub_cost)
    
    
    if ins_cost <= del_cost and ins_cost <= sub_cost:
        result = ("-" + ins_S, T[0] + ins_T) 
    elif del_cost <= sub_cost:
        result = (S[0] + del_S, "-" + del_T) 
    else:
        result = (S[0] + sub_S, T[0] + sub_T) 
    
    MED[(S, T)] = result
    return result
