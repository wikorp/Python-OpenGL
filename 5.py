#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 5.0, 10.0]
right_mouse_button_pressed = 0
left_mouse_button_pressed = 0
R = 10.0

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

light2_ambient = [0.1, 0.1, 0.0, 1.0]
light2_diffuse = [0.8, 0.8, 0.0, 1.0]
light2_specular = [0.5, 0.5, 0.5, 0.5]
light2_position = [-20.0, 15.0, 5.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

before_next = 0
next_parametr = 0
increse = 0
decrese = 0
parametr_iterator = 0


def startup():
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
    
    glLightfv(GL_LIGHT1, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light2_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light2_position)
    
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)


def shutdown():
    pass


def render(time):
    global theta
    global alpha
    global R
    global parametr_iterator
    global next_parametr
    global before_next

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    #object
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)
    
    #color of light parametr selection and modification
    if next_parametr == 1 and before_next == 0:
    	parametr_iterator += 1
    before_next = next_parametr
    
    if parametr_iterator > 3:
    	parametr_iterator = 0
    
    if increse == 1:
    	light2_specular[parametr_iterator] += 0.1
    
    if decrese == 1:
    	light2_specular[parametr_iterator] -= 0.1
    
    light2_specular[parametr_iterator] = min(light2_specular[parametr_iterator], 1.0)
    light2_specular[parametr_iterator] = max(light2_specular[parametr_iterator], 0.0)
   
    glLightfv(GL_LIGHT1, GL_SPECULAR, light2_specular)
    
    #print in console
    #print (parametr_iterator)
    
    #light rotation
    if left_mouse_button_pressed:
       theta += delta_x * pix2angle
      
    if left_mouse_button_pressed:
        alpha += delta_y * piy2angle
        #alpha = min(alpha, 89.0)
        #alpha = max(alpha, -89.0)

    if right_mouse_button_pressed:
    	if delta_y > 0:
    		R += 0.1
    		
    	if delta_y < 0:
    		R -= 0.1
    
    alpha_r = (alpha * math.pi / 180) % (2 * math.pi)
    theta_r = (theta * math.pi / 180) % (2 * math.pi)
    print (alpha)
    print (theta)
   
    x = 5 * math.cos(theta_r) * math.cos(alpha_r)
    y = 5 * math.sin(alpha_r) 
    z = 5 * math.sin(theta_r) * math.cos(alpha_r)
    
    light2_position[0] = x
    light2_position[1] = y
    light2_position[2] = z
    
  #  glTranslate(x, y, z)
    
    glLightfv(GL_LIGHT1, GL_POSITION, light2_position)
    
    #light
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    glTranslatef(x,y,z);
    gluSphere(quadric, 0.5, 6, 5)
    gluDeleteQuadric(quadric)
    
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
    global before_next
    global next_parametr
    global increse
    global decrese
    
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
     
    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:
        next_parametr = 1
    else:
        next_parametr = 0
         
    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        increse = 1
    else:
        increse = 0
    
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        decrese = 1
    else:
        decrese = 0


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
