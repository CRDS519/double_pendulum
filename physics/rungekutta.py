import numpy as np

def rk4_simple_pendulum(f, theta0, h, g, l, friction_factor):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l, friction_factor)
    k2 = f(t + h/2, theta + h/2 * k1, g, l, friction_factor)
    k3 = f(t + h/2, theta + h/2 * k2, g, l, friction_factor)
    k4 = f(t + h, theta + h * k3, g, l, friction_factor)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_simple_physic_pendulum(f, theta0, h, g, l, d, m, i, friction_factor):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l, d, m, i, friction_factor)
    k2 = f(t + h/2, theta + h/2 * k1, g, l, d, m, i, friction_factor)
    k3 = f(t + h/2, theta + h/2 * k2, g, l, d, m, i, friction_factor)
    k4 = f(t + h, theta + h * k3, g, l, d, m, i, friction_factor)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_double_pendulum(f, theta0, h, g, l1, l2, m1, m2, friction_factor):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l1, l2, m1, m2, friction_factor)
    k2 = f(t + h/2, theta + h/2 * k1, g, l1, l2, m1, m2, friction_factor)
    k3 = f(t + h/2, theta + h/2 * k2, g, l1, l2, m1, m2, friction_factor)
    k4 = f(t + h, theta + h * k3, g, l1, l2, m1, m2, friction_factor)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta

def rk4_double_physic_pendulum(f, theta0, h, g, l1, l2, d1, d2, m1, m2, i1, i2, friction_factor):
    t = 0
    theta = np.array(theta0)
    k1 = f(t, theta, g, l1, l2, d1, d2, m1, m2, i1, i2, friction_factor)
    k2 = f(t + h/2, theta + h/2 * k1, g, l1, l2, d1, d2, m1, m2, i1, i2, friction_factor)
    k3 = f(t + h/2, theta + h/2 * k2, g, l1, l2, d1, d2, m1, m2, i1, i2, friction_factor)
    k4 = f(t + h, theta + h * k3, g, l1, l2, d1, d2, m1, m2, i1, i2, friction_factor)
    theta += h/6*(k1 + 2*k2 + 2*k3 + k4)
    return theta