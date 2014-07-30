#!/usr/bin/python

# a binary search algorithm (naive sort of one)
# we get an array of numbers
# input:
# n size of array 
# m size of query
# n sorted integers (array)
# m unsorted integers (query)
# we return where each k_m \in query is in array, and -1 if it is not found


class BinSearchArray:
    def __init__(self,n,m,array,query):
        self.array = array
        self.query = query
        self.n = n
        self.m = m

    def search(self):
        indices = []
        for i in self.query:
            indices.append(arrayFind(i,self.array,0))
        return indices


#a recursive but not tail-call-ey algo
#recursive but iterative? I guess
#we use stored to store the value of the indices to the left, if any
#rather than doing tail-calls or something
def arrayFind(key,array,stored):
    n = len(array)
    if n == 0:
        return "yikes!"
    if n == 1:
        if key == array[0]:
            return (stored + 1)
        else:
            return (-1)
    if n == 2:
        if key == array[0]:
            return (stored + 1)
        elif key == array[1]:
            return (stored + 2)
        else:
            return (-1)
    if key < array[(n/2)]:
        return arrayFind(key,array[:(n/2)],stored)
    elif key > array[(n/2)]:
        return arrayFind(key,array[(n/2):],stored + (n/2))
    else:
        return (stored + (n/2) + 1)

#read in file and instantiate the class

with open ("/home/benpote/Downloads/rosalind_bins (5).txt", "r") as myfile:
    data=myfile.read().split('\n')

n = int(data[0])
m = int(data[1])
array = [int(i) for i in data[2].split(' ')]
query = [int(i) for i in data[3].split(' ')]

getAnswer = BinSearchArray(n,m,array,query)
answer = getAnswer.search()

out = ""
for i in answer:
    out += str(i) + " "

f1 = open('/home/benpote/Code/rosalind/algorithmic_heights/binary_search/output.txt', 'w+')

print >> f1, out, i

#it works for the example/test data, but I can't figure out how to make it work for the
#real data - this is the frustrating thing about rosalind
