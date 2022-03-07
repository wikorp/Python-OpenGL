#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

from PIL import Image


viewer = [0.0, 0.0, 10.0]
left_mouse_button_pressed = 0
off = False

theta = 0.0
pix2angle = 1.0

mouse_x_pos_old = 0
delta_x = 0

alpha = 0.0
piy2angle = 1.0

mouse_y_pos_old = 0
delta_y = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

image = None
image2 = None
t1 = 0

def startup():
    global image
    global image2
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_CULL_FACE)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    image = Image.open("tekstura.tga")
    image2 = Image.open("tekstura2.tga")
    #glTexImage2D(
   #     GL_TEXTURE_2D, 0, 3, image.size[0], image.size[1], 0,
   #     GL_RGB, GL_UNSIGNED_BYTE, image.tobytes("raw", "RGB", 0, -1)
   # )


def shutdown():
    pass


def render(time):
    global theta
    global alpha

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)
      
    if left_mouse_button_pressed:
        alpha += delta_y * piy2angle

    glRotatef(alpha, 1.0, 0.0, 0.0)
    
    if t1 == 0:
    	image_tmp = image
    else:
    	image_tmp = image2
    	
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, image_tmp.size[0], image_tmp.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, image_tmp.tobytes("raw", "RGB", 0, -1)
    )

    #glBegin(GL_QUADS)
    #glTexCoord2f(0.0, 0.0)
    #glVertex3f(-5.0, -5.0, 0.0)
    #glTexCoord2f(1.0, 0.0)
    #glVertex3f(5.0, -5.0, 0.0)
    #glTexCoord2f(1.0, 1.0)
    #glVertex3f(5.0, 5.0, 0.0)
    #glTexCoord2f(0.0, 1.0)
    #glVertex3f(-5.0, 5.0, 0.0)
    #glEnd()
    
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    if off == True:
    	glTexCoord2f(0.0, 0.0)
    	glVertex3f(-2.0, -2.0, 2.0)
    	glTexCoord2f(1.0, 0.0)
    	glVertex3f(2.0, -2.0, 2.0)
    	glTexCoord2f(0.5, 1.0)
    	glVertex3f(0.0, 4.0, 0.0)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(0.0, 1.0) #0.5, 1.0
    glVertex3f(0.0, 4.0, 0.0)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0.0, 4.0, 0.0)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0.0, 4.0, 0.0)
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global off
    global t1
    global t2
    
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
        
    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:
        off = not off
    
    if key == GLFW_KEY_1 and action == GLFW_PRESS:
        t1 = 0
    
    if key == GLFW_KEY_2 and action == GLFW_PRESS:
        t1 = 1


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old
    
    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos
    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed
    global right_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0
        
    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
