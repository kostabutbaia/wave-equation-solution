import numpy as np

from utils import get_func

def I(x):
    return 9*x*(x-1)*np.sin(6*x**2)

def get_test_num(x, t):
    Nx = len(x)-1
    c = 1
    u_1 = np.zeros((Nx+1))
    u_2 = np.zeros((Nx+1))
    # Given mesh points as arrays x and t (x[i], t[n])
    dx = x[1] - x[0]
    dt = t[1] - t[0]
    C = c*dt/dx # Courant number
    Nt = len(t)-1
    C2 = C**2 # Help variable in the scheme
    frames = []

    u = np.zeros(((Nx+1)*(Nt+1)))
    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_1[i] = I(x[i])
    # Apply special formula for first step, incorporating du/dt=0
    for i in range(1, Nx):
        u[i] = u_1[i] - 0.5*C**2*(u_1[i+1] - 2*u_1[i] + u_1[i-1])
        u[0] = 0; u[Nx] = 0 # Enforce boundary conditions
        # Switch variables before next step
        u_2, u_1 = u_1, u
    for n in range(1, Nt):
        # Update all inner mesh points at time t[n+1]
        for i in range(1, Nx):
            u[i] = 2*u_1[i] - u_2[i] - \
            C**2*(u_1[i+1] - 2*u_1[i] + u_1[i-1])
            # Insert boundary conditions
            u[0] = 0; u[Nx] = 0
            frames.append(np.array(u))
            u_2, u_1 = u_1, u
    return frames

def main():
    delta_t = 0.0125
    delta_x = 0.33
    t_f = 5
    L=1
    x_range = np.arange(0, L, delta_x)
    t_range = np.arange(0, t_f, delta_t)
    frames = get_test_num(x_range, t_range)

    print(frames)



if __name__ == '__main__':
    main()