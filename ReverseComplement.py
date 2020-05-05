# Reverse Complement Problem: Find the reverse complement of a DNA string.
#      Input: A DNA string Pattern.
#      Output: The reverse complement of Pattern.


def ReverseComplement(Text):
    pairs = dict(A="T", C="G", G="C", T="A", N="N") # the N is for the bases that were not read correctly by the sequencer
    complement = [
        pairs[x] for x in Text
    ]
    return "".join(complement[::-1])