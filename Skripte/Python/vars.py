# (c) Tom Gaimann - 2020

from scipy.stats import linregress
import matplotlib.pyplot as plt
import scipy.signal
from vars import *
import numpy as np
import csv
import sys

CSV_FOLDER = "Data/"
PGF_OUTPUT = "PGFplots/"
PNG_OUTPUT = "PNGplots/"

print("+----------------------------------------------------------+")
print("|                  (c) Tom Gaimann - 2020                  |")
print("|  W-Seminar Projekt: Optoelektronik und Halbleiterphysik  |")
print("|  Executing: " + sys.argv[0] + (45-len(sys.argv[0]))*" "+"|")
print("+----------------------------------------------------------+")
print("|  Usage: python program.py [pgf/png] [input-file]         |")
print("|  All of the following text is program output:            |")
print("+----------------------------------------------------------+")


try:
	setPgf = False
	setPng = False
	if sys.argv[1] == "pgf":
		setPgf = True
		import matplotlib
		matplotlib.use("pgf")
		matplotlib.rcParams.update({
			"pgf.texsystem": "pdflatex",
			'font.family': 'serif',
			'text.usetex': True,
			'pgf.rcfonts': False,
		})
	elif sys.argv[1] == "png":
		setPng = True
except IndexError:
	pass
	
def END_FUNCTION(plotTitle):
	if setPgf:
		pgf_file = plotTitle.replace(" ", "_").replace("\n", "").lower() +".pgf"
		plt.savefig(PGF_OUTPUT + pgf_file)
		print(" -> " + PGF_OUTPUT + pgf_file)
	elif setPng:
		png_file = plotTitle.replace(" ", "_").replace("\n", "").lower() +".png"
		plt.savefig(PNG_OUTPUT + png_file)
		print(" -> " + PNG_OUTPUT + png_file)
	else:
		plt.show()
	