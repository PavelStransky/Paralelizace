import numpy as np
import time

def f(x):
    return np.exp(-x) * np.sin(x)


def g(x):
    return 1 / np.sqrt(1 + 1 / np.sqrt(1 + x**3))


def integrator_1d_cyklus(f, a, b, N):
    soucet = 0
    for _ in range(N):
        x = np.random.uniform(a, b)
        soucet += f(x)
    return (b - a) / N * soucet

def integrator_1d(f, a, b, N):
    x = np.random.uniform(a, b, size=N)
    return (b - a) / N * sum(f(x))

def integruj_f(N):
    return integrator_1d_cyklus(f, 0, np.sqrt(10), N)

if __name__ == "__main__":
    N = 10000000
    
    pocatecni_cas = time.time()
    integral_cyklus = integrator_1d_cyklus(f, 0, np.sqrt(10), N)
    doba_vypoctu = time.time() - pocatecni_cas

    print(f"Integrace f (cyklus) = {integral_cyklus}, doba výpočtu: {doba_vypoctu} s.")

    pocatecni_cas = time.time()
    integral_rada = integrator_1d(f, 0, np.sqrt(10), N)
    doba_vypoctu = time.time() - pocatecni_cas

    print(f"Integrace f (řada) = {integral_rada}, doba výpočtu: {doba_vypoctu} s.")
