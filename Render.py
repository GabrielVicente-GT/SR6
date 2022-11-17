#Render proporcionado en clase para trabajar eficientemente
import struct
from extras import *
import MatricesSimuladas as MatrizSimulada

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BLUE  = color(51, 114, 176)
ORANGE = color(243, 156, 18)
RED = color(255, 0, 0)

class Render(object):

    def __init__(self, width, height):
            self.width  = width
            self.heigth = height
            self.color_actual   = BLACK
            self.texture = None
            self.Model = None
            self.View = None
            self.clear()

    def loadViewMatrix(self, x,y,z,center):
        Mi = MatrizSimulada.matrix ([
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0],
            [0, 0, 0, 1]
        ])

        Op = MatrizSimulada.matrix ([
            [1,0,0,-center.x],
            [0,1,0,-center.y],
            [0,0,1,-center.z],
            [0,0,0,1]
        ])

        self.View = Mi @ Op

    def lookAt(self, eye, center, up):
        z = (eye-center).normalize()
        x = (up * z).normalize()
        y = (z * x).normalize()

        self.loadViewMatrix(x,y,z,center)
        self.loadProjectionMatrix(eye, center)
        self.loadViewPortMatrix()

    def loadProjectionMatrix(self,eye, center):

        coeficiente_nuevo=-1/(eye.len()-center.len())

        self.Projection = MatrizSimulada.matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, coeficiente_nuevo, 1]])

    def loadViewPortMatrix(self):
        x,y = 0,0
        w,h = self.width/2, self.heigth/2
        self.ViewPort = MatrizSimulada.matrix([[w,0,0,x+w],[0,h,0,y+h],[0,0,128,128],[0,0,0,1]
        ])


    def loadModelMatrix(self, translate = (0,0,0), scale = (1,1,1), rotate = (0,0,0)):
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translation_matrix = MatrizSimulada.matrix ([
            [1,0,0,translate.x],
            [0,1,0,translate.y],
            [0,0,1,translate.z],
            [0,0,0,1]
        ])

        scale_matrix = MatrizSimulada.matrix ([
            [scale.x,0,0,0],
            [0,scale.y,0,0],
            [0,0,scale.z,0],
            [0,0,0,1]
        ])

        a = rotate.x
        rotation_x = MatrizSimulada.matrix ([
            [1,0,0,0],
            [0,cos(a),-sin(a),0],
            [0,sin(a),cos(a),0],
            [0,0,0,1]
        ])

        a = rotate.y
        rotation_y = MatrizSimulada.matrix ([
            [cos(a),0,sin(a),0],
            [0,1,0,0],
            [-sin(a),0,cos(a),0],
            [0,0,0,1]
        ])

        a = rotate.z
        rotation_z = MatrizSimulada.matrix ([
            [cos(a),-sin(a),0,0],
            [sin(a),cos(a),0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])

        rotation_matrix = rotation_x @ rotation_y @ rotation_z

        self.Model = translation_matrix @ rotation_matrix @ scale_matrix

    def clear(self):
        self.framebuffer = [
            [ self.color_actual for x in range(self.width)]
            for y in range(self.heigth)
        ]
        self.zbuffer = [
            [ -999999 for x in range(self.width)]
            for y in range(self.heigth)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

        #pixel header

        f.write( char('B'))
        f.write( char('M'))
        f.write( dword(14 + 40 + self.width * self.heigth * 3))
        f.write( word(0))
        f.write( word(0))
        f.write( dword(14+40))

        #info header

        f.write( dword(40))
        f.write( dword(self.width))
        f.write( dword(self.heigth))
        f.write( word(1))
        f.write( word(24))
        f.write( dword(0))
        f.write( dword(self.width*self.heigth*3))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))

        # pixel data

        for y in range(self.heigth):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

    def point(self, x, y):
        self.framebuffer[y][x] = self.color_actual

    def point2(self, x, y):
        self.zbuffer[y][x] = self.color_actual

    def set_color(self, color):
        self.color_actual = color

    def line(self, v1, v2):

        y1 = round(v2.y)
        y0 = round(v1.y)
        x1 = round(v2.x)
        x0 = round(v1.x)

        dy,dx= abs(y1 - y0),abs(x1 - x0)

        #Si la pendiente es "mas inclinada" verticalmente
        pendiente = dy > dx
        if pendiente:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        #Y si es inversa
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        #Se calcula nuevamente la pendiente
        dy,dx = abs(y1 - y0),(x1 - x0)

        #Tomando en cuenta que dy implica el desplezamaiento
        limitation = dx
        compensation = 0

        y = y0
        for x in range(x0,1+x1):
            if pendiente:
                self.point(y, x)
            else:
                self.point(x, y)

            compensation += dy * 2

            if compensation >= limitation:
                y += 1 if y0 < y1 else -1
                limitation += dx * 2
