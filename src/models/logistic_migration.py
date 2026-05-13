import numpy as np

def kapaciteti_konstant(t, K0):
    return K0

def kapaciteti_sezonal(t, K0, a, T):
    """Kapaciteti periodik K(t) = K0 * [1 + a * sin(2*pi*t/T)]"""
    return K0 * (1 + a * np.sin(2 * np.pi * t / T))

def kapaciteti_renie(t, K0, r_renie):
    """Kapaciteti në rënie graduale."""
    return K0 * np.exp(-r_renie * t)

def modeli_demografik(N, t, r, K_func, K_args, M_in_func, M_in_args, M_out_func, M_out_args):
    """
    Ekuacioni diferencial i modelit:
    dN/dt = r*N*(1 - N/K(t)) + M_in(t) - M_out(t)
    """
    K_t = K_func(t, *K_args)
    M_in = M_in_func(t, *M_in_args)
    M_out = M_out_func(N, t, *M_out_args)
    
    # Parandalimi i popullatës negative
    if N <= 0 and (r * N * (1 - N / K_t) + M_in - M_out) < 0:
        return 0.0
        
    dNdt = r * N * (1 - N / K_t) + M_in - M_out
    return dNdt

# Funksione ndihmëse për migrimin
def migrim_zero(t_or_N, *args): return 0.0
def migrim_proporcional(N, t, m): return m * N