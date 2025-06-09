import math
import numpy as np

def f_simple_pendulum(t, angle, g, l, m, friction):
        theta1, theta2 = angle

        dtheta1dt = theta2
        dtheta2dt = -(g/l)*math.sin(theta1) - (friction/(m*(l**2)))*theta2

        return np.array([dtheta1dt,dtheta2dt])

def f_simple_physic_pendulum(t, angle, g, l, d, m, i, friction):
        theta1, theta2 = angle

        dtheta1dt = theta2
        dtheta2dt = (-m*g*d*math.sin(theta1) - friction*theta2)/(i + m*(d**2))

        return np.array([dtheta1dt,dtheta2dt])

def f_double_pendulum(t, angle, g, l1, l2, m1, m2, f1, f2):
        theta1a, theta1b, theta2a, theta2b = angle

        num1 = -m2*(theta1b**2)*math.sin(2*(theta1a - theta2a))
        num2 = m2*g*math.cos(theta1a - theta2a)*math.sin(theta2a)
        num3 = f2*math.cos(theta1a - theta2a)*theta2b
        num4 = -m2*l2*(theta2b**2)*math.sin(theta1a - theta2a)
        num5 = -(m1 + m2)*g*math.sin(theta1a)
        num6 = -f1*theta1b
        den = m1 + m2 - m2*(math.cos(theta1a - theta2a)**2)

        dtheta1adt = theta1b
        dtheta1bdt = num1/(2*den) + num2/(l1*den) + num3/(l1*l2*den) + num4/(l1*den) + num5/(l1*den) + num6/((l1**2)*den)
        dtheta2adt = theta2b
        dtheta2bdt = -(l1/l2)*math.cos(theta1a - theta2a)*dtheta1bdt + (l1/l2)*(theta1b**2)*math.sin(theta1a - theta2a) - (g/l2)*math.sin(theta2a) - (f2/(m2*(l2**2)))*theta2b

        return np.array([dtheta1adt,dtheta1bdt,dtheta2adt,dtheta2bdt])

def f_double_physic_pendulum(t, angle, g, l1, l2, d1, d2, m1, m2, i1, i2, f1, f2):
        theta1a, theta1b, theta2a, theta2b = angle

        den = m2*(d2**2) + i2
        inv = 1/(m1*(d1**2) + i1 + m2*(l1**2) - ((m2**2)*(l1**2)*(d2**2)*(math.cos(theta1a - theta2a)**2))/den)

        num1 = -(m2**2)*(l1**2)*(d2**2)*(theta1b**2)*math.cos(theta1a - theta2a)*math.sin(theta1a - theta2a)
        num2 = (m2**2)*g*l1*(d2**2)*math.cos(theta1a - theta2a)*math.sin(theta2a)
        num3 = m2*l1*d2*f2*theta2b*math.cos(theta1a - theta2a)
        term1 = -m2*l1*d2*(theta2b**2)*math.sin(theta1a - theta2a)
        term2 = -m1*g*d1*math.sin(theta1a)
        term3 = -m2*g*l1*math.sin(theta1a)
        term4 = -f1*theta1b

        num4 = -m2*l1*d2*math.cos(theta1a - theta2a)
        num5 = m2*l1*d2*(theta1b**2)*math.sin(theta1a - theta2a)
        num6 = -m2*g*d2*math.sin(theta2a)
        num7 = -f2*theta2b

        dtheta1adt = theta1b
        dtheta1bdt = inv*((num1 + num2 + num3)/den + term1 + term2 + term3 + term4)
        dtheta2adt = theta2b
        dtheta2bdt = (num4*dtheta1bdt + num5 + num6 + num7)/den

        return np.array([dtheta1adt,dtheta1bdt,dtheta2adt,dtheta2bdt])