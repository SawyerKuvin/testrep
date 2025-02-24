import numpy as np
import matplotlib.pyplot as plt

#------------------------------------#
#Given Functions#
#Bisection Method
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol
#      num  - number of iterations

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 
    num = 0
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier,num]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier,num]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier,num]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      num = num + 1
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier, num]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier, num]

#Fixed Point Method
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]

#---------------------------------------#
#Homework Problem Functions
#Problem 1
def Problem1():
   a = -1 * np.pi/2
   b = np.pi/2
   tol = 1e-8
   f_x = lambda x: 2*x - 1 - np.sin(x)
   [astar, _, num] = bisection(f_x,a,b,tol)
   print("The final approximation for the root was: ", astar)
   print("The number of iterations used was: ", num)

#Problem 2
def Problem2():
   a = 4.82
   b = 5.2
   tol = 1e-4
   f_a = lambda x: (x-5)**9
   f_b = lambda x: x**9 - 45*x**8 + 900*x**7 - 10500*x**6 + 78750*x**5 - 393750*x**4 + 1312500*x**3 - 2812500*x**2 + 3515625*x - 1953125
   [astar_a, ier_a, num_a] = bisection(f_a,a,b,tol)
   [astar_b, ier_b, num_b] = bisection(f_b,a,b,tol)

   print("The answer from the bisection method for part a: ", astar_a)
   print("The answer from the bisection method for part b: ", astar_b)

#Problem 3
def Problem3():
   a = 1
   b = 4
   tol = 0.5e-3
   f_x = lambda x: x**3 + x - 4
   [astar, ier_a, num] = bisection(f_x,a,b,tol)

   print("The root of this equation is: ", astar)
   print("The number of iterations used was: ", num)

#Problem 5
def Problem5():
   #Part a)
   x = np.linspace(-2.5,7.5,100)
   f_x = x - 4*np.sin(2*x) - 3
   x_line = np.zeros(100)

   plt.figure
   plt.plot(x,f_x)
   plt.plot(x,x_line)
   plt.grid(True)
   plt.title("Figure Showing the Zeros of f(x)")
   plt.xlabel("X Values")
   plt.ylabel("f(x) Values")
   plt.ylim([-4,4])
   plt.show()

   #Part b)
   g_x = lambda x: -np.sin(2*x) + (5*x)/4 - (3/4)
   x0_i = -0.9
   x0_ii = -0.5
   x0_iii = 1.7
   x0_iv = 3.2
   x0_v = 4.5
   x0_vi = 5

   tol = 0.5e-10
   Nmax = 50

   [xstar_i,_] = fixedpt(g_x,x0_i,tol,Nmax)
   print(xstar_i)
   [xstar_ii,_] = fixedpt(g_x,x0_ii,tol,Nmax)
   print(xstar_ii)
   [xstar_iii,_] = fixedpt(g_x,x0_iii,tol,Nmax)
   print(xstar_iii)
   [xstar_iv,_] = fixedpt(g_x,x0_iv,tol,Nmax)
   print(xstar_iv)
   [xstar_v,_] = fixedpt(g_x,x0_v,tol,Nmax)
   print(xstar_v)
   [xstar_vi,_] = fixedpt(g_x,x0_vi,tol,Nmax)
   print(xstar_vi)

#---------------------------------------#
#Calling Homework Problem

#Problem 1
Problem1()

#Problem 2
Problem2()

#Problem 3
Problem3()

#Problem 5
Problem5()

 