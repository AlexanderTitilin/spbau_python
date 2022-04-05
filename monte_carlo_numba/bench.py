#!/usr/bin/env python3
from monte_carlo import *
from monte_carlo_numba import *

if __name__ == "__main__":
    print("Ищем интеграл функции сos(x) на [0,pi/2]")
    print("c помощью формул с матанализа понимаем, что он равен 1")
    N = 100000000
    t0 = time.time()
    print("Считаем по-простому")
    cos_integral_val = cos_integral(N)
    print(
            f"{cos_integral_val} - значение ,посчитали за {time.time() - t0} сек"
            )
    print("Считаем с nubma")
    t0 = time.time()
    cos_integral_jit_val = cos_integral_jit(N)
    print(
            f"{cos_integral_jit_val} - значение ,посчитали за {time.time() - t0} сек"
            )

