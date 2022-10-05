#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 0.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.3, 0.6, 0.3)
    fraktal(-100.0, 100.0, 200.0, 200.0, 1)

    glFlush()

def rectangle(x, y, a, b):
	glBegin(GL_TRIANGLES)
	glVertex2f(x - 0.5*a, y + 0.5*b)
	glVertex2f(x - 0.5*a, y - 0.5*b)
	glVertex2f(x + 0.5*a, y - 0.5*b)
	glEnd()
	
	glBegin(GL_TRIANGLES)
	glVertex2f(x - 0.5*a, y + 0.5*b)
	glVertex2f(x + 0.5*a, y + 0.5*b)
	glVertex2f(x + 0.5*a, y - 0.5*b)
	glEnd()	

def fraktal(x, y, a, b, depth):
	if depth > 6:
		rectangle(x, y, a, b)
	else:
		a /= 3
		b /= 3
		fraktal(x, y, a, b, depth + 1)
		fraktal(x + a, y, a, b, depth + 1)
		fraktal(x + 2 * a, y, a, b, depth + 1)
		fraktal(x + 2 * a, y - b, a, b, depth + 1)
		fraktal(x + 2 * a, y - 2 * b, a, b, depth + 1)
		fraktal(x + 1 * a, y - 2 * b, a, b, depth + 1)
		fraktal(x, y - 2 * b, a, b, depth + 1)
		fraktal(x, y - b, a, b, depth + 1)
		
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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

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
