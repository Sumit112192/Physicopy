from quantity import Charge
import numpy as np
import physics.constants
import math
from physics.coordinateSystem import SphericalCoordinatesFromPoint

class ForceBetweenTwoChargedParticles():
		
	
	def getForce(self, onCharge, dueToCharge):
		self.onCharge = onCharge
		self.dueToCharge= dueToCharge

		self.d = np.linalg.norm(self.onCharge.coordinate - self.dueToCharge.coordinate)
		magnitude = (1/(4*math.pi*constants.PERMITTIVITY_OF_FREE_SPACE))*self.onCharge.magnitude*self.dueToCharge.magnitude/(self.d*self.d)
		tempDirection = SphericalCoordinatesFromPoint(self.dueToCharge.coordinate, self.onCharge.coordinate)
		force = (magnitude*math.sin(tempDirection.getTheta())*math.cos(tempDirection.getPhi()), magnitude*math.sin(tempDirection.getTheta())*math.sin(tempDirection.getPhi()), magnitude*math.cos(tempDirection.getTheta()))
		return force
	
q1 = Charge(10, (0,0,0))
q2 = Charge(10, (5,0,0))
print(ForceBetweenTwoChargedParticles().getForce(q1, q2))





