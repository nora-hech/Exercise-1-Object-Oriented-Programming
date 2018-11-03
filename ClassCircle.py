# Circle class in Python
import numpy as np
 
    
class Circle():
    
    # Initializer / Instance Attribute
    def __init__(self, radius):
        self.radius=radius
        
    # instance methods
    def area(self):
        return np.pi*self.radius**2
        
    def perimeter(self):
        return 2*np.pi*self.radius
        
def main(r):
        
    C=Circle(r)
    print C.radius
    print C.area()
    print "The area of a circle with a radius of "+str(C.radius)+" cm is "+str(C.area())+" cm*cm"


main(5)
