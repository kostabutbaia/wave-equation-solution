import numpy as np

from utils import get_func

def split_array_N(arr: list[float], N: int) -> list[float]:
    if len(arr) % N != 0:
        raise Exception(f'cannot evenly divide arr with each array of length {N}')
    return [arr[i*N:(i+1)*N] for i in range(int(len(arr)/N))]

def get_var_pos(i: int, j: int, N_x: int) -> int:
    return i + N_x*j

def f_func(x):
    return 9*x*(x-1)*np.sin(6*x**2)


def get_num_sol(delta_x, delta_t, t_final, L, c):
    C = delta_t/delta_x*c
    x_range = np.arange(0, L, delta_x)
    t_range = np.arange(0, t_final, delta_t)

    N_x = len(x_range)
    N_t = len(t_range)
    u = np.zeros((N_x*N_t))

    # u(x, 0) = g(x)
    for i, x in enumerate(x_range):
        u[get_var_pos(i, 0, N_x)] = f_func(x)

    for i in range(1, N_x):
        u[get_var_pos(i, 1, N_x)] = u[get_var_pos(i, 0, N_x)] - 0.5*C**2*(u[get_var_pos(i + 1, 0, N_x)] - 2*u[get_var_pos(i, 0, N_x)] + u[get_var_pos(i - 1, 0, N_x)])
    
    for j in range(1, N_t - 1):
        for i in range(1, N_x - 1):   
            u[get_var_pos(i, j + 1, N_x)] = -u[get_var_pos(i, j - 1, N_x)] + 2 * u[get_var_pos(i, j, N_x)] + C**2*(u[get_var_pos(i + 1, j, N_x)] - 2*u[get_var_pos(i, j, N_x)] + u[get_var_pos(i - 1, j, N_x)])

    return split_array_N(u, N_x)


def main():
    pass


if __name__ == '__main__':
    main()