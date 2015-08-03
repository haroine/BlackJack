import random

class Deck:
	
	def __init__(self, n=1):
		""" By default, 52-card deck (french deck), shuffled """
		self.size = 52
		self.deck = Deck.init(self, n)
		self.cardNames = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]
		self.colorNames = ["Trefle","Pique","Carreau","Coeur"]
		Deck.shuffle(self)
		
	def __repr__(self):
		return Deck.displayCard(self, self.deck)
		
	def init(self, n=1):
		""" Initialisation of deck list, containing card numbers. n is number
			of decks put together """
		deck = []
		for j in range(0,n):
			for i in range(0,self.size):
				deck.append(i)
			
		return deck

	def shuffle(self):
		""" Shuffles deck """
		random.shuffle(self.deck)
		
	def drawCard(self, n=1):
		""" Draws n card from deck : puts them out of deck list and return list with card numbers """
		if (n > 1):
			listCards = []
			for i in range(n):
				listCards.append(self.deck.pop(0))
			return listCards
		else:
			return self.deck.pop(0)
		
	def displayCard(self, card):
		# TODO : exception if length(cardNames)*length(colorNames) != size
		""" Takes int (id of card) as argument and returns string of card name according to 
			deck parameters (cardNames and colorNames).
			If card is list, display all cards with '\n' between them """
		if(isinstance(card, int)):
			return '{}'.format(self.cardNames[Deck.cardNumber(self, card)]) + " de " + '{}'.format(self.colorNames[Deck.cardColorNumber(self, card)])
		elif(isinstance(card, list)):
			returnString = ""
			for i in range(len(card)):
				returnString += '{}'.format(self.cardNames[Deck.cardNumber(self, card[i])]) + " de " + '{}'.format(self.colorNames[Deck.cardColorNumber(self, card[i])])
				returnString += "\n"
			return returnString
		else:
			return "Unknown type for variable"

	def cardNumber(self, card):
		return card%len(self.cardNames)
		
	def cardColorNumber(self, card):
		return card/len(self.cardNames)
