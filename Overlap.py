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

from itertools import permutations

# reads are sequence reads, k is minimum length overlap
def NaiveOverlapMap(reads, k):
        overlaps = {}
        for a,b in permutations(reads, 2):
            overlap_length = Overlap(a, b, k)
            if overlap_length:
                overlaps[(a,b)] = overlap_length
        return overlaps