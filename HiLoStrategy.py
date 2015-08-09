from Strategy import Strategy

class HiLoStrategy(Strategy):

	""" Custom strategy taking Hi-Lo count into account """
	def inputAction(self, dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount):
		
		if (playerCards[0] == playerCards[1]) and (playerCards[1] == 10) and (cardCount >= 5.) and (dealerCardNumber == 4):
			return "P"
			
		if (playerCards[0] == playerCards[1]) and (playerCards[1] == 10) and (cardCount >= 4.) and (dealerCardNumber == 5):
			return "P"
			
		if (sumCards==16) and (dealerCardNumber==0 or dealerCardNumber>=9) and (cardCount >= 0.):
			return "S"
			
		if (sumCards==15) and (dealerCardNumber==0 or dealerCardNumber>=9) and (cardCount >= 4.):
			return "S"
			
		if (sumCards==10) and (dealerCardNumber==0 or dealerCardNumber>=9) and (cardCount >= 4.):
			return "DH"
			
		if (sumCards==10) and (dealerCardNumber==2) and (cardCount >= 2.):
			return "S"
			
		if (sumCards==10) and (dealerCardNumber==1) and (cardCount >= 3.):
			return "S"
			
		if (sumCards==11) and (dealerCardNumber==0) and (cardCount >= 1.):
			return "DH"
			
		if (sumCards==9) and (dealerCardNumber==1) and (cardCount >= 1.):
			return "DH"
			
		if (sumCards==10) and (dealerCardNumber==0) and (cardCount >= 4.):
			return "DH"
						
		if (sumCards==9) and (dealerCardNumber==6) and (cardCount >= 3.):
			return "DH"
			
		if (sumCards==16) and (dealerCardNumber==8) and (cardCount >= 5.):
			return "S"
			
		if (sumCards==13) and (dealerCardNumber==1) and (cardCount >= -1.):
			return "S"
			
		if (sumCards==12) and (dealerCardNumber==3) and (cardCount >= 0.):
			return "S"
			
		if (sumCards==12) and (dealerCardNumber==4) and (cardCount >= -2.):
			return "S"
			
		if (sumCards==12) and (dealerCardNumber==5) and (cardCount >= -1.):
			return "S"
			
		if (sumCards==13) and (dealerCardNumber==4) and (cardCount >= -2.):
			return "S"
		
		return super(HiLoStrategy, self).inputAction(dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount)

	def inputBet(self, cardCount=0.):

		bet = 1
		
		if (cardCount >= 1.):
			bet = int(cardCount)

		return str(bet)
