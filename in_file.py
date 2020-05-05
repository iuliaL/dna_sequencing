def read_fa(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def read_fastq(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as f:
        while True:
            f.readline() # ignore first line
            seq = f.readline().rstrip()
            f.readline() # ignore 3rd line
            qual = f.readline().rstrip()
            if len(seq) == 0: # EOF
                break
            else:
                sequences.append(seq)
                qualities.append(qual)
    return sequences, qualities