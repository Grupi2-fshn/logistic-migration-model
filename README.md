# Projekti 1: Modeli Demografik Logjistik me Migrim

**Studenti:** Arlind Lacka  
**Grupi:** Grupi 2 
**Lënda:** Modelim në Fizike

## 1. Pershkrimi i Projektit
Ky projekt simulon evolucionin e nje popullate duke perdorur ekuacionin logjistik, te pasuruar me parametra te migrimit (hyrje dhe dalje) dhe nje kapacitet mbajtes $K(t)$ që mund të ndryshoje me kohen. Ky model eshte i rendesishem per të kuptuar stabilitetin e sistemeve biologjike dhe sociale.

## 2. Modeli Matematikor
Ekuacioni diferencial baze që kemi implementuar eshte:

$$ \frac{dN}{dt} = rN \left( 1 - \frac{N}{K(t)} \right) + M_{in} - M_{out} $$

Ku:
*   **N**: Madhesia e popullates.
*   **r**: Shkalla e rritjes intrinseke.
*   **K(t)**: Kapaciteti mbajtes i mjedisit.
*   **$M_{in} - M_{out}$**: Normat e migrimit.

## 3. Struktura e Kodeve
Projekti eshte i organizuar në kete menyre:
*   `src/`: Permban logjiken e modelit dhe funksionet e vizualizimit.
*   `scripts/`: Skriptet kryesore për ekzekutimin e simulimeve (`run_scenarios.py`).
*   `results/figures/`: Grafiket e gjeneruar automatikisht pas ekzekutimit.
*   `requirements.txt`: Bibliotekat e nevojshme (numpy, matplotlib, scipy).

## 4. Si te ekzekutohet projekti
1. Sigurohuni qe keni instaluar bibliotekat:
   ```bash
   pip install -r requirements.txt