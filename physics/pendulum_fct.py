import math
import numpy as np

def f_simple_pendulum(t, angle, g, l):
        theta1, theta2 = angle
        dtheta1dt = theta2
        dtheta2dt = -(g/l)*math.sin(theta1)
        return np.array([dtheta1dt,dtheta2dt])

def f_double_pendulum(t, angle, g, l1, l2, m1, m2):
        theta1a, theta1b, theta2a, theta2b = angle

        num1 = -g*(2*m1 + m2)*math.sin(theta1a) - m2*g*math.sin(theta1a - 2*theta2a) - 2*math.sin(theta1a - theta2a)*m2*((theta2b**2)*l2 + (theta1b**2)*l1*math.cos(theta1a - theta2a))
        num2 = 2*math.sin(theta1a - theta2a)*((theta1b**2)*l1*(m1 + m2) + g*(m1 + m2)*math.cos(theta1a) + (theta2b**2)*l2*m2*math.cos(theta1a - theta2a))
        den1 = l1*(2*m1 + m2 - m2*math.cos(2*theta1a - 2*theta2a))
        den2 = l2*(2*m1 + m2 - m2*math.cos(2*theta1a - 2*theta2a))

        dtheta1adt = theta1b
        dtheta1bdt = num1/den1
        dtheta2adt = theta2b
        dtheta2bdt = num2/den2

        return np.array([dtheta1adt,dtheta1bdt,dtheta2adt,dtheta2bdt])