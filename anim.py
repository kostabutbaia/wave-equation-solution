import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

from wavesol import get_wave_solution

from params import *


def create_anim_gif(name: str) -> None:
    fig = plt.figure()
    plt.xlim(-0.5, L)
    plt.ylim(-h-2, h+2)
    plt.grid()
    x_range, frames = get_wave_solution(L, num_x, max_t, num_t, speed, phi_func, psi_func, integral_step, fixed_end)
    l, = plt.plot([], [], 'k-')
    point, = plt.plot([], [], 'go')
    
    writer = PillowWriter(fps=FPS)

    with writer.saving(fig, f'solutions/{name}.gif', 100):
        for frame in frames:
            l.set_data(x_range, frame)
            point.set_data(x_range[0], frame[0])
            writer.grab_frame()


if __name__ == '__main__':
    create_anim_gif(NAME)