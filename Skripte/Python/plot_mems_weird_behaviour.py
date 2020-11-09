from vars import *

print(" -> Please change input files manually if needed!")

csv_CH1 = CSV_FOLDER + "weird_mems_CH1.csv"
csv_CH2 = CSV_FOLDER + "weird_mems_CH2.csv"

fig, (ax1, ax2) = plt.subplots(2)

ax1.set_xlabel("Zeit [s]")
ax1.set_ylabel("Spannung [mV]")

ax2.set_xlabel("Zeit [s]")
ax2.set_ylabel("Spannung [mV]")

# CH1
plt.subplot(2,1,1)
x_CH1 = np.genfromtxt(csv_CH1, delimiter=",", skip_header=8, usecols=1) / 1000000
y_CH1 = np.genfromtxt(csv_CH1, delimiter=",", skip_header=8, usecols=2)
total_time = x_CH1[-1]
#ax1.set_title("Ausgangsspannung des MEMS-Mikrofons")
ax1.grid()
ax1.plot(x_CH1, y_CH1, 'k', linewidth=0.5)
ax1.set_xlim(xmin=0,xmax=total_time)

# CH2
plt.subplot(2,1,2)  
y_CH2 = np.genfromtxt(csv_CH2, delimiter=",", skip_header=8, usecols=2)
#ax2.set_title("Ausgangsspannung des ATtinys")
ax2.grid()
ax2.plot(x_CH1, y_CH2, 'k', linewidth=0.5)
ax2.set_xlim(xmin=0,xmax=total_time)


plt.tight_layout()
plt.show()

