import numpy as np

def rk4_simple_pendulum(f, theta0, h, g, l):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l)
    k2 = f(t + h/2, theta + h/2 * k1, g, l)
    k3 = f(t + h/2, theta + h/2 * k2, g, l)
    k4 = f(t + h, theta + h * k3, g, l)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_simple_physic_pendulum(f, theta0, h, g, l, d, m, i):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l, d, m, i)
    k2 = f(t + h/2, theta + h/2 * k1, g, l, d, m, i)
    k3 = f(t + h/2, theta + h/2 * k2, g, l, d, m, i)
    k4 = f(t + h, theta + h * k3, g, l, d, m, i)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_double_pendulum(f, theta0, h, g, l1, l2, m1, m2):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l1, l2, m1, m2)
    k2 = f(t + h/2, theta + h/2 * k1, g, l1, l2, m1, m2)
    k3 = f(t + h/2, theta + h/2 * k2, g, l1, l2, m1, m2)
    k4 = f(t + h, theta + h * k3, g, l1, l2, m1, m2)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_double_physic_pendulum(f, theta0, h, g, l1, l2, d1, d2, m1, m2, i1, i2):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l1, l2, d1, d2, m1, m2, i1, i2)
    k2 = f(t + h/2, theta + h/2 * k1, g, l1, l2, d1, d2, m1, m2, i1, i2)
    k3 = f(t + h/2, theta + h/2 * k2, g, l1, l2, d1, d2, m1, m2, i1, i2)
    k4 = f(t + h, theta + h * k3, g, l1, l2, d1, d2, m1, m2, i1, i2)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta