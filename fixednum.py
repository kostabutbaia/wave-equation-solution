import numpy as np

from utils import get_func
from animcreate import create_anim_gif

def split_array_N(arr: list[float], N: int) -> list[float]:
    if len(arr) % N != 0:
        raise Exception(f'cannot evenly divide arr with each array of length {N}')
    return [arr[i*N:(i+1)*N] for i in range(int(len(arr)/N))]

def get_var_pos(i: int, j: int, N_x: int) -> int:
    return i + N_x*j

def get_num_sol(x_range, t_range, c, f_func, g_func):
    delta_x, delta_t = x_range[1] - x_range[0], t_range[1] - t_range[0]
    C = delta_t/delta_x*c

    N_x = len(x_range)
    N_t = len(t_range)
    u = np.zeros((N_x*N_t))

    for i, x in enumerate(x_range):
        u[get_var_pos(i, 0, N_x)] = f_func(x)

    for i in range(1, N_x):
        u[get_var_pos(i, 1, N_x)] = u[get_var_pos(i, 0, N_x)] + delta_t*g_func(x_range[i]) - 0.5*C**2*(u[get_var_pos(i + 1, 0, N_x)] - 2*u[get_var_pos(i, 0, N_x)] + u[get_var_pos(i - 1, 0, N_x)])
    
    for j in range(1, N_t - 1):
        for i in range(1, N_x - 1):   
            u[get_var_pos(i, j + 1, N_x)] = -u[get_var_pos(i, j - 1, N_x)] + 2 * u[get_var_pos(i, j, N_x)] + C**2*(u[get_var_pos(i + 1, j, N_x)] - 2*u[get_var_pos(i, j, N_x)] + u[get_var_pos(i - 1, j, N_x)])

    return split_array_N(u, N_x)


def main():
    L = 1
    t_final = 5
    g_func = lambda x: 18*x*(x-1)*np.sin(6*x**2)
    f_func = lambda x: 0
    c = 1
    x_range = np.linspace(0, L, 60)
    t_range = np.linspace(0, t_final, 400)
    frames = get_num_sol(x_range, t_range, c, f_func, g_func)
    create_anim_gif('fixed_ends/fixed-numerical-speed', 15, frames, x_range, [0, L], [-3, 3])


if __name__ == '__main__':
    main()