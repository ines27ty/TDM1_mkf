import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import * 

D = 0.01
C_p = 4.2
rho = 998
lambda_ = 0.6
mu = 0.001
surf = np.pi * 0.01 * 1 
nu = mu / rho
Pr = 6.67
delta_T = 5-90

# Ouvrir le fichier
with open("data.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Re = []
Force = []
Q = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')      # Remplacer les tabulations par des virgules
    values = line.split(',')     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Re.append(float(values[0]))
    Force.append(float(values[1]))
    Q.append(float(values[2]))


# Calcul de la vitesse 
U = [Re[i] * nu / D for i in range(len(Re))]

# Calcul du coefficient de frottement
C_d = [Force[i] / (0.5 * rho * U[i]**2 * 0.01) for i in range(len(Re))]
print("C_d = ", C_d)

plt.figure(1)
plt.plot(Re, C_d,'-o')
plt.xlabel('Re')
plt.ylabel('C_d')
plt.grid()

# Calcul du coefficient de convection
h = [Q[i]/(delta_T * surf) for i in range(len(Re))]
print("h = ", h)

plt.figure(2)
plt.plot(Re, h)
plt.xlabel('Re')
plt.ylabel('h')
plt.grid()

# Calcul du nombre de Nusselt
Nu = [h[i] * D / lambda_ for i in range(len(Re))]

# Calcul du nombre de Nusselt Curchill Bernstein
Nu_CB = [ 0.3 + (0.62 * Re[i]**0.5 * Pr ** (1/3)) / (1 + (0.4 / Pr) ** (2/3)) ** (1/4) * (1 + (Re[i] / 282000) ** (5/8)) ** (4/5) for i in range(len(Re))]

# Calcul du nombre de Nusselt Hilpert
for i in range(len(Re)):
    if (Re[i]> 4000) and (Re[i]< 40000) :
        C = 0.193
        m = 0.618
    elif Re[i] > 40000 :
        C = 0.027
        m = 0.805

Nu_H = [C * Re[i] ** m * Pr ** (1/3) for i in range(len(Re))]

plt.figure(3)
plt.plot(Re, Nu,'-o')
plt.plot(Re, Nu_H)
plt.plot(Re, Nu_CB)
plt.xlabel('Re')
plt.ylabel('Nu')
plt.legend(['Nu', 'Nu_H', 'Nu_CB'])
plt.grid()


plt.show()