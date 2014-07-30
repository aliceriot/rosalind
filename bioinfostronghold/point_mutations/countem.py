#want to write a function which takes two strings and counts the point mutation differences between them (differences at the same position)
with open ("/home/benpote/Downloads/rosalind_hamm.txt", "r") as myfile:
    data = myfile.read()

datasplit = data.split('\n')


def pmcount(seq1,seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
        else:
            continue
    return count

#it works! let's make it parse in the file and be a bit more automatic though

pmcount(datasplit[0],datasplit[1])
#the above works too! woohoo!
