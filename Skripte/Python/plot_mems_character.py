from vars import *

x = np.array([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500])
y = np.array([88 ,  128,  496,  744,  520,  392,  480,  504,  424,  424,  456])

plotTitle = "Spannungsspitzen beim MEMS-Mikrofon in Abhängigkeit von Frequenz"
plt.rcParams['axes.axisbelow'] = True
plt.grid()
plt.scatter(x, y)
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Spannung [mV]")
#plt.title(plotTitle)

END_FUNCTION(plotTitle)