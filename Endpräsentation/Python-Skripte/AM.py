# (c) Tom Gaimann, 2020
# Zusammensetzung eines amplitudenmodulierten Signals
# Ref: https://medium.com/@nabanita.sarkar/simulating-amplitude-modulation-using-python-6ed03eb4e712

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

A_modulator = 1  # Amplitude der Nachrichten Welle
f_modulator = 4  # Frequenz der Nachrichten Welle
A_carrier = 1  # Amplitude der Träger Welle
f_carrier = 40  # Frequenz der Träger Welle
modulation_index = 1

t = np.linspace(0, 1, 1000)  # Zeit

carrier = A_carrier * np.cos(2 * np.pi * f_carrier * t)
modulator = A_modulator * np.cos(2 * np.pi * f_modulator * t)
product = (
    A_carrier
    * (1 + modulation_index * np.cos(2 * np.pi * f_modulator * t))
    * np.cos(2 * np.pi * f_carrier * t)
)

plt.subplot(3, 1, 1)
plt.title("Amplituden Modulation")
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

fig.savefig("AM.png", dpi=100)
