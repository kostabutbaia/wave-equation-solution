import numpy as np
from utils import *
from fourier import *
from animcreate import create_anim_gif

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
    L = 1
    t_final = 5
    g_func = lambda x: 18*x*(x-1)*np.sin(6*x**2)
    f_func = lambda x: 0
    c = 1

    x_range = np.linspace(0, L, 30)
    t_range = np.linspace(0, t_final, 400)
    frames = get_analytic_sol(x_range, t_range, 5, g_func, f_func, L, c)
    create_anim_gif('fixed_ends/fixed-analytic-speed', 15, frames, x_range, [0, L], [-3, 3])


if __name__ == '__main__':
    main()