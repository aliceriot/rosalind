#quick script to give you the reverse complement of a sequence

#the 'file read' is yanked from the last question
with open ("/home/benpote/Downloads/rosalind_revc (2).txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

#quick little function to reverse the string and substitute 'U' for 'T'

def revcomp(seq):
    out = ""
    seq = seq[::-1]
    for i in seq:
        if i == 'T':
            out += 'A'
        elif i == 'A':
            out += 'T' #we're not supposed to make it RNA yet...
        elif i == 'C':
            out += 'G'
        elif i == 'G':
            out += 'C'
    return out

#it works! hooray

rna = revcomp(data)
