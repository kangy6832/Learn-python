class Triangle :
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def is_available(x, y, z):
        return x + y > z and x + z > y and y + z > x
    
    @property
    def perimeter (self):
        return self.x + self.y + self.z
    
    @property
    def area (self):
        p = self.perimeter / 2
        return (p * (p - self.z) * (p - self.x) * (p - self.y)) ** 0.5
    
if Triangle.is_available(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长:{t.perimeter}')
    print(f'面积:{t.area}')
else :
    print('无效长度')