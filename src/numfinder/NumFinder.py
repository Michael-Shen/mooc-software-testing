"""
Course  Topic 1: Automated Software Testing   -> Introduction -> Why is software testing important?
NumFinder to find the max and min in a given list
"""

class NumFinder:
    def __init__(self,list):
        self.list = list
        
    def find(self):
        max = self.list[0]
        min = self.list[0]
        for i in self.list:
            if i >= max:
                max = i 
            if i <= min:
                min = i 
        return (max,min)
        
if __name__== '__main__': # pragma: no cover
    foo = NumFinder([2,5,9,1,100,20])
    print(foo.find())
    
    foo2 = NumFinder([-1,5,9,1,-100,20])
    print(foo2.find())