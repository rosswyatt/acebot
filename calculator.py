
from math import *
from statistics import *

def InputsCalc(command):
	calculation = command.replace("calculate ", "")
	try:
		x = eval(calculation)
		return x
	except(SyntaxError, NameError, TypeError):
		return "Check your syntax. For some help with python, type '@acebot python help'"


