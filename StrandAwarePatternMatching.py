from ReverseComplement import ReverseComplement

# a given match index should be reported only once if Pattern and its reverse complement are identical (e.g AACGTT)

def StrandAwarePatternMatching(Pattern, Genome):
    positions = []
    k = len(Pattern)
    for index in range(len(Genome) - k + 1):
        currentKmer = Genome[index:index + k]
        rc = ReverseComplement(currentKmer)
        kmer_match = True
        rc_match = True
        for i in range(len(currentKmer)):
            if currentKmer[i] != Pattern[i]:
                kmer_match = False
                break
        if currentKmer != rc:
            for i in range(len(rc)):
                if rc[i] != Pattern[i]:
                    rc_match = False
                    break
        if kmer_match:
            positions.append(index)
        if rc_match and currentKmer != rc:
            positions.append(index)
    return positions

