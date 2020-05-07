import bisect

class Index(object):
    ''' Preprocessing (indexing) genome text'''
    def __init__(self, genome, k):
        ''' all kmers in genome along with their occuring positions, sorted alphabetically '''
        self.k = k
        self.index = [] # will be list of tuples
        for i in range(len(genome) - k + 1):
            kmer = genome[i: i + k] 
            self.index.append((kmer, i))
            self.index.sort()

    def query(self, pattern):
        kmer_from_pattern = pattern[:self.k] # take a kmer from searched pattern
        i = bisect.bisect_left(self.index, (kmer_from_pattern, -1)) # putting -1 since -1 would never be an index in self.index
        hits = []
        while i < len(self.index):
            indexed_kmer = self.index[i][0]
            position = self.index[i][1]
            if not indexed_kmer == kmer_from_pattern:
                break
            else:
                hits.append(position)
            i += 1

        return hits # there are actual partial hits since the check is made only for the first k-length bases from pattern

# make use of Index object
# this fn will use an instantiated object of class Index
def queryIndex(pattern, genome, Index):
    k = Index.k
    positions = []
    possible_starting_positions_for_pattern = Index.query(pattern)
    for i in possible_starting_positions_for_pattern:
        if pattern[k:] == genome[i + k : i + len(pattern)]: # verifying the rest of the pattern after k-length bases that were matched by indexing
            positions.append(i) # full pattern match
    return positions

# indexed = Index('GCTAGCTCTACGAGTCTA', 3)
# print(queryIndex('TCTA', 'GCTAGCTCTACGAGTCTA', indexed))
    
