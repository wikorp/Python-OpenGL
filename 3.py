#!/usr/bin/env python3
import sys
import math
import numpy
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

arr = numpy.zeros((100, 100, 3))

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    egg_prepare()


def shutdown():
    pass

def egg_prepare():
    u = 0
    v = 0
    u_i = 0
    v_i = 0
    for i in range(100):
        for j in range(100):
            x = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2 - 45*u) * math.cos(math.pi * v)
            y = 160*u**4 - 320*u**3 + 160*u**2 - 5
            z = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2 - 45*u) * math.sin(math.pi * v)
            
            arr[u_i][v_i][0] = x
            arr[u_i][v_i][1] = y 
            arr[u_i][v_i][2] = z
            
            v_i += 1
            v += 0.01
            
        u_i += 1
        u += 0.01

        v_i = 0 
        v = 0
    
def egg30():
    glBegin(GL_POINTS)
       
    for i in range(100):
        for j in range(100):
            glVertex3f(arr[i][j][0],arr[i][j][1],arr[i][j][2])

    glEnd()

def egg35():
    glBegin(GL_LINES)

    for i in range(100):
        for j in range(100):
            if (j < 99):
                glVertex3f(arr[i][j][0],arr[i][j][1],arr[i][j][2])
                glVertex3f(arr[i][j+1][0],arr[i][j+1][1],arr[i][j+1][2])
            else:
                glVertex3f(arr[i][99][0],arr[i][99][1],arr[i][99][2])
                glVertex3f(arr[i][0][0],arr[i][0][1],arr[i][0][2])
    
    for j in range(100):
        for i in range(100):
            if (i < 99):
                glVertex3f(arr[i][j][0],arr[i][j][1],arr[i][j][2])
                glVertex3f(arr[i+1][j][0],arr[i+1][j][1],arr[i+1][j][2])
            else:
                glVertex3f(arr[99][j][0],arr[99][j][1],arr[99][j][2])
                glVertex3f(arr[0][j][0],arr[0][j][1],arr[0][j][2])
    
    glEnd()

    
def egg40():
    glBegin(GL_TRIANGLES)

    for i in range(100):
        for j in range(100):

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99):
                glVertex3f(arr[i][j][0],arr[i][j][1],arr[i][j][2])
                glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                glVertex3f(arr[i][j+1][0],arr[i][j+1][1],arr[i][j+1][2])
            else:
                glVertex3f(arr[i][99][0],arr[i][99][1],arr[i][99][2])
                glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                glVertex3f(arr[i][0][0],arr[i][0][1],arr[i][0][2])
            
            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (i < 99):
                glVertex3f(arr[i+1][j][0],arr[i+1][j][1],arr[i+1][j][2])
            else:
                glVertex3f(arr[0][j][0],arr[0][j][1],arr[0][j][2])


            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (i < 99):
                glVertex3f(arr[i+1][j][0],arr[i+1][j][1],arr[i+1][j][2])
            else:
                glVertex3f(arr[0][j][0],arr[0][j][1],arr[0][j][2])

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99):
                glVertex3f(arr[i][j+1][0],arr[i][j+1][1],arr[i][j+1][2])
            else:
                glVertex3f(arr[i][0][0],arr[i][0][1],arr[i][0][2])

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99 and i < 99):
                glVertex3f(arr[i+1][j+1][0],arr[i+1][j+1][1],arr[i+1][j+1][2])
            elif (j < 99 and i == 99):
                glVertex3f(arr[0][j+1][0],arr[0][j+1][1],arr[0][j+1][2])
            elif (j == 99 and i < 99):
                glVertex3f(arr[i+1][0][0],arr[i+1][0][1],arr[i+1][0][2])
            elif (j == 99 and i == 99):
                glVertex3f(arr[0][0][0],arr[0][0][1],arr[0][0][2])

    glEnd()

def egg45():
    glBegin(GL_TRIANGLE_STRIP)

    for i in range(100):
        for j in range(100):

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99):
                glVertex3f(arr[i][j][0],arr[i][j][1],arr[i][j][2])
                glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                glVertex3f(arr[i][j+1][0],arr[i][j+1][1],arr[i][j+1][2])
            else:
                glVertex3f(arr[i][99][0],arr[i][99][1],arr[i][99][2])
                glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                glVertex3f(arr[i][0][0],arr[i][0][1],arr[i][0][2])
            
            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (i < 99):
                glVertex3f(arr[i+1][j][0],arr[i+1][j][1],arr[i+1][j][2])
            else:
                glVertex3f(arr[0][j][0],arr[0][j][1],arr[0][j][2])


            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (i < 99):
                glVertex3f(arr[i+1][j][0],arr[i+1][j][1],arr[i+1][j][2])
            else:
                glVertex3f(arr[0][j][0],arr[0][j][1],arr[0][j][2])

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99):
                glVertex3f(arr[i][j+1][0],arr[i][j+1][1],arr[i][j+1][2])
            else:
                glVertex3f(arr[i][0][0],arr[i][0][1],arr[i][0][2])

            glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            if (j < 99 and i < 99):
                glVertex3f(arr[i+1][j+1][0],arr[i+1][j+1][1],arr[i+1][j+1][2])
            elif (j < 99 and i == 99):
                glVertex3f(arr[0][j+1][0],arr[0][j+1][1],arr[0][j+1][2])
            elif (j == 99 and i < 99):
                glVertex3f(arr[i+1][0][0],arr[i+1][0][1],arr[i+1][0][2])
            elif (j == 99 and i == 99):
                glVertex3f(arr[0][0][0],arr[0][0][1],arr[0][0][2])

    glEnd()


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)

    axes()
    #egg30()
    #egg35()
    #egg40()
    egg45()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
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
