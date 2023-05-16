

class Numbers:
    MULTIPLIER = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(cls,a):
        return a * cls.MULTIPLIER
    @staticmethod
    def substract(b,c):
        return b - c
    @property
    def values(self):
        return (self.x,self.y)
    @values.setter
    def valuesSetter(self,x ,y):
        self.x=x
        self.y=y
    # code here...

c=Numbers(2,5)
print(c.add())
print(c.multiply(2))
print(c.valuesSetter(3,6))