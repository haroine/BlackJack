import pandas as pd
import numpy as np
from Deck import Deck

class Strategy(object):
	
	## TODO : add count
	
	def __init__(self, name="player", strategyFile=None):
		self.name = name
		self.strategyFile = strategyFile
		self.strategyDF = None
		
		if strategyFile is not None:
			self.strategyDF = pd.DataFrame.from_csv(strategyFile)
		
	def __repr__(self):
		return 'Name : ' + self.name + ' - File : {}'.format(self.strategyFile)
		
	def	getName(self):
		return self.name
		
	def	getStrategyFile(self):
		return self.strategyFile
		
	def getRawInput(self, text):
		
		return raw_input(text)
		
	def getInput(self, text, inputType, dealerCard=None, playerCards=None, sumCards=0, doubleIsValid=True
				, splitIsValid=False, cardCount=0.):
		
		if self.name == "player":
			return self.getRawInput(text)
		else:
			if inputType == "BET":
				return self.inputBet(cardCount=cardCount)
			elif inputType == "INSURANCE":
				return self.inputInsurance()
			elif inputType == "ACTION":
				return self.inputAction(dealerCard, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount)
		## TODO : other cases (AI strategies)
		
		return self.getRawInput(text)
		
	""" Most strategies recommend not to take the insurance """
	def inputInsurance(self):
		
		return "N"
		
	""" Implements card counting (hi-lo method) """
	def cardCount(self, deck, dealerCards, playerCards):
		
		cardCount = 0
		
		for cardNumber in deck.cardNumberList(dealerCards):
			
			if (cardNumber == 0) or (cardNumber >= 9):
				cardCount -= 1
				continue
				
			if (cardNumber >= 1) and (cardNumber <= 5):
				cardCount += 1
				continue
				
			## cards in [6,8] do not increment count
				
		for i in range(len(playerCards)):
			for cardNumber in deck.cardNumberList(playerCards[i]):
				
				if (cardNumber == 0) or (cardNumber >= 9):
					cardCount -= 1
					continue
					
				if (cardNumber >= 1) and (cardNumber <= 5):
					cardCount += 1
					continue
					
				## cards in [6,8] do not increment count

		return cardCount

	def inputAction(self, dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid, cardCount=0.):
		
		if self.strategyDF is None:
			raise IOError("Strategy file is not loaded.")
		
		## In strategy dataframe:
		## Rows 0-15: hard totals (20 -> 5)
		## Rows 16-24: soft totals (A;9 -> A;A)
		## Rows 25-33: pairs (10;10 -> 2;2)
		
		## Soft totals
		if (np.product(playerCards) == 0):
			
			cardIndex = max(playerCards[0], playerCards[0])
			cardIndex = min(cardIndex, 10)
			
			rowNumber = 24 - cardIndex
			
			if cardIndex == 10: ## Black Jack, nothing won't be asked anyway
				return "H"
			
			action = self.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber], doubleIsValid, splitIsValid, 
											sumCards, dealerCardNumber)
			return action
			
		## Pairs
		if (playerCards[0] == playerCards[1]):
			
			cardIndex = min(playerCards[0],10)
			
			rowNumber = 34 - playerCards[0]
			
			action = self.validateAction(self.strategyDF.iloc[rowNumber][dealerCardNumber], doubleIsValid, splitIsValid, 
											sumCards, dealerCardNumber)
			return action
		
		## Hard totals
		action = self.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber], doubleIsValid, splitIsValid, 
										sumCards, dealerCardNumber)
		return action
		
		return "H"
		
	""" Some actions are not always valid, this function validates
	them for the rules in place (to be implemented by hand) """
	def validateAction(self, action, doubleIsValid, splitIsValid, sumCards, dealerCardNumber, cardCount=0.):
		
		validatedAction = action
		
		## Surrender is illegal for now
		if action == "SU":
			return "H"
			
		if action == "DH":
			if doubleIsValid:
				return "D"
			else:
				return "H"
			
		if action == "DS":
			if doubleIsValid:
				return "D"
			else:
				return "S"
				
		## If split is not valid, get action from same hard total
		if action=="P":
			if splitIsValid:
				return "P"
			else:
				return self.inputAction(dealerCardNumber, [3,4], sumCards, doubleIsValid, splitIsValid, cardCount)
			
		return validatedAction
			
		
	def inputBet(self, cardCount=0.):
		
		return "1"
