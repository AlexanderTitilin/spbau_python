#!/usr/bin/env python3
from random import random
from math import cos, pi
import time
import multiprocessing as mp


def randfloat(a, b):
    return random() * (b - a) + a


def monte_carlo_integral(a, b, f, n):
    s = 0
    for _ in range(n):
        s += f(randfloat(a, b))
    return ((b - a) / n) * s


def cos_integral(n):
    return monte_carlo_integral(0, pi / 2, cos, n)


if __name__ == "__main__":
    with mp.Pool(processes=mp.cpu_count()) as pool:
        print("Ищем интеграл функции сos(x) на [0,pi/2]")
        print("c помощью формул с матанализа понимаем, что он равен 1")
        N = 100000
        M = 1000
        t0 = time.time()
        print("считаем с помощью multiprocessing")
        mp_cos_integral_val = sum(pool.map(cos_integral, [N] * M)) / M
        print(
            f"{mp_cos_integral_val}-значение ,посчитали за {time.time() - t0}  сек"
        )
        t0 = time.time()
        print("Считаем по-простому")
        cos_integral_val = cos_integral(N * M)
        print(
                f"{cos_integral_val} - значение ,посчитали за {time.time() - t0} сек"
                )
