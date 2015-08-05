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
		
	def getInput(self, text, inputType, dealerCard=None, playerCards=None, sumCards=0, doubleIsValid=True, splitIsValid=False):
		
		if self.name == "player":
			return self.getRawInput(text)
		else:
			if inputType == "BET":
				return self.inputBet()
			elif inputType == "INSURANCE":
				return self.inputInsurance()
			elif inputType == "ACTION":
				return self.inputAction(dealerCard, playerCards, sumCards, doubleIsValid, splitIsValid)
		## TODO : other cases (AI strategies)
		
		return self.getRawInput(text)
		
	def inputInsurance(self):
		
		return "N"

	def inputAction(self, dealerCardNumber, playerCards, sumCards, doubleIsValid, splitIsValid):
		
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
			
			action = Strategy.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber], doubleIsValid, splitIsValid)
			return action
			
		## Pairs
		if (playerCards[0] == playerCards[1]):
			
			cardIndex = min(playerCards[0],10)
			
			rowNumber = 35 - playerCards[0]
			
			print rowNumber
			print dealerCardNumber
			action = Strategy.validateAction(self.strategyDF.iloc[rowNumber][dealerCardNumber], doubleIsValid, splitIsValid)
			return action
		
		## Hard totals
		action = Strategy.validateAction(self.strategyDF.iloc[20-sumCards][dealerCardNumber], doubleIsValid, splitIsValid)
		return action
		
		return "H"
		
	""" Some actions are not always valid, this function validates
	them for the rules in place (to be implemented by hand) """
	@staticmethod
	def validateAction(action, doubleIsValid, splitIsValid):
		
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
			
		return validatedAction
			
		
	def inputBet(self):
		
		return "1"
