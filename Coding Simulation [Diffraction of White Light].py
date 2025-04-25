import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# Input Variables:
screenDistance = float(input("Enter the distance between the grating and the screen (m): "))
screenWidth = float(input("Enter the width of the screen (m): "))
slitSeparation = float(input("Enter the distance between slits (m): "))
slitNum = int(input("Enter the number of slits: "))

thetaMAX = np.arctan((screenWidth / 2) / screenDistance)

# Wavelength Spectrum:
wlRed = random.randint(626,750) * 10**-9
wlOrange = random.randint(591,625) * 10**-9
wlYellow = random.randint(566,590) * 10**-9
wlGreen = random.randint(521,565) * 10**-9
wlCyan = random.randint(496,520) * 10**-9
wlBlue = random.randint(476,495) * 10**-9
wlIndigo = random.randint(451,475) * 10**-9
wlViolet = random.randint(381,450) * 10**-9

# Function of Intensity:
theta = np.linspace(-thetaMAX, thetaMAX, 1000000)

betaRed = (np.pi * slitSeparation * np.sin(theta)) / wlRed
betaOrange = (np.pi * slitSeparation * np.sin(theta)) / wlOrange
betaYellow = (np.pi * slitSeparation * np.sin(theta)) / wlYellow
betaGreen = (np.pi * slitSeparation * np.sin(theta)) / wlGreen
betaCyan = (np.pi * slitSeparation * np.sin(theta)) / wlCyan
betaBlue = (np.pi * slitSeparation * np.sin(theta)) / wlBlue
betaIndigo = (np.pi * slitSeparation * np.sin(theta)) / wlIndigo
betaViolet = (np.pi * slitSeparation * np.sin(theta)) / wlViolet

IRed = (np.sin(slitNum * betaRed) / np.sin(betaRed))**2
IOrange = (np.sin(slitNum * betaOrange) / np.sin(betaOrange))**2
IYellow = (np.sin(slitNum * betaYellow) / np.sin(betaYellow))**2
IGreen = (np.sin(slitNum * betaGreen) / np.sin(betaGreen))**2
ICyan = (np.sin(slitNum * betaCyan) / np.sin(betaCyan))**2
IBlue = (np.sin(slitNum * betaBlue) / np.sin(betaBlue))**2
IIndigo = (np.sin(slitNum * betaIndigo) / np.sin(betaIndigo))**2
IViolet = (np.sin(slitNum * betaViolet) / np.sin(betaViolet))**2

# Line Graph of Intensity Distribution (Grouped):
xDistance = screenDistance * np.tan(theta)

plt.figure(figsize=(10,4))

plt.plot(xDistance, IRed, label='Red', color='red')
plt.plot(xDistance, IOrange, label='Orange', color='orange')
plt.plot(xDistance, IYellow, label='Yellow', color='yellow')
plt.plot(xDistance, IGreen, label='Green', color='green')
plt.plot(xDistance, ICyan, label='Cyan', color='cyan')
plt.plot(xDistance, IBlue, label='Blue', color='blue')
plt.plot(xDistance, IIndigo, label='Indigo', color='indigo')
plt.plot(xDistance, IViolet, label='Violet', color='violet')

plt.xlabel("Screen (m)")
plt.ylabel("Intensity (I_max)")
plt.title("Intensity Disitrbution of White Light")
plt.grid(True)
plt.show()