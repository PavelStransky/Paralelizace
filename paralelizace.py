import numpy as np
import matplotlib.pyplot as plt 

import multiprocessing as mp
import time

import sys

import integrace

def integrator_1d_Pool(V, N, f, a, b):
    m = N // V

    vysledky = 0

    with mp.Pool(processes=V) as pool:
        vysledky = pool.starmap(integrace.integrator_1d_cyklus, [[f, a, b, m]] * V)

    return np.average(vysledky)

def doba_integrace(v_max=8, N=10000000):
    doby_vypoctu = []
    v_rada = range(1, v_max + 1)

    for v in v_rada:
        pocatecni_cas = time.time()
        integral_paralelne = integrator_1d_Pool(v, N, integrace.f, 0, np.sqrt(10))
        doba_vypoctu = time.time() - pocatecni_cas

        doby_vypoctu.append(doba_vypoctu)

        print(f"Počet procesorů: {v}, If (parallel) = {integral_paralelne}, doba výpočtu: {doba_vypoctu} s.")

    plt.plot(v_rada, doby_vypoctu)
    plt.xlabel("Počet vláken")
    plt.ylabel("Doba výpočtu [s]")
    plt.show()

if __name__ == "__main__":
    print("Počet logických jader:", mp.cpu_count())

    N = 5000000

    if len(sys.argv) > 1:
        vlakna = int(sys.argv[1])

        pocatecni_cas = time.time()
        integral_paralelne = integrator_1d_Pool(vlakna, N, integrace.f, 0, np.sqrt(10))
        doba_vypoctu = time.time() - pocatecni_cas

        print(f"Počet procesorů: {vlakna}, If (parallel) = {integral_paralelne}, doba výpočtu: {doba_vypoctu} s.")

    else:
        doba_integrace(v_max=50, N=N)