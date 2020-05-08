
def NaiveExactPatternMatching(Pattern, Genome):
    positions = []
    k = len(Pattern)
    for index in range(len(Genome) - k + 1):
        currentKmer = Genome[index:index + k]
        kmer_match = True
        for i in range(len(currentKmer)):
            if currentKmer[i] != Pattern[i]:
                kmer_match = False
                break
        if kmer_match:
            positions.append(index)
    return positions

def NaiveExactPatternMatchingWithCounts(Pattern, Genome):
    positions = []
    num_alignments = 0
    num_character_comparisons = 0

    k = len(Pattern)
    for index in range(len(Genome) - k + 1):
        currentKmer = Genome[index:index + k]
        kmer_match = True
        num_alignments += 1
        for i in range(len(currentKmer)):
            num_character_comparisons += 1
            if currentKmer[i] != Pattern[i]:
                kmer_match = False
                break
        if kmer_match:
            positions.append(index)

    return positions, num_alignments, num_character_comparisons


