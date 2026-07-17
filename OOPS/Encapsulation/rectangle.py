class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
        else:
            print("Length must be positive")

    @property
    def breadth(self):
        return self.__breadth

    @breadth.setter
    def breadth(self, value):
        if value > 0:
            self.__breadth = value
        else:
            print("Breadth must be positive")

    @property
    def area(self):
        return self.__length * self.__breadth


r = Rectangle(4, 3)

print("Area:", r.area)

r.length = 10
r.breadth = 5

print("New Area:", r.area)