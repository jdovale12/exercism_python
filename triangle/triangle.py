import numpy as np

def equilateral(sides):
    x = np.array(sides)
    if x.all():
        if x[0] != x [1] or x[0] != x [2] :
            return False
        else:
            return True
    else:
        return False
    
def isosceles(sides):
    x = np.array(sides)
    if x.all():
        aux = 0
        for i in x:
            for j in x:
                if i != j:
                    aux+=1
        if aux>:
            return False
        else:
            return True
    else:
        return False


def scalene(sides):
    x = np.array(sides)
    if x.all():
        aux = 0
        for i in x:
            for j in x:
                if i != j:
                    aux+=1
        if aux>6:
            return True
        else:
            return False
    else:
        return False
