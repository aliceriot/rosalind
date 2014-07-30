#a quick script to take a DNA sequence and turn it into an RNA sequence (e.g. change thymine to uracil)

#first want to read in the file

with open ("/home/benpote/Downloads/rosalind_rna (3).txt", "r") as myfile:
        data=myfile.read().replace('\n', '')
#this reads in the data as a string with no line breaks

#this little function goes through a string, adding a 'U' to the return string (out) when it finds a 'T'
def convertit(seq):
    out = ""
    for i in seq:
        if i == 'T':
            out += 'U'
        else:
            out += i
    return out
    
#now we can just call:

rna = convertit(data)
