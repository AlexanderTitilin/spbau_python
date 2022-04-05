from random import random
from math import cos, pi
import time
from numba import njit 

@njit()
def randfloat_jit(a, b):
    return random() * (b - a) + a


@njit()
def monte_carlo_integral_jit(a, b, f, n):
    s = 0
    for _ in range(n):
        s += f(randfloat_jit(a, b))
    return ((b - a) / n) * s
@njit()
def cos_integral_jit(n):
    return monte_carlo_integral_jit(0, pi / 2, cos, n)



        
