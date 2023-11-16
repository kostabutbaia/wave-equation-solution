import numpy as np

from utils import riemman_sum_solve_integral, get_func_ct, get_func

def calc_psi_int(x: float, t: float, c: float, psi_func, integral_step: int) -> float:
    alpha_range = np.arange(x-c*t, x+c*t, integral_step)
    psi_values = get_func(psi_func, alpha_range)
    return riemman_sum_solve_integral(psi_values, integral_step)

def get_wave_sol_at_t(t: float, x_range: list[float], c: float, phi_func, psi_func, intgral_step: int) -> list[float]:
    phi_values_p = get_func_ct(c, t, phi_func, x_range)
    phi_values_m = get_func_ct(-c, t, phi_func, x_range)
    psi_integral = np.array([calc_psi_int(x, t, c, psi_func, intgral_step) for x in x_range])
    return 1/2*(phi_values_p+phi_values_m) + 1/(2*c)*psi_integral

def get_wave_solution(max_x: float, num_x: float, max_t: float, num_t: int, c: float, phi_func, psi_func, integral_step: int, fixed_end: bool):
    x_range = np.linspace(-max_x, max_x, 2*num_x)
    t_range = np.linspace(0, max_t, num_t)

    sol = list()
    for t in t_range:
        sol_at_t = get_wave_sol_at_t(t, x_range, c, phi_func, psi_func, integral_step)
        sol.append(sol_at_t - sol_at_t[::-1] if fixed_end else sol_at_t + sol_at_t[::-1])
        sol[-1] = sol[-1][num_x:]

    return x_range[num_x:], sol