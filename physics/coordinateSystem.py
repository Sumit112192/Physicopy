import numpy as np
import math
from physics.simpleCalculation import distanceBetweenPoints
from physics.approximate import convertToMultipleOfPi

class SphericalCoordinatesFromPoint():
	def __init__(self, coordinate2, coordinate1 = (0, 0, 0)):
		self.coordinate1 = coordinate1
		self.coordinate2 = coordinate2
	def getR(self):
		return distanceBetweenPoints(self.coordinate1, self.coordinate2)
	def getTheta(self):
		if self.getR()!=0:
			return math.acos((self.coordinate2[2] - self.coordinate1[2])/self.getR())
		else:
			return 0
	def getPhi(self):
		if(self.coordinate2[0] - self.coordinate1[0] == 0):
			if(self.coordinate2[1]>self.coordinate1[1]):
				return math.pi
			elif(self.coordinate2[1]==self.coordinate1[1]):
				return 0
			else:
				return -math.pi
		return math.atan((self.coordinate2[1] - self.coordinate1[1])/(self.coordinate2[0] - self.coordinate1[0]))
