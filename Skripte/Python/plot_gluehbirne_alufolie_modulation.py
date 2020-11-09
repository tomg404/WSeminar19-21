from vars import *	


csv_file1 = CSV_FOLDER + "Experiment3/" + "gluehbirne_alufolie_modulation.csv"
csv_file2 = CSV_FOLDER + "Experiment3/" + "gluehbirne_ohne_alufolie.csv"

x1 = np.genfromtxt(csv_file1, delimiter=",", skip_header=8, usecols=1) / 1000000
y1 = np.genfromtxt(csv_file1, delimiter=",", skip_header=8, usecols=2)

x2 = np.genfromtxt(csv_file2, delimiter=",", skip_header=8, usecols=1) / 1000000
y2 = np.genfromtxt(csv_file2, delimiter=",", skip_header=8, usecols=2)

fig, (ax1, ax2) = plt.subplots(2)

plotTitle = "Reaktion des MEMS-Mikrofons auf eine Glühbirne"
#fig.suptitle(plotTitle)

ax1.set_xlabel("Zeit [s]")
ax1.set_ylabel("Spannung [mV]")

ax2.set_xlabel("Zeit [s]")
ax2.set_ylabel("Spannung [mV]")

ax1.set_xlim(xmin=0, xmax=x1[-1])
ax2.set_xlim(xmin=0, xmax=x2[-1])
ax1.grid()
ax2.grid()
#ax1.set_title(plotTitle)
fig.tight_layout()
plt.subplots_adjust(left=0.13)

# Final Plot
ax1.plot(x1, y1, "r-", linewidth=0.7)
ax2.plot(x2, y2, "b-", linewidth=0.7)

END_FUNCTION(plotTitle)	# automatically decides if export as png/pgf or just show plot