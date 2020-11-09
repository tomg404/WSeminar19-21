from vars import *

csvFile =  CSV_FOLDER + "mems_wave.csv"


resolution = 1                                                                      # Nur jeden n-ten wert verwenden
x = np.genfromtxt(csvFile, delimiter=",", skip_header=8, usecols=1) / 1000000    # Zeit
y = np.genfromtxt(csvFile, delimiter=",", skip_header=8, usecols=2)                 # Spannung

plotTitle = "Oszilloskop Messung vom MEMS-Mikrofon"
plt.plot(x[1::resolution], y[1::resolution], "k-", linewidth=0.5)
plt.grid()
plt.xlabel("Zeit [s]")
plt.ylabel("Spannung [mV]")
#plt.title(plotTitle)
plt.xlim(xmin=0,xmax=x[-1])

END_FUNCTION(plotTitle)


	