# (c) Tom Gaimann, 2020
# Zusammensetzung eines frequenzmodulierten Signals
# Ref: https://gist.github.com/fedden/d06cd490fcceab83952619311556044a

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

f_modulator = 4  # Frequenz der Nachrichten Welle
f_carrier = 40  # Frequenz der Träger Welle
modulation_index = 1.0

time = np.linspace(0, 1, 1000)  # Zeit

carrier = np.cos(2.0 * np.pi * f_carrier * time)
modulator = np.cos(2.0 * np.pi * f_modulator * time) * modulation_index
product = np.zeros_like(modulator)

for i, t in enumerate(time):
    product[i] = np.cos(2.0 * np.pi * (f_carrier * t + modulator[i]))

plt.subplot(3, 1, 1)
plt.title("Frequenz Modulation")
plt.plot(modulator, color="green")
plt.ylabel("Amplitude")
plt.xlabel("Nachrichten Signal")

plt.subplot(3, 1, 2)
plt.plot(carrier, color="red")
plt.ylabel("Amplitude")
plt.xlabel("Träger Signal")

plt.subplot(3, 1, 3)
plt.plot(product, color="purple")
plt.ylabel("Amplitude")
plt.xlabel("Moduliertes Signal")

# Plot Einstellungen
plt.subplots_adjust(hspace=1)
plt.rc("font", size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)

fig.savefig("FM.png", dpi=100)
