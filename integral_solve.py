import numpy as np

def riemman_sum_solve_integral(y_points: list[int], delta_x: int) -> int:
    return delta_x * y_points[:-1].sum()

# Tests

def check_test(test_name: str, passed: bool):
    result = 'PASSED' if passed else 'FAILED'
    print(f'Test {test_name}: {result}')

def run_tests():
    check_test('x squared', test_x_squared())
    check_test('sin(x)', test_sin_x())

def test_x_squared() -> bool:
    x_range = np.linspace(0, 1, 1000)
    y_points = np.array([x**2 for x in x_range])
    real_solution = 1/3

    riemman_sol = riemman_sum_solve_integral(y_points, 1/1000)
    return np.abs(riemman_sol-real_solution) < 0.01

def test_sin_x() -> bool:
    x_range = np.linspace(0, 1, 200)
    y_points = np.array([np.sin(x) for x in x_range])
    real_solution = -np.cos(1)+np.cos(0)

    riemman_sol = riemman_sum_solve_integral(y_points, 1/200)
    return np.abs(riemman_sol-real_solution) < 0.01

if __name__ == '__main__':
    run_tests()