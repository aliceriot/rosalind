#rosalind problem, rna -> protein

#the motherfucker works!
#first we want to open up our datafile
with open ("/home/benpote/Downloads/rosalind_prot (8).txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

#now we'd like to write a function which pages through a string an mRNA string and build
#a protein string from it

def rnaprot(mrna):
    prot = ''
    codons = [mrna[i:i+3] for i in range(0,len(mrna),3)]
    for i in codons:
        if i == 'UUU' or i == 'UUC':
            prot += 'F'
        elif i == 'UUA' or i == 'UUG':
            prot += 'L'
        elif i == 'UCU' or i == 'UCC' or i == 'UCA' or i == 'UCG':
            prot += 'S'
        elif i == 'UAU' or i == 'UAC':
            prot += 'Y'
        elif i == 'UAA' or i == 'UAG' or i == 'UGA':
            return prot
        elif i == 'UGU' or i == 'UGC':
            prot += 'C'
        elif i == 'UGG':
            prot += 'W'
        elif i == 'CUU' or i == 'CUC' or i == 'CUA' or i == 'CUG':
            prot += 'L'
        elif i == 'CCU' or i == 'CCC' or i == 'CCA' or i == 'CCG':
            prot += 'P'
        elif i == 'CAU' or i == 'CAC':
            prot += 'H'
        elif i == 'CAA' or i == 'CAG':
            prot += 'Q'
        elif i == 'CGU' or i == 'CGC' or i == 'CGA' or i == 'CGG' or i == 'AGA' or i == 'AGG':
            prot += 'R'
        elif i == 'AUU' or i == 'AUC' or i == 'AUA':
            prot += 'I'
        elif i == 'AUG':
            prot += 'M'
        elif i == 'ACU' or i == 'ACC' or i == 'ACA' or i == 'ACG':
            prot += 'T'
        elif i == 'AAU' or i == 'AAC':
            prot += 'N'
        elif i == 'AAA' or i == 'AAG':
            prot += 'K'
        elif i == 'AGU' or i == 'AGC':
            prot += 'S'
        elif i == 'GUU' or i == 'GUC' or i == 'GUA' or i == 'GUG':
            prot += 'V'
        elif i == 'GCU' or i == 'GCC' or i == 'GCA' or i == 'GCG':
            prot += 'A'
        elif i == 'GAU' or i == 'GAC':
            prot += 'D'
        elif i == 'GAA' or i == 'GAG':
            prot += 'E'
        elif i == 'GGU' or i == 'GGC' or i == 'GGA' or i == 'GGG':
            prot += 'G'
    print 'No stop codon, strange...'
    return prot

out = rnaprot(data)
out.strip('\n')

f = open('output.txt', 'w')
f.write(out)

f.close()


