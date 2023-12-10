from integral_solve import riemman_sum_solve_integral
import numpy as np
import matplotlib.pyplot as plt

def b_n(n: int, x_points: list[float], y_points: list[float], L: float) -> float:
    func = np.array(y_points) * np.array([np.sin(n*np.pi/L*x) for x in x_points])
    integral_sol = 2/L*riemman_sum_solve_integral(func, L/(len(x_points) - 1))
    return integral_sol

def get_series_at_x(x: float, L: float, N: int, x_points: list[float], y_points: list[float]) -> float:
   f = np.array([b_n(i, x_points, y_points, L)*np.sin(i*np.pi/L*x) for i in range(1, N+1)])
   return f.sum()

def test():
    L = 1
    N = 100
    x_points = np.linspace(0, L, N)
    y_points = np.array([x**2 for x in x_points])

    res = [get_series_at_x(x, L, 30, x_points, y_points) for x in x_points]
    plt.plot(x_points, y_points)
    plt.plot(x_points, res)
    plt.show()


if __name__ == '__main__':
    test()