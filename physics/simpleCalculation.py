import numpy as np
def distanceBetweenPoints(point1, point2):
	return np.linalg.norm(np.array(point1) - np.array(point2))