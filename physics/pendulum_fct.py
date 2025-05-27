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

def f_double_physic_pendulum(t, angle, g, l1, l2, d1, d2, m1, m2, i1, i2):
        theta1a, theta1b, theta2a, theta2b = angle

        d11 = m1*(d1**2)
        d12 = m2*l1*d2*math.cos(theta1a - theta2a)
        d22 = m2*(d2**2) + i2

        c1 = -m2*l1*d2*math.sin(theta1a - theta2a)*(theta2b**2) - 2*m2*l1*d2*math.sin(theta1a - theta2a)*theta1b*theta2b
        c2 = m2*l1*d2*math.sin(theta1a - theta2a)*(theta1b**2)

        g1 = (m1*d1 + m2*l1)*g*math.sin(theta1a)
        g2 = m2*d2*g*math.sin(theta2a)

        det = (m1*(d1**2) + i1 + m2*(l1**2))*(m2*(d2**2) + i2) - (m2**2)*(l1**2)*(d2**2)*(math.cos(theta1a - theta2a)**2)

        dtheta1adt = theta1b
        dtheta1bdt = (d12*(c2 + g2) - d22*(c1 + g1))/det
        dtheta2adt = theta2b
        dtheta2bdt = (d12*(c1 + g1) - d11*(c2 + g2))/det

        return np.array([dtheta1adt,dtheta1bdt,dtheta2adt,dtheta2bdt])