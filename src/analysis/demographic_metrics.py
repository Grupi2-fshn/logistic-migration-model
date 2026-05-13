import numpy as np

def llogarit_metrikat(t, N, K_target):
    """Llogarit metrikat bazë të kërkuara."""
    maksimumi = np.max(N)
    vlera_asimptotike = N[-1]
    
    # Koha e përgjysmimit (koha kur N arrin K/2 për herë të parë)
    gjysma_K = K_target / 2.0
    indekset = np.where(N >= gjysma_K)[0]
    koha_pergjysem = t[indekset[0]] if len(indekset) > 0 else np.nan
    
    return {
        "Maksimumi": maksimumi,
        "Vlera Asimptotike": vlera_asimptotike,
        "Koha e N/K=0.5": koha_pergjysem
    }