
#a class to hold all of the variables we need
class ElementArray:
    def __init__(self,input_string):
        elements = [[int(i) for i in k.split(' ')] for k in data.split('\n') if k != '']
        self.k = elements[0][0]
        self.n = elements[0][1]
        self.arrays = elements[1:]

    #a method to get the majority elements of all the lists in the arrays variable
    def majorityElements(self):
        def majElemHelper(array_elem):
            count = 0
            majority_element = -1
            for i in range(len(array_elem)):
                if count == 0:
                    majority_element = array_elem[i]
                if array_elem[i] == majority_element:
                    count += 1
                else:
                    count -= 1
            count = 0
            for i in range(len(array_elem)):
                if (array_elem[i] == majority_element):
                    count += 1
            if count > (len(array_elem) / 2):
                return majority_element
            else:
                return -1
        out = [majElemHelper(i) for i in self.arrays]
        return out
            



with open ("/home/benpote/Downloads/rosalind_maj.txt", "r") as myfile:
    data = myfile.read()
        
elementArray = ElementArray(data)
#I did it in ipython, but to get our answer we run:
elementArray.majorityElements()



