import numpy as np
import math
from matplotlib import pyplot as plt

N = 20

h = 1.0/N

x = [h*i for i in range(N)]

def precise_solution(x):
    return 2.9*(x**2) - 2.9*x + math.exp(-x) + math.exp(x) - 2

def f_func(x,y,z):
    return z

def g_func(x,y,z):
    return y + 2.9*(x-x**2) + 7.8

def runge_kutta(y_0, z_0):
    y = [y_0] * N
    z = [z_0] * N

    for i in range(N-1):
        K1 = h * f_func(x[i], y[i], z[i])
        L1 = h * g_func(x[i], y[i], z[i])

        K2 = h * f_func(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)
        L2 = h * g_func(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)

        K3 = h * f_func(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)
        L3 = h * g_func(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)

        K4 = h * f_func(x[i] + h, y[i] + K3, z[i] + L3)
        L4 = h * g_func(x[i] + h, y[i] + K3, z[i] + L3)

        y[i+1] = y[i] + (K1 + 2 * K2 + 2 * K3 + K4)/(6.0)
        z[i+1] = z[i] + (L1 + 2 * L2 + 2 * L3 + L4)/(6.0)
    return y, z

def phi(mu):
    y_0 = 0
    z_0 = mu
    y, z = runge_kutta(y_0, z_0)
    return y[-1] - math.exp(1) - math.exp(-1) + 2

def dphi(mu0):
    return 0.5 * math.exp(-mu0) * (math.exp(2 * mu0) + 1)

def newton_modified(mu_0):
    while np.abs(phi(mu_0)) > 0.00001:
        mu_0 = mu_0 - (phi(mu_0) / dphi(mu_1))
    return mu_0

def search_bounds(start=-100):
    while phi(start) < 0:
        start += 1
    return start - 1, start

mu_1,mu_2= search_bounds()

mu = newton_modified(mu_1)
y0 = 0
z0 = mu
y_shoot, z = runge_kutta(y0, z0)


def tridiagonal():
    y = [0] * N
    lam_trid = [0] * N
    mu_trid = [0] * N

    y[N-1] = math.exp(1) + math.exp(-1) - 2

    for i in range(1, N - 1):
        lam_trid[i+1] = (-1)/ (lam_trid[i] - 2+h**2)
        mu_trid[i+1] = (h**2 * (2.9*x[i] * (1-x[i]) + 7.8) - mu_trid[i]) / (lam_trid[i]-2+h**2)
        
    for i in range(N - 1, 1, -1):
        y[i-1] = y[i]*lam_trid[i] + mu_trid[i]

    return y

x_precise = np.linspace(0, 1, 1000)
y_precise = [precise_solution(x_i) for x_i in np.linspace(0, 1, 1000)]
y_trid = tridiagonal()

plt.title(f'N={N}')
plt.plot(x, y_trid, label = f"Tridiagonal method", color='darkviolet')
plt.plot(x, y_shoot, label = f"Shooting method, mu={np.round(mu, 6)}", color='forestgreen')
plt.plot(x_precise, y_precise, label = "Precise solution", color='deeppink')
plt.grid(True)
plt.legend()
plt.show()
