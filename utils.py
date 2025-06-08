import numpy as np

def pi_formatter(y, pos):
    n = int(np.round(y / (np.pi / 4)))
    if n == 0:
        return "0"
    elif n == 1:
        return "π/4"
    elif n == -1:
        return "−π/4"
    elif n == 2:
        return "π/2"
    elif n == -2:
        return "−π/2"
    elif n == 3:
        return "3π/4"
    elif n == -3:
        return "−3π/4"
    elif n == 4:
        return "π"
    elif n == -4:
        return "−π"
    else:
        return f"{n}π/4"
