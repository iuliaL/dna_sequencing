# GCTAGCTC
# TCAA
# https://www.coursera.org/learn/dna-sequencing/lecture/HYZXj/lecture-boyer-moore-basics

def BoyerMooreExactMatching(pattern, boyer_moore_obj, genome):
    '''Find all the positions of a given pattern in genome using BoyerMoore (exact pattern matching)'''

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
                skip_bad_char = boyer_moore_obj.bad_character_rule(j, mismatched_char)
                skip_good_suffix = boyer_moore_obj.good_suffix_rule(j)
                shift = max(shift, skip_bad_char, skip_good_suffix)
                break
        if not mismatched:
            positions.append(i)
            shift = max(shift, boyer_moore_obj.match_skip()) # pattern matches entirely the current kmer
        i += shift

    return positions


def BoyerMooreExactMatchingWithCounts(pattern, boyer_moore_obj, genome):
    '''Find all the positions of a given pattern in genome using BoyerMoore (exact pattern matching)
        and count number of alignments and char comparisons'''

    positions = []
    num_alignments = 0
    num_character_comparisons = 0

    i = 0
    k = len(pattern)

    while i < len(genome) - k + 1:
        num_alignments += 1
        shift = 1 # the minimum shift is 1
        mismatched = False
        current_kmer = genome[i: i + k]
        for j in range(k - 1, -1, -1): # iterate over all chars of pattern backwards
            num_character_comparisons += 1
            if not pattern[j] == current_kmer[j]:
                mismatched = True
                mismatched_char = current_kmer[j]
                skip_bad_char = boyer_moore_obj.bad_character_rule(j, mismatched_char)
                skip_good_suffix = boyer_moore_obj.good_suffix_rule(j)
                shift = max(shift, skip_bad_char, skip_good_suffix)
                break
        if not mismatched:
            positions.append(i)
            shift = max(shift, boyer_moore_obj.match_skip()) # pattern matches entirely the current kmer
        i += shift

    return positions, num_alignments, num_character_comparisons

