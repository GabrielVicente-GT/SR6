from Object import *
import gl
from vector import *
from textures import *
import MatricesSimuladas as MatrizSimulada

def transform_vertex_robusto(vertex):
    renderizado = gl.RenderizadoFuncio()
    # augmented_vertex = [c
    #     vertex[0],
    #     vertex[1],
    #     vertex[2],
    #     1
    # ]
    augmented_vertex = MatrizSimulada.matrix([[vertex[0]],[vertex[1]],[vertex[2]],[1]])
    transformed_vertex = renderizado.ViewPort @ renderizado.Projection @renderizado.View @ renderizado.Model @ augmented_vertex
    divisor = transformed_vertex.obtener_valor_unico(3,0)
    return V3(
        transformed_vertex.obtener_valor_unico(0,0)/divisor,
        transformed_vertex.obtener_valor_unico(1,0)/divisor,
        transformed_vertex.obtener_valor_unico(2,0)/divisor,

    )

def crear_robusto(Objeto, Textura,translate, scale, rotate):

    renderizado = gl.RenderizadoFuncio()
    renderizado.loadModelMatrix(translate,scale,rotate)
    cube = Obj(Objeto)
    renderizado.texture = Texture(Textura)

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex_robusto(cube.vertices[f1])
        v2 = transform_vertex_robusto(cube.vertices[f2])
        v3 = transform_vertex_robusto(cube.vertices[f3])

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex_robusto(cube.vertices[f4])

            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1
                ft4 = face[3][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                vt4 = V3(*cube.tvertices[ft3])

                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))
                gl.triangulo_version_dos_textura((v1,v3,v4),(vt1,vt3,vt3))
            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))
                gl.triangulo_version_dos_textura((v1,v3,v4))

        elif len(face) == 3:
            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))

            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))

