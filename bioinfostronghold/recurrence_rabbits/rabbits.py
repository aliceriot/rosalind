#want to write something which does this fibonacci recurrence thingum, starting with 1

#this is a shitty one I made that doesn't work derrrp
def rabbits(n, k):
    init = 1
    pop = 1
    for i in range(n):
        pop += pop * k
    return pop



#this works! always just whiteboard it
#rosalind thinks it works too! woo
def rabbits2(n, k):
    pops = [1,1]
    while len(pops) < n:
        pops.append(pops[-1] + (pops[-2] * k))
    return pops[-1]
# I think this is a pythonic way to do it, using a list
# no for loop, I really don't think that's the best way to accomplish this






