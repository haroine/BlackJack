from Strategy import Strategy
from random import randint

class RandomStrategy(Strategy):

	""" Custom strategy taking Hi-Lo count into account """
	def inputAction(self, dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount):
		
		u = randint(0,3)

		if (u == 0):
			return "H"

		if (u == 1):
			return "S"

		if (u == 2):
			return "D"

		if (u == 3):
			return "P"
		
		return "H"

	def inputBet(self, cardCount=0.):

		return "1"

	def inputInsurance(self):

		return "N"
