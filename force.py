from quantity import Charge
import numpy as np
import constants
import math

class ForceBetweenTwoChargedParticles():
		
	
	def getForce(self, onCharge, dueToCharge):
		self.onCharge = onCharge
		self.dueToCharge= dueToCharge

		self.d = np.linalg.norm(self.onCharge.coordinate - self.dueToCharge.coordinate)
		magnitude = (1/(4*math.pi*constants.PERMITTIVITY_OF_FREE_SPACE))*self.onCharge.magnitude*self.dueToCharge.magnitude/(self.d*self.d)
		return magnitude
	





