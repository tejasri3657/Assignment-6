# -*- coding: utf-8 -*-
"""Assignment-6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-G13qx_oGvl_qJonkwKq5O0WifOD2JK
"""

#Functions related to line
import numpy as np

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

  #Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

#Intersection of two lines
def perp_foot(n,cn,P):
  m = omat@n
  N=np.block([[n],[m]])
  p = np.zeros(2)
  p[0] = cn
  p[1] = m@P
  #Intersection
  x_0=np.linalg.inv(N)@p
  return x_0

#Functions related to triangle
import numpy as np

#Triangle vertices
def tri_vert(a,b,c):
  p = (a**2 + c**2-b**2 )/(2*a)
  q = np.sqrt(c**2-p**2)
  A = np.array([p,q]) 
  B = np.array([0,0]) 
  C = np.array([a,0]) 
  return  A,B,C

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P


#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icircle(A,B,C):
  k1 = 1
  k2 = 1
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r
#Functions related to conics
import numpy as np

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating points on an ellipse
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

  #Generating points on a parabola
def parab_gen(y,a):
	x = y**2/a
	return x

#Generating points on a standard hyperbola 
def hyper_gen(y):
	x = np.sqrt(1+y**2)
	return x

import numpy as np
import matplotlib.pyplot as plt


O = np.array(([0,0]))

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse


#Ellipse parameters
V = np.array(([9,0],[0,6]))
f = 1
u = np.array(([0,0]))

#Standard Ellipse
a = 9
b = 6
x = ellipse_gen(a,b)
c = 6.7

#Vertices
A1 = np.array([a,0])
A2 = -A1
B1 = np.array([0,b])
B2 = -B1

#Plotting points
A = np.array([9,0])
B = np.array([-9,0])
f = np.array([6.7,0])
M = np.array([6.7,4.0])
N = np.array([6.7,-4.0])

#Latus rectum
x_MN = line_gen(M,N)
plt.plot(x_MN[0,:],x_MN[1,:],label='$Latus rectum$')


#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Plotting the standard ellipse
plt.plot(x[0,:],x[1,:])

#Labelling points
plt.plot(9,0,'o',color='r')
plt.text(9 ,0,'A')
plt.plot(0,6, 'o',color='r')
plt.text(0,6,'B')
plt.plot(0,0, 'o',color='r')
plt.text(0,0,'O')
plt.plot(6.7,0,'o',color='r')
plt.text(6.7,0,'F1')
plt.plot(-6.7,0,'o',color='r')
plt.text(-6.7,0,'F2')
plt.plot(6.7,4.0, 'o',color='r')
plt.text(6.5 ,4.2,'M')
plt.plot(6.7,-4.0, 'o',color='r')
plt.text(6.1 ,-4.2,'N')
plt.plot(6.7,0, 'o',color='r')

#Plotting line OF1
O=np.array([0,0])
F1=np.array([c,0])
OF1 = line_gen(O,F1)
plt.plot(OF1[0,:],OF1[1,:],'g',label='Foci')

#Plotting line OF2
O=np.array([0,0])
F2=np.array([-c,0])
OF2 = line_gen(O,F2)
plt.plot(OF2[0,:],OF2[1,:],'g',label='Foci')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()