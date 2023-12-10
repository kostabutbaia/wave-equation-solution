import numpy as np
from utils import *
from fourier import *

def get_analytic_sol_at_t(t: float, x_range: list[float], sum_N: int, g, f, L, a) -> list[float]:
    return [
        partial_sum(sum_N,
                    lambda n: L/(n*np.pi*a),
                    lambda n: b_n(n, x_range, get_func(g, x_range), L),
                    lambda n: np.sin(n*np.pi*a*t/L),
                    lambda n: np.sin(n*np.pi*x/L)
                    ) + \
        partial_sum(sum_N,
                    lambda n: b_n(n, x_range, get_func(f, x_range), L),
                    lambda n: np.cos(n*np.pi*a*t/L),
                    lambda n: np.sin(n*np.pi*x/L)
                    )
        for x in x_range
    ]

def get_analytic_sol(x_range: list[float], t_range: list[float], sum_N: int, g, f, L, a):
    return [
        get_analytic_sol_at_t(t, x_range, sum_N, g, f, L, a)
        for t in t_range
    ]


def main():
    pass


if __name__ == '__main__':
    main()