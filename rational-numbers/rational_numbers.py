from __future__ import division
from math import gcd

class Rational:
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer = self.numer * other.denom + self.denom * other.denom
        self.denom = self.denom * other.denom
        return self

    def __sub__(self, other):
        self.numer = self.numer * other.denom - self.denom * other.denom
        self.denom = self.denom * other.denom
        return self

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        return self

    def __truediv__(self, other):
        self.numer = self.numer * other.denom
        self.denom = self.denom * other.numer
        return self
    
    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)

    def __pow__(self, power):
        self.numer = self.numer ** power
        self.denom = self.denom ** power
        return self

    def __rpow__(self, base):
        return (base ** (self.numer / self.denom))
    
    def simply(self):
        agcd = gcd(self.numer ,self.denom)
        self.numer = self.numer // agcd
        selfdenom =  self.denom // agcd
        return self
    
    def signs(self):
        if(self.denom<0):
            self.numer = self.numer * -1 
            self.denom = self.denom * -1
