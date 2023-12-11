import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

from fixedsol import get_analytic_sol
from fixednum import get_num_sol

# Parameters

a = 1
L = 1

def g_func(x):
    return 0

def f_func(x):
    return 9*x*(x-1)*np.sin(6*x**2)

def create_compare_gif(
        name: str,
        title: str,
        FPS: int,
        frames1: list[float],
        label1: str,
        frames2: list[float],
        label2: str,
        x_range: list[float],
        xlims: list[float],
        ylims: list[float]
) -> None:
    if len(frames1) != len(frames2):
        raise Exception(f'frames amount dont match {len(frames1)} != {len(frames2)}')
    fig = plt.figure()
    plt.title(title)
    plt.xlim(xlims[0], xlims[1])
    plt.ylim(ylims[0], ylims[1])
    plt.grid()
    l1, = plt.plot([], [], 'k-', label=label1)
    l2, = plt.plot([], [], 'k--', label=label2)
    plt.legend()
    
    writer = PillowWriter(fps=FPS)

    with writer.saving(fig, f'solutions/fixed_ends/{name}.gif', 100):
        for i in range(len(frames1)):
            l1.set_data(x_range, frames1[i])
            l2.set_data(x_range, frames2[i])
            writer.grab_frame()


if __name__ == '__main__':
    L = 1
    t_final = 5
    g_func = lambda x: 0
    f_func = lambda x: 9*x*(x-1)*np.sin(6*x**2)
    c = 1
    x_range = np.linspace(0, L, 60)
    t_range = np.linspace(0, t_final, 400)
    print('calculating...')
    frames_num = get_num_sol(x_range, t_range, c, f_func, g_func)
    frames_real = get_analytic_sol(x_range, t_range, 5, g_func, f_func, L, c)
    print('making animation')

    create_compare_gif(
        'fixed-compared',
        'with initial profile',
        15,
        frames_real,
        'real solution',
        frames_num,
        'numerical solution',
        x_range,
        [0, L],
        [-3, 3]
    )