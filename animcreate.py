import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


def create_anim_gif(name: str, FPS: int, frames: list[float], x_range: list[float], xlims: list[float], ylims: list[float]) -> None:
    fig = plt.figure()
    plt.xlim(xlims[0], xlims[1])
    plt.ylim(ylims[0], ylims[1])
    plt.grid()
    l, = plt.plot([], [], 'k-')
    
    writer = PillowWriter(fps=FPS)

    with writer.saving(fig, f'solutions/{name}.gif', 100):
        for frame in frames:
            l.set_data(x_range, frame)
            writer.grab_frame()