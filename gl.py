#Archivo gl solicitado por SR1

#Importa el archivo proporcionado en clase
import  Render
from vector import *
import random
import extras as ex
from textures import *
from Object import *

def EscrituraSobreTextura(a,b):
        # """
    t = Texture(b)
    r = Render.Render(t.width,t.height)

    r.framebuffer = t.pixels

    # # Cara Clase
    # scale_factor = (500,500,600)
    # translate_factor = (525, 500,0)

    cube = Obj(a)

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
        if len(face) == 4:
            f1 = face[0][1] - 1
            f2 = face[1][1] - 1
            f4 = face[3][1] - 1
            f3 = face[2][1] - 1

            vt1 = V3(cube.tvertices[f1][0]*t.width,cube.tvertices[f1][1]*t.height)
            vt2 = V3(cube.tvertices[f2][0]*t.width,cube.tvertices[f2][1]*t.height)
            vt3 = V3(cube.tvertices[f3][0]*t.width,cube.tvertices[f3][1]*t.height)
            vt4 = V3(cube.tvertices[f4][0]*t.width,cube.tvertices[f4][1]*t.height)

            # print(round(vt1.x),round(vt1.y))
            # print(round(vt2.x),round(vt2.y))
            # print(round(vt3.x),round(vt3.y))
            # print(vt1,vt2,vt3)
            # r.line(vt1.x,vt1.y,vt2.x,vt2.y)
            # r.line(vt2.x,vt2.y,vt3.x,vt3.y)
            # r.line(vt3.x,vt3.y,vt1.x,vt1.y)
            try:
                r.line(vt1,vt2)
                r.line(vt2,vt3)
                r.line(vt3,vt4)
                r.line(vt4,vt1)
            except:
                pass
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

#Le asigna al renderizado global un render sencillo
def RenderizadoFuncio():
    global renderizado
    return renderizado

def glInit():
    global renderizado
    renderizado = Render.Render(1,1)

#Crea la ventana con el ancho y la altura que el usuario desea
def glCreateWindow(width, height):
    global renderizado
    global widthFrame
    global heightFrame

    #Si el ancho y alto cumplen con la condicion de que sean valores
    #modulos de 4 se crea el render, de otrao forma, se adaptan para que sean
    #modulos de 4

    if width % 4 == 0 and height % 4 == 0:
        renderizado       = Render.Render(width,height)
    else:
        width   = width+width%4
        height  = height+height%4
        renderizado       = Render.Render(width,height)

    widthFrame  = width
    heightFrame = height

#Se crea la ventana donde se trabajara el punto
def glViewPort(x, y, width, height):
    global renderizado
    renderizado.set_color(Render.color(round(255*0), round(255*0), round(255*0)))

    #posicion desde la que se crea el view port
    #Se crea desde la esquina inferior izquierda
    global xPositionVP
    global yPositionVP

    #altura y ancho de viewport
    global widthVP
    global heightVP

    #si sobrepasan la altura y ancho de la ventana total se hace una reasignacion
    if  x > widthFrame or x < 0:
        x = widthFrame
    elif y > heightFrame or y < 0:
        y = heightFrame

    #posicion de inicio para el viewport
    xPositionVP = x
    yPositionVP = y


    #si sobrepasa la suma de la altura con la posicion el alto y ancho
    #respectivo, se hace una reasignacion
    if (xPositionVP + width) > widthFrame:
        width = widthFrame - xPositionVP
    if (yPositionVP + height) > heightFrame:
        height = heightFrame - yPositionVP

    widthVP     = width
    heightVP    = height

    #se renderiza el viewport
    for w in range (xPositionVP, xPositionVP + widthVP):
        for z in range (yPositionVP, yPositionVP + heightVP):
            renderizado.point(w, z)

#Se pinta todo el tablero de pixeles con el color predeterminado
def glClear():
    global renderizado
    renderizado.clear()

#Se cambia el color predeterminado
def glClearColor(r, g, b):
    global renderizado
    renderizado.set_color(Render.color(round(255*r), round(255*g), round(255*b)))

#Se dibuja un punto en las cordenadas especificas (respetando el viewport)
def glVertex(x, y):
    global puntomedidoX
    global puntomedidoY

    if y > 0:
        puntomedidoY = yPositionVP + round(heightVP/2) + round((heightVP/2)*y)
    elif y < 0:
        puntomedidoY = yPositionVP + round(heightVP/2) - round((heightVP/2)*(-y))
    elif y == 0:
        puntomedidoY = yPositionVP + round(heightVP/2)

    if x > 0:
        puntomedidoX = xPositionVP + round(widthVP/2) + round((widthVP/2)*(x))
    elif x < 0:
        puntomedidoX = xPositionVP + round(widthVP/2) - round((widthVP/2)*(-x))
    elif x == 0:
        puntomedidoX = xPositionVP + round(widthVP/2)

    # for xx in range(10):
    #     for yy in range (10):
    # # print(puntomedidoX,puntomedidoY)
    #         renderizado.point(923+xx,100+yy)
    if puntomedidoY == (yPositionVP +heightVP):

        puntomedidoY = puntomedidoY -1

    if puntomedidoX == (xPositionVP +widthVP):

        puntomedidoX = puntomedidoX -1
    renderizado.point(puntomedidoX,puntomedidoY)

#Se cambia el color con el que se dibuja el punto
def glColor(r, g, b):
    global renderizado
    renderizado.set_color(Render.color(round(255*r), round(255*g), round(255*b)))

#Se escribe el archivo
def glFinish(nombre):
    global renderizado
    renderizado.write(nombre)

def escala(unitario, tipo):
    #Valores para operar
    devolucion = 1
    a = 0
    b = 0

    #Dependiendo si se calcula un punto respecto a la altura o el ancho
    if tipo == "W":
        a = widthVP
        b = xPositionVP
    elif tipo == "H":
        a = heightVP
        b = yPositionVP

    #El caso dependiendo si esta en el centro del eje, a la izquierda o a la derecha
    if unitario > 0:
        devolucion = b + round(a/2) + round((a/2)*(unitario))
    elif unitario < 0:
        devolucion = b + round(a/2) - round((a/2)*(-unitario))
    elif unitario == 0:
        devolucion = b + round(a/2)

    #Si el valor calculado es igual al limite se le resta un pixel para que quede dentro del viewport
    if devolucion == (a + b):
        devolucion = devolucion -1

    return devolucion

def glLine(x0,y0,x1,y1):
    global renderizado
    #Se cambia el color para tener contraste
    renderizado.set_color(Render.color(round(255*1), round(255*1), round(255*1)))

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = escala(x0,"W")
    y0 = escala(y0,"H")
    x1 = escala(x1,"W")
    y1 = escala(y1,"H")

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
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
    dy,dx = abs(y1 - y0),abs(x1 - x0)

    #Tomando en cuenta que dy implica el desplezamaiento
    limitation = dx
    compensation = 0

    y = y0
    for x in range(x0,1+x1):
        if pendiente:
            renderizado.point(y, x)
        else:
            renderizado.point(x, y)

        compensation += dy * 2

        if compensation >= limitation:
            y += 1 if y0 < y1 else -1
            limitation += dx * 2

def glLine3(x0,y0,x1,y1):
    global renderizado
    #Se cambia el color para tener contraste
    renderizado.set_color(Render.color(round(255*0), round(255*0.62), round(255*0.1)))

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = round(x0)
    y0 = round(y0)
    x1 = round(x1)
    y1 = round(y1)

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
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
            renderizado.point(y, x)
        else:
            renderizado.point(x, y)

        compensation += dy * 2

        if compensation >= limitation:
            y += 1 if y0 < y1 else -1
            limitation += dx * 2

def glLine2(v1,v2):
    global renderizado
    #Se cambia el color para tener contraste

    #Se realiza la conversión utilizando la funcion escala para convertir valores entre -1 y 1
    #A valores en pixeles

    x0 = round(v1.x)
    y0 = round(v1.y)
    x1 = round(v2.x)
    y1 = round(v2.y)

    #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
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
            renderizado.point(y, x)
        else:
            renderizado.point(x, y)

        compensation += dy * 2

        if compensation >= limitation:
            y += 1 if y0 < y1 else -1
            limitation += dx * 2

def triangulo_version_dos(vertices):
    global renderizado
    A,B,C = vertices
    # colorA = (255,0,0)
    # colorB = (0,255,0)
    # colorC = (0,0,255)

    luz = V3(0,0,-1)
    normal_triangulo =  (C-A) * (B-A)
    # # print("A> ",A)
    # # print("B> ",B)
    # # print("C> ",C)
    # # print("C-A> ",(C-A))
    # # print("B-A> ",(B-A))
    # # print("all> ",(C-A) * (B-A))
    i = luz.normalize() @ normal_triangulo.normalize()
    # print(i)
    # # print(normal_triangulo.normalize().x,normal_triangulo.normalize().y,normal_triangulo.normalize().z)
    if i < 0:
        return

    gris = 255*i
    renderizado.set_color(Render.color(round(gris),round(gris) ,round(gris)))

    Bmin, Bmax = ex.bounding_box(A,B,C)
    Bmin.round()
    Bmax.round()

    for x in range(Bmin.x, Bmax.x+1):
        for y in range(Bmin.y, Bmax.y+1):
            w,v,u = ex.barycentric(A,B,C,V3(x,y))
            if(w < 0 or v < 0 or u<0):
                continue

            # renderizado.set_color(Render.color(round(colorA[0] * w) + round(colorB[0] * v +colorC[0] * u),round(colorA[1] * w) + round(colorB[1] * v +colorC[1] * u),round(colorA[2] * w) + round(colorB[2] * v +colorC[2] * u)))

            z = A.z * w + B.z * v + C.z*u
            try:
                if renderizado.zbuffer[x][y] < z:
                    renderizado.zbuffer[x][y] = z
                    # print("triangulodibujado2")
                    renderizado.point(x,y)
            except:
                renderizado.point(x,y)

def triangulo_version_dos_textura(verices,vertices_de_textura = ()):
    global renderizado

    A,B,C = verices

    if renderizado.texture:
        tA,tB,tC = vertices_de_textura

    # colorA = (255,0,0)
    # colorB = (0,255,0)
    # colorC = (0,0,255)

    luz = V3(0,0,-1)
    normal_triangulo =  (C-A) * (B-A)
    # # print("A> ",A)
    # # print("B> ",B)
    # # print("C> ",C)
    # # print("C-A> ",(C-A))
    # # print("B-A> ",(B-A))
    # # print("all> ",(C-A) * (B-A))
    i = luz.normalize() @ normal_triangulo.normalize()
    # print(i)
    # # print(normal_triangulo.normalize().x,normal_triangulo.normalize().y,normal_triangulo.normalize().z)
    if i < 0:
        return

    rojo    = 250*i
    verde   = 250*i
    azul    = 250*i
    renderizado.set_color(Render.color(round(rojo),round(verde) ,round(azul)))

    Bmin, Bmax = ex.bounding_box(A,B,C)
    Bmin.round()
    Bmax.round()

    for x in range(Bmin.x, Bmax.x+1):
        for y in range(Bmin.y, Bmax.y+1):
            w,v,u = ex.barycentric(A,B,C,V3(x,y))
            if(w < 0 or v < 0 or u<0):
                continue

            # renderizado.set_color(Render.color(round(colorA[0] * w) + round(colorB[0] * v +colorC[0] * u),round(colorA[1] * w) + round(colorB[1] * v +colorC[1] * u),round(colorA[2] * w) + round(colorB[2] * v +colorC[2] * u)))

            z = A.z * w + B.z * v + C.z*u

            # print(tx," ",ty)


            # print("triangulodibujado")
            if x > 0 and y > 0 and x<len(renderizado.zbuffer) and y<len(renderizado.zbuffer[0]) and renderizado.zbuffer[x][y] < z:
                renderizado.zbuffer[x][y] = z

                if renderizado.texture:
                    tx = tA.x * w + tB.x * u + tC.x *v
                    ty = tA.y * w + tB.y * u + tC.y *v
                    renderizado.set_color(renderizado.texture.GetColorIntensity(tx,ty,i))
                    # print(tx," ",ty)


                renderizado.point(x,y)

def zbuffer():
    print(renderizado.zbuffer[0])

def relleno(posicionequis,posicionye,color):
    global renderizado
    pila = [[posicionequis,posicionye]]
    currentc = Render.color(round(255*0), round(255*0), round(255*0))

    if color == 1:
        renderizado.set_color(Render.color(round(255*0.96), round(255*0.82), round(255*0.25)))
    elif color ==2:
        renderizado.set_color(Render.color(round(255*1), round(255*0), round(255*0)))
    elif color == 3:
        renderizado.set_color(Render.color(round(255*0), round(255*1), round(255*0)))
    elif color == 4:
        renderizado.set_color(Render.color(round(255*0), round(255*0), round(255*1)))
    elif color == 5:
        renderizado.set_color(Render.color(round(255*0.5), round(255*0.5), round(255*0.5)))

    while len(pila) != 0:
        posicionancho, posicionlargo = pila[-1][0],pila[-1][1]
        pila.pop()

        if renderizado.framebuffer[posicionlargo][posicionancho] == currentc:
            renderizado.point(posicionancho,posicionlargo)
            nuevos = [[posicionancho + 1, posicionlargo],[posicionancho - 1, posicionlargo],[posicionancho, posicionlargo + 1],[posicionancho, posicionlargo - 1]]
            pila.append(nuevos[0])
            pila.append(nuevos[1])
            pila.append(nuevos[2])
            pila.append(nuevos[3])

def TrazosFiguras():
    poligono1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360) ,(250, 380), (220, 385), (205, 410), (193, 383)]

    prev_point = poligono1[-1]
    for point in poligono1:
        glLine2(V3(*prev_point),V3(*point))
        prev_point = point

    poligono2 = [(321, 335), (288, 286), (339, 251), (374, 302)]

    prev_point = poligono2[-1]
    for point in poligono2:
        glLine2(V3(*prev_point),V3(*point))
        prev_point = point

    poligono3 = [(377, 249), (411, 197), (436, 249)]

    prev_point = poligono3[-1]
    for point in poligono3:
        glLine2(V3(*prev_point),V3(*point))
        prev_point = point

    poligono4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),(597, 215), (552, 214), (517, 144), (466, 180)]

    prev_point = poligono4[-1]
    for point in poligono4:
        glLine2(V3(*prev_point),V3(*point))
        prev_point = point

    poligono5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

    prev_point = poligono5[-1]
    for point in poligono5:
        glLine2(V3(*prev_point),V3(*point))
        prev_point = point

def Laboratorio1():
    relleno(700,150,5)
    relleno(600,150,4)
    relleno(400,225,3)
    relleno(330,300,2)
    relleno(210,380,1)