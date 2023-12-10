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
    # Boundary Conditions
    # u(0, t) = 0
    for j in range(N_t):
        u[get_var_pos(0, j, N_x)] = 0

    # u(L, t) = 0
    for j in range(N_t):
        u[get_var_pos(N_x - 1, j, N_x)] = 0

    # u(x, 0) = g(x)
    g_values = get_func(f_func, x_range)
    for i in range(N_x):
        u[get_var_pos(i, 0, N_x)] = g_values[i]

    for i in range(1, N_x - 1):
        for j in range(1, N_t - 1):
            u[get_var_pos(i, j + 1, N_x)] = -u[get_var_pos(i, j - 1, N_x)] + 2 * u[get_var_pos(i, j, N_x)] + C**2*(u[get_var_pos(i + 1, j, N_x)] - 2*u[get_var_pos(i, j, N_x)] + u[get_var_pos(i - 1, j, N_x)])

    return split_array_N(u, N_x)


def main():
    pass


if __name__ == '__main__':
    main()