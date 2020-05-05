from HammingDistance import HammingDistance

def ApproximatePatternMatching(Pattern, Genome, d=2):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        current = Genome[i: i + len(Pattern)]
        if HammingDistance(current, Pattern) <= d:
            positions.append(i)  
    return positions