import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scipy.integrate import odeint
from src.models.logistic_migration import modeli_demografik, kapaciteti_konstant, migrim_zero, migrim_proporcional
from src.visualization.population_plots import plot_harta_parametrave

def main():
    t = np.linspace(0, 100, 500)
    N0 = 10
    K0 = 100
    
    r_values = np.linspace(0.05, 0.5, 30)
    m_values = np.linspace(0.0, 0.4, 30)
    
    R, M = np.meshgrid(r_values, m_values)
    Z_asimptota = np.zeros_like(R)
    
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            r_akt = R[i, j]
            m_akt = M[i, j]
            N_sol = odeint(modeli_demografik, N0, t, 
                           args=(r_akt, kapaciteti_konstant, (K0,), migrim_zero, (), migrim_proporcional, (m_akt,)))[:, 0]
            Z_asimptota[i, j] = N_sol[-1]  # Vlera në fund të kohës
            
    plot_harta_parametrave(R, M, Z_asimptota, "Shkalla e Rritjes (r)", "Norma e Migrimit (m)",
                           "Harta e Parametrave: Popullata Asimptotike",
                           "results/figures/param_scan_migration.png")
    print("\n[SUKSES] Harta e parametrave u gjenerua.")

if __name__ == "__main__":
    main()