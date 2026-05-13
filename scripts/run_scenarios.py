import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scipy.integrate import odeint
from src.models.logistic_migration import modeli_demografik, kapaciteti_konstant, kapaciteti_sezonal, migrim_zero, migrim_proporcional
from src.analysis.demographic_metrics import llogarit_metrikat
from src.visualization.population_plots import plot_evolucioni_kohor

def main():
    t = np.linspace(0, 50, 1000)
    N0 = 10  # Popullata fillestare
    r = 0.3  # Shkalla e rritjes
    K0 = 100 # Kapaciteti mbajtës bazë
    
    # 1. Rritje logjistike pa migrim
    N_logjistik = odeint(modeli_demografik, N0, t, args=(r, kapaciteti_konstant, (K0,), migrim_zero, (), migrim_zero, ()))[:, 0]
    
    # 2. Migrim dalës proporcional (m = 0.1)
    N_migrim = odeint(modeli_demografik, N0, t, args=(r, kapaciteti_konstant, (K0,), migrim_zero, (), migrim_proporcional, (0.1,)))[:, 0]
    
    # 3. Kapacitet sezonal (a=0.3, T=10)
    N_sezonal = odeint(modeli_demografik, N0, t, args=(r, kapaciteti_sezonal, (K0, 0.3, 10), migrim_zero, (), migrim_zero, ()))[:, 0]

    # Gjenerimi i figurave
    plot_evolucioni_kohor(t, [N_logjistik, N_migrim, N_sezonal], 
                          ["Baza (Logjistike)", "Me Migrim Dalës", "Kapacitet Sezonal"],
                          "Evolucioni i Popullatës në Skenarë të Ndryshëm",
                          "results/figures/skenaret_evolucioni.png")
    
    # Llogaritja dhe printimi i metrikave
    print("--- Metrikat Numerike ---")
    skenaret = {"Logjistik": N_logjistik, "Migrim": N_migrim, "Sezonal": N_sezonal}
    for emer, N in skenaret.items():
        metrikat = llogarit_metrikat(t, N, K0)
        print(f"[{emer}] Max: {metrikat['Maksimumi']:.2f}, Asimptota: {metrikat['Vlera Asimptotike']:.2f}, Koha t(K/2): {metrikat['Koha e N/K=0.5']:.2f}")

if __name__ == "__main__":
    main()