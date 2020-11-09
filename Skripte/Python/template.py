from vars import *	# automatically looks for png/pgf flag in the first argument
					# if more imports are needed change in vars.py

# Get data
x = ...
y = ...

# Plot Settings
plotTitle = "Example Plot"
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title(plotTitle)
plt.xlim(xmin=0, xmax=100)

# Final Plot
plt.plot(x, y, "k-")

END_FUNCTION(plotTitle)	# automatically decides if export as png/pgf or just show plot