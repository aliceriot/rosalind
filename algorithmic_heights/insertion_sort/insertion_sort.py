

def insertion_sort(array,n):
    count = 0
    for i in range(1,n):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array = swap(array,k-1,k)
            k -= 1
            count += 1
    return array, count

def swap(array,first,second):
    placeholder = array[first]
    array[first] = array[second]
    array[second] = placeholder
    return array



with open ("/home/benpote/Downloads/rosalind_ins.txt", "r") as myfile:
    data=myfile.read().split('\n')

n = int(data[0])

num = [int(i) for i in data[1].split(' ')]

insertion_sort(num,n)

