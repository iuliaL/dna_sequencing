import matplotlib.pyplot as plt


# Phred33: summing 33 to sequenced-base qualities (Q) and then converting them to ASCII encoded chars

def QToPhred33(num):
    return char(num + 33)

def phred33ToQ(char):
    return ord(char) - 33

def createHistogram(qualities):
    h = [0] * 50
    for qual in qualities:
        for phred in qual:
            Q = phred33ToQ(phred) 
            h[Q] += 1
    return h

def plotHistogram(qualities):
    histogram = createHistogram(qualities)
    x = range(len(histogram))
    y = histogram
    plt.bar(x, y)
    plt.show()