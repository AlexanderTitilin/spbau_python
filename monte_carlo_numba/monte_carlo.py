from random import random
from math import cos, pi
import time


def randfloat(a, b):
    return random() * (b - a) + a


def monte_carlo_integral(a, b, f, n):
    s = 0
    for _ in range(n):
        s += f(randfloat(a, b))
    return ((b - a) / n) * s


def cos_integral(n):
    return monte_carlo_integral(0, pi / 2, cos, n)


