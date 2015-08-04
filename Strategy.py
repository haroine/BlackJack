import pandas as pd

class Strategy:
	
	## TODO : add count
	
	def __init__(self, name="player", strategyFile=None):
		self.name = name
		self.strategyFile = strategyFile
		
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
		
	def getInput(self, text, inputType, dealerCard=None, playerCards=None):
		
		if self.name == "player":
			return self.getRawInput(text)
		else:
			if inputType == "BET":
				return self.inputBet()
			elif inputType == "INSURANCE":
				return self.inputInsurance()
			elif inputType == "ACTION":
				return self.inputAction(dealerCard, playerCards)
		## TODO : other cases (AI strategies)
		
		return self.getRawInput(text)
		
	def inputInsurance(self):
		
		return "N"

	def inputAction(self, dealerCard, playerCards):
		
		## TODO
		
		return "H"
		
	def inputBet(self):
		
		return "10"
