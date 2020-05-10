from itertools import permutations
from collections import defaultdict
import operator

# overlaps that are exact matches 

# a  TAATGTAAT
#         ||||
# b       TAATAAC

def Overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0
    while True:
        # look for b's prefix in a
        start = a.find(b[:min_length], start) # Python Docs: string.find(value, start, end)
        if start == -1:
            return 0

        if b.startswith(a[start:]):
            return len(a) - start 
        start += 1


# reads are sequence reads, k is minimum length overlap
def NaiveOverlapMap(reads, k):
        overlaps = {}
        for a,b in permutations(reads, 2):
            overlap_length = Overlap(a, b, k)
            if overlap_length:
                overlaps[(a,b)] = overlap_length
        return overlaps


def OverlapGraph(reads, k=30): # k is minimum length overlap
    kmers_in_reads = defaultdict(set)
    edges = []
    # For every k-mer in a read, we add the read to the set corresponding to that k-mer
    for read in reads:
        for i in range(len(read) - k + 1):
            curr_kmer = read[i:i+k]
            kmers_in_reads[curr_kmer].add(read)

    for read in reads:
        suffix = read[len(read) - k:]
        # find all reads containing that k-mer (obtained from the corresponding set)
        reads_containing_suffix = kmers_in_reads[suffix]
        # and call Overlap(a, b, min_length=k) for each
        for r in reads_containing_suffix:
            if r != read: # do not overlap a read with itself
                overlap = Overlap(read, r, k)
                if overlap:
                    edges.append((read, r))
    return edges



def pick_Maximal_overlap(reads, k):
    """ Return a pair of reads from the list with a
        maximal suffix/prefix overlap >= k.  Returns
        overlap length 0 if there are no such overlaps."""
    reada, readb = None, None
    best_olen = 0
    for a, b in permutations(reads, 2):
        olen = Overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen