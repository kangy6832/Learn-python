class Point :
    def __init__ (self, x, y):
        self.x, self.y = x, y

    def distence_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return ((dx ** 2 + dy ** 2) ** 0.5)
    
    def __str__ (self) :
        return f'({self.x}, {self.y})'
    
p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)
print(p2)
print(p1.distence_to(p2))
