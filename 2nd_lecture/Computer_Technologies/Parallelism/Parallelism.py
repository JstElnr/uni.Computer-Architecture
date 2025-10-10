import matplotlib.pyplot as plt
import numpy as np
N=np.arange(1,33)
P=0.9
S=1/((1-P)+(P/N))
plt.plot(N,S,marker='o',color='purple')
plt.title("Amdahl's Law-Speedup vs Number of Proccessors")
plt.xlabel("Speedup (S)")
plt.grid(True)
plt.show()