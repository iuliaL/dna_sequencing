from Overlap import Overlap
from itertools import permutations
from Overlap import pick_Maximal_overlap, pick_maximal_overlap_with_precomputed_kmers
import time
from collections import defaultdict, Counter

# brute force
def NaiveSCS(reads):
    """ Returns shortest common superstring of given strings,
        assuming no string is a strict substring of another """
    shortest_superstring = None
    for s in permutations(reads): # returns every possible ordering in the list of reads as tuples
        sup = s[0]
        for i in range(len(reads) - 1):
            overlap_len = Overlap(s[i], s[i+1], min_length=1)
            sup += s[i+1][overlap_len:]
        if shortest_superstring is None or len(sup) < len(shortest_superstring):
            shortest_superstring = sup
    return shortest_superstring

def SCS_list(reads):
    # Returns list of all superstrings that are tied for shortest
    shortest_superstrings = set()
    shortest_superstring = NaiveSCS(reads)
    for s in permutations(reads): # returns every possible ordering in the list of reads as tuples
        shortest = NaiveSCS(s)
        if len(shortest) == len(shortest_superstring):
            shortest_superstrings.add(shortest)
    return shortest_superstrings



def GreedySCS(reads, k):
    """ Greedy shortest-common-superstring merge.
    Repeat until no edges (overlaps of length >= k)
    remain. """
    start = time.process_time()

    read_a, read_b, max_overlap_length = pick_Maximal_overlap(reads, k)
    while max_overlap_length > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[max_overlap_length:])
        read_a, read_b, max_overlap_length = pick_Maximal_overlap(reads, k)

    end = time.process_time()
    print(end-start)
    return ''.join(reads)

def FasterGreedySCS(reads, k=10): # uses precomputed kmers, the rest is the same as the GreedySCS
    start = time.process_time()

    read_a, read_b, max_overlap_length = pick_maximal_overlap_with_precomputed_kmers(reads, k)
    while max_overlap_length > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[max_overlap_length:])
        read_a, read_b, max_overlap_length = pick_maximal_overlap_with_precomputed_kmers(reads, k)

    end = time.process_time()
    print(end-start)
    return ''.join(reads)

