from lib.BoyerMoorePreprocessing import BoyerMoore as bm

# GCTAGCTC
# TCAA

def BoyerMooreMatching(pattern, genome):
    '''Find all the positions of a given pattern in genome using BoyerMoore'''

    boyerMoore = bm(pattern)
    positions = []
    i = 0
    k = len(pattern)

    while i < len(genome) - k + 1:
        shift = 1 # the minimum shift is 1
        mismatched = False
        current_kmer = genome[i: i + k]
        for j in range(k - 1, -1, -1): # iterate over all chars of pattern backwards
            if not pattern[j] == current_kmer[j]:
                mismatched = True
                mismatched_char = current_kmer[j]
                skip_bad_char = boyerMoore.bad_character_rule(j, mismatched_char)
                skip_good_suffix = boyerMoore.good_suffix_rule(j)
                shift = max(shift, skip_bad_char, skip_good_suffix)
                break
        if not mismatched:
            positions.append(i)
            shift = max(shift, boyerMoore.match_skip()) # pattern matches entirely the current kmer
        i += shift

    return positions 

