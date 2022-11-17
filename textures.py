import struct
from extras import *
from vector import *


class Texture:
    def __init__(self, path):
        self.path = path
        self.read()

    def read (self):
        with open (self.path, "rb") as image:

            image.seek(2 + 4 + 2 + 2)
            header_size = struct.unpack("=l", image.read(4))[0]

            image.seek(2+4+2+2+4+4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)
            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(color(r,g,b))


    def GetColor(self, tx,ty):
        x = round(tx*self.width)
        y = round(ty*self.height)

        return self.pixels[y][x]

    def GetColorIntensity(self,tx,ty,intensity):
        x = round(tx * self.width)
        y = round(ty * self.height)


        b = round(self.pixels[y][x][0] * intensity)
        g = round(self.pixels[y][x][1] * intensity)
        r = round(self.pixels[y][x][2] * intensity)

        return color(r,g,b)
"""
r = Render.Render(1024,1024)
t = Texture('./model.bmp')

r.framebuffer = t.pixels

# # Cara Clase
# scale_factor = (500,500,600)
# translate_factor = (525, 500,0)

cube = Obj.Obj('./model.obj')

# r.color_actual=color(255,255,255)

r.color_actual=color(255,255,255)

for face in cube.faces:
    if len(face) == 3:
        f1 = face[0][1] - 1
        f2 = face[1][1] - 1
        f3 = face[2][1] - 1

        vt1 = V3(cube.tvertices[f1][0]*t.width,cube.tvertices[f1][1]*t.height)
        vt2 = V3(cube.tvertices[f2][0]*t.width,cube.tvertices[f2][1]*t.height)
        vt3 = V3(cube.tvertices[f3][0]*t.width,cube.tvertices[f3][1]*t.height)

        # print(round(vt1.x),round(vt1.y))
        # print(round(vt2.x),round(vt2.y))
        # print(round(vt3.x),round(vt3.y))
        # print(vt1,vt2,vt3)
        # r.line(vt1.x,vt1.y,vt2.x,vt2.y)
        # r.line(vt2.x,vt2.y,vt3.x,vt3.y)
        # r.line(vt3.x,vt3.y,vt1.x,vt1.y)
        r.line(vt1,vt2)
        r.line(vt2,vt3)
        r.line(vt3,vt1)

        # try:
        #     r.line(vt1,vt2)
        #     r.line(vt2,vt3)
        #     r.line(vt3,vt1)
        # except:
        #     r.line2(vt1.x,vt1.y,vt2.x,vt2.y)
        #     r.line2(vt2.x,vt2.y,vt3.x,vt3.y)
        #     r.line2(vt3.x,vt3.y,vt1.x,vt1.y)


        # r.line(vt1,vt2)
        # r.line(vt2,vt3)
        # r.line(vt3,vt1)
        # gl.triangulo_version_dos(v1,v2,v3)
        # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
        # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
        # gl.glLine3(v3[0][0], v3[0][1], v1[0][0],v1[0][1])
        # break

r.write('./t.bmp')

# print(t.GetColorIntensity(0,0,1))
"""