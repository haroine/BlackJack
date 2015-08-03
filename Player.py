
class Player:
	
	def __init__(self, name, money):
		self.name = name
		self.money = money
		
	def __repr__(self):
		return 'Name : ' + self.name + ' - Money : {}'.format(self.money)
		
	def addMoney(self, amount):
		self.money += amount # amount can be negative
		
	def	getName(self):
		return self.name
		
	def	getMoney(self):
		return self.money
		
