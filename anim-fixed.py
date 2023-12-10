import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

from fixedsol import get_analytic_sol
from fixednum import get_num_sol

# from params import *

a = 1
L = 1

def g_func(x):
    return 0

def f_func(x):
    return 9*x*(x-1)*np.sin(6*x**2)

def create_anim_gif(name: str) -> None:
    fig = plt.figure()
    plt.xlim(0, L)
    plt.ylim(-3, 3)
    plt.grid()
    # x_range = np.linspace(0, L, 30)
    # t_range = np.linspace(0, 5, 400)
    # frames = get_analytic_sol(x_range, t_range, 5, g_func, f_func, L, a)

    delta_t = 0.0125
    delta_x = 0.033

    x_range = np.arange(0, L, delta_x)
    
    frames = get_num_sol(delta_x, delta_t, 5, 1, 1)

    l, = plt.plot([], [], 'k-')
    
    writer = PillowWriter(fps=15)

    with writer.saving(fig, f'solutions/{name}.gif', 100):
        for frame in frames:
            l.set_data(x_range, frame)
            writer.grab_frame()


if __name__ == '__main__':
    create_anim_gif('both-fixed-num')