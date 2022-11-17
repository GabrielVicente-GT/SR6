from numpy import *
class V3(object):
    def __init__(self,x,y = 0,z = 0,w=1):
        if (type(x) == matrix):
            self.x, self.y, self.z, self.w = x.tolist()[0]
        else:
            self.x = x
            self.y = y
            self.z = z
            self.w = w

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        self.z = round(self.z)
    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__ (self, other):
        if (type(other) == int or type(other) == float):
            return V3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        return V3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __matmul__(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def len(self):
        return(self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        try: #Si el vector no es cero, entonces normaliza.
            return self * (1 / self.len())
        except: #Si el vector es cero, entonces devuelve un vector cero.
            return V3(-1, -1, -1)

    def __repr__(self):
        return "V3(%s,%s,%s)" & (self.x,self.y,self.z)

    def __str__(self):
        cadena = str(self.x)+" "+str(self.y)+" "+str(self.z)+" "
        return cadena