import pandas as pd
import numpy as np

class Strategy:
	
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
		
	def getInput(self, text, inputType, dealerCard=None, playerCards=None, sumCards=0):
		
		if self.name == "player":
			return self.getRawInput(text)
		else:
			if inputType == "BET":
				return self.inputBet()
			elif inputType == "INSURANCE":
				return self.inputInsurance()
			elif inputType == "ACTION":
				return self.inputAction(dealerCard, playerCards, sumCards)
		## TODO : other cases (AI strategies)
		
		return self.getRawInput(text)
		
	def inputInsurance(self):
		
		return "N"

	def inputAction(self, dealerCardNumber, playerCards, sumCards):
		
		if self.strategyDF is None:
			raise IOError("Strategy file is not loaded.")
		
		## In strategy dataframe:
		## Rows 0-15: hard totals (20 -> 5)
		## Rows 16-24: soft totals (A;9 -> A;A)
		## Rows 25-33: pairs (10;10 -> 2;2)
		
		## Pairs
		if (playerCards[0] == playerCards[1]):
			
			cardIndex = min(playerCards[0],10)
			
			rowNumber = 35 - playerCards[0]
			
			action = Strategy.validateAction(self.strategyDF.iloc[rowNumber][dealerCardNumber])
			return action
		
		## Soft totals
		if (np.product(playerCards) == 0):
			
			cardIndex = max(playerCards[0], playerCards[0])
			cardIndex = min(cardIndex, 10)
			
			rowNumber = 24 - cardIndex
			
			if cardIndex == 10: ## Black Jack, nothing won't be asked anyway
				return "H"
			
			action = Strategy.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber])
			return action
			
		
		## Hard totals
		#~ print "-----------------"
		#~ print 20-sumCards
		#~ print dealerCardNumber
		action = Strategy.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber])
		return action
		
		return "H"
		
	""" Some actions are not always valid, this function validates
	them for the rules in place (to be implemented by hand) """
	@staticmethod
	def validateAction(action):
		
		validatedAction = action
		
		if action == "SU":
			return "H"
			
		## TODO : try to double
		if action == "DH":
			return "H"
			
		if action == "DS":
			return "S"
			
		return validatedAction
			
		
	def inputBet(self):
		
		return "10"
