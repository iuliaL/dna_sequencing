from Overlap import Overlap
from itertools import permutations
from Overlap import pick_Maximal_overlap

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

# my implementation (recursive, works ok)
def GreedySCS(reads, k):
    """ Greedy shortest-common-superstring merge.
         Repeat until no edges (overlaps of length >= k)
         remain. """
    read_a, read_b, max_overlap_length = pick_Maximal_overlap(reads, k)
    if max_overlap_length > 0:
        new_superstring = read_a + read_b[max_overlap_length:]
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(new_superstring)
        return GreedySCS(reads, k)
    else:
        return ''.join(reads)


# print(GreedySCS(['ABCD', 'CDBC', 'BCDA'], 1)) # => not always accurate returns CDBCABCDA
# print(NaiveSCS(['ABCD', 'CDBC', 'BCDA'])) => ABCDBCDA
