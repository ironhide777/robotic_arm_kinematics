#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from sympy import symbols
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

theta=math.radians(10)
L = np.array([[0],
     [0],
     [100],
     [1]])
rotation_x = np.array([[1,0,0,0],
              [0,math.cos(theta),-math.sin(theta),0],
              [0,math.sin(theta),math.cos(theta),0],
              [0,0,0,1]])
rotation_y = 
roatation_z = 
rx=rotation_x.dot(L)
print(r)
X=[0,r[0][0]]
Y=[0,r[1][0]]
Z=[0,r[2][0]]
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(X, Y, Z, 'gray')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

#matrix=r*L
#print(matrix)


# In[2]:


#((power(5,-09)*power(2,3))+(power(8,-06)*power(2,2))-(0.0442*2))
4E-19x6 - 3E-15x5 + 4E-12x4 + 1E-08x3 - 1E-05x2 - 0.0346x 
#eq = (5**-9*x**3)+(8**-6*x**2)-(.0442*x)
xvalue=[]
yvalue=[]
arra= np.arange(0,10,.01)
for i in arra:
    x=math.radians(i+.09)
    xvalue.append(x)
    eq = (5**-9*x**3)+(8**-6*x**2)-(.0442*x)
    yvalue.append(eq)
arra= np.arange(0,10,.01)
for i in arra:
    x=math.radians(i+.09)*-1
    xvalue.append(x)
    eq = (5**-9*x**3)+(8**-6*x**2)-(.0442*x)
    yvalue.append(eq)
plt.plot(xvalue,yvalue)


# In[ ]:





# In[3]:



import math as m
import sympy as sym
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
x=sym.Symbol('x')
y=sym.Symbol('y')
z=sym.Symbol('z')

def Co_mat(X,L,Z):
    Co_mat= np.array([[X],[L],[Z],[1]])
    return Co_mat
def R_x(thetax):
    R_x = np.array([[1,0,0,0],
              [0,m.cos(thetax),-m.sin(thetax),0],
              [0,m.sin(thetax),m.cos(thetax),0],
              [0,0,0,1]])
    return R_x
def R_y(thetay):
    R_y = np.array([[m.cos(thetay),0,m.sin(thetay),0],
               [0,1,0,0],
               [-m.sin(thetay),0,m.cos(thetay),0],
               [0,0,0,1]])
    return R_y
def R_z(thetaz):
    R_z = np.array([[m.cos(thetaz),-m.sin(thetaz),0,0],
               [m.sin(thetaz),m.cos(thetaz),0,0],
               [0,0,1,0],
               [0,0,0,1]])
    return R_z

L=555

thetax= 10*.01744
thetay= 20*.01744
rotation_angle=[]
V=0
for i in range(1000):
    
    rotation_angle.append(V)
    V=V+.09
    
thetaz=rotation_angle

xvalues=[]
yvalues=[]
zvalues=[]
print(zvalues)
for ri in range(1000):
    oz=(thetaz[ri])*.01744
    oy=thetay
    ox=thetax
    #frame1
    f1rot1=np.dot(R_x(ox),Co_mat(0,0,100))
    f1rot2=np.dot(R_y(oy),f1rot1)
    f1rot3=np.dot(R_z(0),f1rot2)
    
    #Frame2
    f2rot1=np.dot(R_x(ox),Co_mat(0,555,0))
    f2rot2=np.dot(R_y(oy),f2rot1)
    f2rot3=np.dot(R_z(0),f2rot2)
    rot4=f2rot3+f1rot3
    transform1= np.dot(R_x(0),rot4)
    transform2= np.dot(R_y(0),transform1)
    transform3= np.dot(R_z(oz),transform2)
    xvalues.append(transform3[0][0])
    yvalues.append(transform3[1][0])
    zvalues.append(transform3[2][0])
print('rot',rot4)

X_1=[0,transform3[0][0]]
Y_1=[0,transform3[1][0]]
Z_1=[0,transform3[2][0]]

print (X_1)
X = X_1[1]
print (X)

    #fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #ax.plot3D(X_1, Y_1, Z_1, 'gray')
    #ax.set_xlabel('X axis')
    #ax.set_ylabel('Y axis')
    #ax.set_zlabel('Z axis')

plt.plot(thetaz,zvalues)

plt.plot(thetaz,xvalues)

plt.plot(thetaz,yvalues)
plt.show()
#visual display code - vpython
from vpython import*

#program settings
scene = canvas(title='demonstartion', width=1000, height=1000, center=vector(0,0,0), background=vector(.8,.8,.8))

print(scene.width/2)

canvas_center = points(pos=vector(0,0,0), radius=5, color=color.yellow, opacity = .5)

pointer_XC = arrow(pos=vector(0,0,0),axis=vector(60,0,0),shaftwidth=5,color = color.red)

pointer_YC = arrow(pos=vector(0,0,0),axis=vector(0,60,0),shaftwidth=5,color = color.green)

pointer_ZC = arrow(pos=vector(0,0,0),axis=vector(0,0,60),shaftwidth=5,color = color.black)



#coordinate settings
World_coordinate = points(pos=vector(-1000,-1000,1000), radius=5, color=color.yellow)

pointer_X = arrow(pos=vector(-1000,-1000,1000),axis=vector(100,0,0),shaftwidth=5,color = color.red)

pointer_Y = arrow(pos=vector(-1000,-1000,1000),axis=vector(0,100,0),shaftwidth=5,color = color.green)

pointer_Z = arrow(pos=vector(-1000,-1000,1000),axis=vector(0,0,100),shaftwidth=5,color = color.black)

#environment settings 
limitX=2000
#plane_1=box(pos=vector(0,0,0), size=vector(limitX,1,1000),color=color.blue, opacity = .1)
#plane_2=box(pos=vector(0,0,0), size=vector(1,1000,1000),color=color.blue, opacity = .1)
X_axis_line = box(pos=vector(0,0,0), size=vector(1000,5,5), color=color.black, opacity = .1)
Y_axis_line = box(pos=vector(0,0,0), size=vector(5,1000,0), color=color.black, opacity = .1)
Z_axis_line = box(pos=vector(0,0,0), size=vector(5,5,1000), color=color.black, opacity = .1)
#object setting
def coordinate(pxx,pxy,pxz):
    X_axis_line = box(pos=vector(pxx,pxy,pxz), size=vector(100,1,1), color=color.red, opacity = .9)
    Y_axis_line = box(pos=vector(pxx,pxy,pxz), size=vector(1,100,1), color=color.red, opacity = .9)
    Z_axis_line = box(pos=vector(pxx,pxy,pxz), size=vector(1,1,100), color=color.red, opacity = .9)
    return X_axis_line, Y_axis_line, Z_axis_line
#variables
xaxis_offset = 60
pointer = arrow(pos=vector(0,0,0),axis=vector(f1rot3[0][0],f1rot3[1][0],f1rot3[2][0]), length =100, shaftwidth=10)
coordinate(f1rot3[0][0],f1rot3[1][0],f1rot3[2][0])
pointer = arrow(pos=vector(f1rot3[0][0],f1rot3[1][0],f1rot3[2][0]),axis=vector(f2rot3[0][0],f2rot3[1][0],f2rot3[2][0]),length=550,shaftwidth=10)
coordinate(transform3[0][0],transform3[1][0],transform3[2][0])
#coordinate(rot4[0][0],rot4[1][0],rot4[2][0])


# In[ ]:





# In[ ]:




