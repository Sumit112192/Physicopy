import math
from fractions import Fraction
def convertToMultipleOfPi(number):
	multiple = number/math.pi
	multiple = Fraction(multiple)
	if(multiple.numerator<10 and multiple.denominator<10):
		return multiple
	return number
