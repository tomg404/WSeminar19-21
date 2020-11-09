from vars import *
from numpy import array, exp
from scipy.optimize import curve_fit

x = np.array([0.5,   2,   4,   6,   8,  10,  12])
y = np.array([508, 348, 304, 208, 180, 104,  68])

x1 = np.linspace(0.5, 12, 1000)
#x1 = np.logspace(-5, 5, 1000)

plotTitle = "Ausgangsspannung des MEMS-Mikrofons in Abhängigkeit\ndes Laserpunktdurchmessers"
plt.rcParams['axes.axisbelow'] = True
plt.grid()
plt.xlabel("Laserpunktdurchmesser [mm]")
plt.ylabel("Spannung [mV]")
#plt.title(plotTitle)
plt.xlim(xmin=0,xmax=12.5)


def func1(x,a,b):
	return a/(x**b)	
params, _ = curve_fit(func1, x, y, maxfev=10000)
a, b = params[0], params[1]
yfit1 = a/(x**b)
plt.plot(x1, func1(x1,a,b))
print(a,b)

m = linregress(x,y)[0]	# -34.5
t = linregress(x,y)[1]	# 452.7
plt.plot(x, m * x + t, 'r:', linewidth=1)


plt.scatter(x, y, color='k')
#plt.annotate(r'Gleichung der Geraden:', xy=(6,450), fontsize=13)
#plt.annotate(r'$ f(x) = -34.5 * x + 452.7 $', xy=(6,420), fontsize=13)

END_FUNCTION(plotTitle)