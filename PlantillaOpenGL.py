from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPasto():
    glColor3f(0.16470588235294117647058823529412,0.61568627450980392156862745098039,0.56078431372549019607843137254902)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.8,0.0)
    glVertex3f(1.0,-0.8,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarCirculo():
    glColor3f(0.91372549019607843137254901960784,0.76862745098039215686274509803922,0.41568627450980392156862745098039)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + 0.6 ,0.0)
    glEnd()

def dibujarRayos():
    glColor3f(0.91372549019607843137254901960784,0.76862745098039215686274509803922,0.41568627450980392156862745098039)
    glBegin(GL_LINES)
    glVertex2f(-0.35,0.6)
    glVertex2f(-0.32,0.6)
    glVertex2f(-0.6,0.38)
    glVertex2f(-0.6,0.35)
    
    glVertex2f(-0.85,0.6)
    glVertex2f(-0.82,0.6)
    glVertex2f(-0.6,0.85)
    glVertex2f(-0.6,0.83)

    glVertex2f(-0.85,0.38)
    glVertex2f(-0.32,0.85)
    
    glVertex2f(-0.32,0.38)
    glVertex2f(-0.85,0.85)
    glEnd()

def dibujarLuna():
    glColor3f(0.2,0.2,0.2)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.185 - 0.6 , sin(angulo) * 0.181 + 0.58 ,0.0)
    glEnd()

def dibujarCuadro():
    glColor3f(0.8,0.8,0.8)
    glBegin(GL_QUADS)
    glVertex3f(-0.2,-0.8,0.0)
    glVertex3f(0.8,-0.8,0.0)
    glVertex3f(0.8,0,0.0)
    glVertex3f(-0.2,0,0.0)
    glEnd()

def dibujarVentana():
    glColor3f(0.03529411764705882352941176470588, 0.31764705882352941176470588235294, 0.35686274509803921568627450980392)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.55,0.0)
    glVertex3f(0.3,-0.55,0.0)
    glVertex3f(0.3,-0.3,0.0)
    glVertex3f(-0.1,-0.3,0.0)
    glEnd()

def dibujarTriangulo():
    glColor3f(0.95686274509803921568627450980392,0.63529411764705882352941176470588,0.38039215686274509803921568627451)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.4,0,0.0)
    glVertex3f(0.3,0.4,0.0)
    glVertex3f(1,0,0.0)
    glEnd()

def dibujarPuerta():
    glColor(0.8,0.5,0)
    glBegin(GL_QUADS)
    glVertex3f(0.4,-0.8,0.0)
    glVertex3f(0.6,-0.8,0.0)
    glVertex3f(0.6,-0.4,0.0)
    glVertex3f(0.4,-0.4,0.0)
    glEnd()

def dibujarManija():
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.55 , sin(angulo) * 0.02 - 0.6 ,0.0)
    glEnd()

def dibujarTronco():
    glColor(0.90588235294117647058823529411765,0.43529411764705882352941176470588,0.31764705882352941176470588235294)
    glBegin(GL_QUADS)
    glVertex3f(-0.8,-0.8,0.0)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.6,-0.5,0.0)
    glVertex3f(-0.8,-0.5,0.0)
    glEnd()

def dibujarHojas1():
    glColor3f(0.16470588235294117647058823529412,0.61568627450980392156862745098039,0.56078431372549019607843137254902)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.7 , sin(angulo) * 0.2 + -0.4 ,0.0)
    glEnd()

def dibujarHojas2():
    glColor3f(0.16470588235294117647058823529412,0.61568627450980392156862745098039,0.56078431372549019607843137254902)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.7 , sin(angulo) * 0.2 + -0.2 ,0.0)
    glEnd()

def dibujarHojas3():
    glColor3f(0.16470588235294117647058823529412,0.61568627450980392156862745098039,0.56078431372549019607843137254902)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.8 , sin(angulo) * 0.2 + -0.3 ,0.0)
    glEnd()

def dibujarHojas4():
    glColor3f(0.16470588235294117647058823529412,0.61568627450980392156862745098039,0.56078431372549019607843137254902)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + -0.3 ,0.0)
    glEnd()

def dibujarNube1():
    glColor3f(0.4,0.4,0.4)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.6 , sin(angulo) * 0.1 + 0.8 ,0.0)
    glEnd()

def dibujarNube2():
    glColor3f(0.4,0.4,0.4)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.3 , sin(angulo) * 0.1 + 0.6 ,0.0)
    glEnd()

def dibujarNube3():
    glColor3f(0.4,0.4,0.4)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.1 , sin(angulo) * 0.1 + 0.7 ,0.0)
    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarRayos()
    dibujarCirculo()
    dibujarLuna()
    dibujarCuadro()
    dibujarVentana()
    dibujarTriangulo()
    dibujarPuerta()
    dibujarTronco()
    dibujarHojas1()
    dibujarHojas2()
    dibujarHojas3()
    dibujarHojas4()
    dibujarManija()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(600,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece region de dibujo
        glViewport(0,0,600,600)
        #Establece color de borrado
        glClearColor(0.14901960784313725490196078431373,0.27450980392156862745098039215686,0.32549019607843137254901960784314,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()