from vars import *

csvFile = CSV_FOLDER + "attiny-output_wave.csv"

resolution = 1                                                                      # Nur jeden n-ten wert verwenden
x = np.genfromtxt(csvFile, delimiter=",", skip_header=8, usecols=1) /1000000		# Zeit Konversion von Nanosekunden zu Sekunden
y = np.genfromtxt(csvFile, delimiter=",", skip_header=8, usecols=2)                 # Spannung
total_time = x[-1] 

plotTitle = "Oszilloskop Messung vom Attiny13a"
plt.plot(x[1::resolution], y[1::resolution], "k-", linewidth=0.5)
plt.grid()
plt.xlabel("Zeit [s]")
plt.ylabel("Spannung [mV]")
#plt.title(plotTitle)
plt.xlim(xmin=0,xmax=total_time)

# sägezahn welle
#x_int = np.linspace(x[0], x[-1], 100)
#tck = interpolate.splrep(x, y, k=3, s=1000)
#y_int = interpolate.splev(x_int, tck, der = 0)
#plt.plot(x_int, y_int, "r-")

yhat = scipy.signal.savgol_filter(y, 5, 3)
plt.plot(x, yhat, "r-")

END_FUNCTION(plotTitle)