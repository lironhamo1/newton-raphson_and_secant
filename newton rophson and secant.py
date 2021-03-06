from sympy import *
import math

def deriv(f,x):
    my_f1 = diff(f,x)
    return lambdify(x, my_f1)

def newton(f,a,b, eps):
    x0=(b+a)/2
    fx=f
    x1=a
    x= symbols('x')
    f=lambdify(x,f)
    fd=deriv(fx,x)
    count=0
    while (abs(x1-x0)>eps):
        tmp=x1
        if fd(x0)==0:
            print("cant divided by zero")
            return
        x1=x0-(f(x0)/fd(x0))
        count+=1
        x0=tmp
        if (count>=50):
            return None
    print("Newton-Raphson num of iter", count)
    return x1

def secant(f,a,b, eps):
    x2 = (a+b)/2
    x1=b
    x0=a
    x = symbols('x')
    f = lambdify(x, f,"math")
    count=0
    while (abs(x2 - x1) > eps):
        tmp=x2
        x2=(x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0=x1
        x1=tmp
        count+=1
        if (count>=50):
            return None
    print("secant num of iter",count)
    return x2
"""
Cutting the section (a,b) into smaller sections
And if there is a sign change we will send it to secant and newton"""
def func_2(f, start_point , end_point, num_of_split):
    length=(end_point-start_point)/num_of_split
    x = symbols('x')
    fx = lambdify(x, f,"math")
    x=start_point
    while(x<end_point):
        if fx(x)* fx(x+length)<=0:
            c=secant(f,x,x+length,10**-10)
            if (c != None):
                print("Secant :The value of root is : ", "%.4f" % c)
            c=newton(f,x,x+length,10**-10)
            if (c != None):
                print("Newton :The value of root is : ", "%.4f" % c)
        x=x+length

x = var('x')  # the possible variable names must be known beforehand...
user_input = input("Enter function\n")
f= sympify(user_input)
a=float(input("Enter start point\n"))
b=float(input("Enter end point\n"))
func_2(f,a,b,100)