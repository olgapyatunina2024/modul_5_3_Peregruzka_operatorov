class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'

    def __eq__(self, other):    # 1
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors == other.nFloors

    def __lt__(self, other):    # 2
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors < other.nFloors

    def __le__(self, other):
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors <= other.nFloors

    def __gt__(self, other):
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors > other.nFloors

    def __ge__(self, other):
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors >= other.nFloors

    def __ne__(self, other):
        if isinstance(other.nFloors, int) and isinstance(other, House):
            return self.nFloors != other.nFloors

    def __add__(self, value):
        if isinstance(value, int):
            self.nFloors = self.nFloors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.nFloors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


