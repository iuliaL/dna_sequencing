from HammingDistance import HammingDistance
from lib.bm_preproc import BoyerMoore as bm
from BoyerMooreMatching import BoyerMooreExactMatching


def NaiveApproximatePatternMatching(Pattern, Genome, d=2):
    '''Naive, goes one nucleotide at a time checking all possible positions'''
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        current = Genome[i: i + len(Pattern)]
        if HammingDistance(current, Pattern) <= d:
            positions.append(i)
    return positions


def BoyerMooreApproximatePatternMatching(Pattern, Genome, d=2):  # d is the distance meaning allowed mismatches
    # split pattern into d + 1 segments
    # this means at least one of the segments of pattern will match exactly somewhere in the genome
    # (the pigeonhole principle) https://www.coursera.org/learn/dna-sequencing/lecture/QSGKX/lecture-pigeonhole-principle
    num_segments = d + 1
    segment_length = round(len(Pattern) / num_segments)
    all_matches = set()

    for i in range(num_segments):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(Pattern))
        curr_segment = Pattern[start:end]
        processed_segment = bm(curr_segment)
        matches = BoyerMooreExactMatching(curr_segment, processed_segment, Genome)  # exact match positions of the segment in the genome
        # Extend matching segments to see if whole pattern matches
        for m in matches:
            if start > m or m - start + len(Pattern) > len(Genome):
                continue
            window_to_check = Genome[m - start: m - start + len(Pattern)]
            mismatches = HammingDistance(Pattern, window_to_check)
            if mismatches <= d:
                all_matches.add(m - start)
    return list(all_matches)

