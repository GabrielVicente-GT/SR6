#Gabriel Alejandro Vicente Lorenzo
#SR6 UVG

#Se importan los metodos solicitados por el ejercicios
import gl
import Creando
from vector import *

#Funciones de gl que inicializan un Render con 1024 y 1024
gl.glInit()

gl.glCreateWindow(1024,1024)

gl.glClearColor(0,0,0)
gl.glClear()

#Se renderiza el .bmp para un Medium Shot
renderizado = gl.RenderizadoFuncio()
renderizado.lookAt(V3(0,0,5), V3(0,0,0), V3(0,1,0))

Creando.crear_robusto('./Objts/Pato.obj','./Textrs/Pato.bmp',translate = (0,-0.6,0),scale = (0.025,0.025,0.025),rotate = (-pi/3,0,0))
gl.glFinish('mediumShot.bmp')

#Se cambia el color actual y se limpia el Render
gl.glClearColor(0,0,0)
gl.glClear()

#Se renderiza el .bmp para un Low Angle
Creando.crear_robusto('./Objts/Pato.obj','./Textrs/Pato.bmp',translate = (-0.1,-0.65,0),scale = (0.025,0.025,0.025),rotate = (-pi/1.6,pi/20,0))
gl.glFinish('lowAngle.bmp')

#Se cambia el color actual y se limpia el Render
gl.glClearColor(0,0,0)
gl.glClear()

#Se renderiza el .bmp para un High Angle
Creando.crear_robusto('./Objts/Pato.obj','./Textrs/Pato.bmp',translate = (0,-0.35,0),scale = (0.025,0.025,0.025),rotate = (-pi/8,0,0))
gl.glFinish('highAngle.bmp')

#Se cambia el color actual y se limpia el Render
gl.glClearColor(0,0,0)
gl.glClear()

#Se renderiza el .bmp para un Dutch Angle
Creando.crear_robusto('./Objts/Pato.obj','./Textrs/Pato.bmp',translate = (-0.1,-0.65,0),scale = (0.025,0.025,0.025),rotate = (-pi/3,pi/20,-pi/4))
gl.glFinish('dutchAngle.bmp')
