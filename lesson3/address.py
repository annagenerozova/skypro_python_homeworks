class Address:
    
    def __init__(self, index, city, street, house, apartment):
        self.i = index
        self.c = city
        self.s = street
        self.h = house
        self.a = apartment
    
    def __str__(self):
        return f"{self.i}, {self.c}, {self.s}, {self.h} - {self.a}"