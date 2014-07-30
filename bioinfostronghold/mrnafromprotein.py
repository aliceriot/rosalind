#here we want to try to figure out what a mrna sequence corresponding to a particular protein
#might look like!
#what fun!

#so basically we're going to read in a file containing a protein string

with open ("/home/benpote/Downloads/rosalind_mrna (2).txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

transmat = dict([('F',2),('L',6),('S',6),('Y',2),('C',2),('W',1),('P',4),('H',2),('Q',2),('R',6),('I',3),('M',1),('T',4),('N',2),('K',2),('V',4),('A',4),('D',2),('E',2),('G',4)])

def pos_mrna(seq):
    num = 1
    for i in seq:
        num *= transmat[i] #this gives us the possible sequences due to proteins
    num *= 3 #3 possible stop codons
    return num
        
#I'm not sure why this isn't working! rrrr
#rosalind can be very annoying sometimes
