import math
import numpy as np

def f_simple_pendulum(t, angle, g, l):
        theta1, theta2 = angle
        dtheta1dt = theta2
        dtheta2dt = -(g/l)*math.sin(theta1)
        return np.array([dtheta1dt,dtheta2dt])

def f_simple_physic_pendulum(t, angle, g, l, d, m, i):
        theta1, theta2 = angle
        dtheta1dt = theta2
        dtheta2dt = (-m*g*d*math.sin(theta1))/(i + m*(d**2))
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

def f_double_physic_pendulum(t, angle, g, l1, l2, d1, d2, m1, m2, i1, i2):
        theta1a, theta1b, theta2a, theta2b = angle

        i1m = i1 - m1*(d1**2) # moment of inertia around the center of mass
        i2m = i2 - m2*(d2**2)

        num1 = -(2*g*m1*d1*(i2m + m2*(d2**2))*math.sin(theta1a) + l1*m2*(g*(2*i2m + m2*(d2**2))*math.sin(theta1a) + d2*(g*m2*d2*math.sin(theta1a - 2*theta2a) + 2*((theta2b**2)*(i2m + m2*(d2**2)) + (theta1b**2)*l1*m2*d2*math.cos(theta1a - theta2a))*math.sin(theta1a - theta2a))))
        num2 = m2*d2*(-(g*(2*i1m + (l1**2)*m2 + 2*m1*(d1**2))*math.sin(theta2a)) + l1*(g*m1*d1*math.sin(theta2a) + 2*(theta1b**2)*(i1m + (l1**2)*m2 + m1*(d1**2))*math.sin(theta1a - theta2a) + (theta2b**2)*l1*m2*d2*math.sin(2*(theta1a - theta2a)) + g*m1*d1*math.sin(2*theta1a - theta2a) + g*l1*m2*math.sin(2*theta1a - theta2a)))
        den = 2*i1m*(l1**2)*m2 + 2*i2m*m1*(d1**2) + (l1**2)*(m2**2)*(d2**2) + 2*m1*m2*(d1**2)*(d2**2) + 2*i1m*(i2m + m2*(d2**2)) - (l1**2)*(m2**2)*(d2**2)*math.cos(2*(theta1a - theta2a))

        dtheta1adt = theta1b
        dtheta1bdt = num1/den
        dtheta2adt = theta2b
        dtheta2bdt = num2/den

        return np.array([dtheta1adt,dtheta1bdt,dtheta2adt,dtheta2bdt])