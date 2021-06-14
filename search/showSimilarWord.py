import difflib

from physics.quantities import quantity

def similarQuantity(word):
	word = difflib.get_close_matches(word, quantity)
	return word

