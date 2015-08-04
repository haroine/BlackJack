
class Strategy:
	
	def __init__(self, name="player", strategyFile=None):
		self.name = name
		self.strategyFile = strategyFile
		
	def __repr__(self):
		return 'Name : ' + self.name + ' - File : {}'.format(self.strategyFile)
		
	def	getName(self):
		return self.name
		
	def	getStrategyFile(self):
		return self.strategyFile
		
	def getRawInput(self, text):
		
		return raw_input(text)
		
	## TODO : add question type
	def getInput(self, text):
		
		if self.name == "player":
			return self.getRawInput(text)
		
		## TODO : other cases (AI strategies)
		
		return self.getRawInput(text)
