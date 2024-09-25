import numpy as np
import matplotlib.pyplot as plt 




# Define the range for r
r = np.linspace(0.01, 1.0, 1000)  # Avoid division by zero 

# Given expressions
E_A = 1.436 / r
E_R = 5.86e-6 / r**9
E_N = E_A + E_R

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.plot(r, E_A, label='$E_A$', color='blue')
plt.plot(r, E_R, label='$E_R$', color='red')
plt.plot(r, E_N, label='$E_N$', color='green')

# Adding labels and legend
plt.xlabel('Interionic separation $r$ (nm)')
plt.ylabel('Energy (eV)')
plt.title('Potential Energies $E_A$, $E_R$, and $E_N$ vs Interionic separation $r$')
plt.legend()
plt.grid(True)
plt.show()