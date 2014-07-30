#quick script to calculate GC content

#read in our datafile
with open ("/home/benpote/Downloads/rosalind_gc (4).txt", "r") as myfile:
        data=myfile.read().replace('\n', '')
#this reads in the whole file as one big string

#now we'll split the string every time it finds a >
seqs = data.split('>')
seqs.remove('')

#gc content function
def gccont(seq): #
    """takes a string and returns the number of G or C / length"""
    count = 0
    for i in seq:
        if i == 'G':
            count += 1
        elif i == 'C':
            count += 1
    cont = float(count) / len(seq)
    return cont

#much simpler version that I think works equally well
def gccont2(seq):
    """takes a string and returns the count of G or C / length"""
    gccont = float(seq.count("G") + seq.count("C")) / len(seq)
    return gccont
#is this more 'pythonic'? perhaps.
    

#called the gccont function and get sequence ids
def getresult(fasta): #input file here is a list of fasta sequences
    """main: takes a list of fasta seqs and returns a dictionary with id:gc content pairs"""
    out = {}
    for i in fasta:
        seqid = i[9:13] #get sequence id number
        gc = gccont(i[13:]) #check those list slices!!!
        out[seqid] = gc
    return out

#print out the best one
def keywithmaxval(dic):
    """create a list of the dicts keys and values, return the key associated with the max value"""
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]
    
        
#now we get results by doing
results = getresult(seqs)

#hacky way thats dumb
def show_results(results):
    print "Rosalind_" + keywithmaxval(results) + "\n"
    print results[keywithmaxval(results)]






