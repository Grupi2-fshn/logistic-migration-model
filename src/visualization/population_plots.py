import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'serif'

def plot_evolucioni_kohor(t, N_list, labels, title, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    ngjyrat = ['darkblue', 'darkorange', 'forestgreen', 'darkred']
    
    for i, N in enumerate(N_list):
        ax.plot(t, N, linewidth=2, label=labels[i], color=ngjyrat[i % len(ngjyrat)])
        
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel("Koha (t)", fontsize=12)
    ax.set_ylabel("Popullata (N)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def plot_harta_parametrave(X, Y, Z, xlabel, ylabel, title, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
    fig.colorbar(c, ax=ax, label="Popullata Asimptotike")
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()