from Strategy import Strategy

""" Prototype for custom strategy """
class CustomStrategy(Strategy):


	def inputAction(self, dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount):
		
		return super(CustomStrategy, self).inputAction(dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount)

	def inputBet(self, cardCount=0.):

		return super(CustomStrategy, self).inputBet(cardCount)
