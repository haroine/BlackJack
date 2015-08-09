from Strategy import Strategy

class GrossBetStrategy(Strategy):

	def inputBet(self, cardCount=0.):

		bet = 1
		
		if (cardCount >= 16.):
			bet = 20
		elif(cardCount >= 8. and cardCount < 16.):
			bet = 8
		elif(cardCount >= 2. and cardCount < 8.):
			bet = 5

		return str(bet)
