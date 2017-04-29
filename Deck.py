import random

class Deck:
	
	def __init__(self, n=1, lang="French", size=52, customCardNumbers=None):
		""" By default, 52-card deck (french deck), shuffled """
		self.lang = lang

		self.size = size
		self.deck = Deck.init(self, n)
		
		if lang=="English":
			self.cardNames = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
			self.colorNames = ["Clubs","Spades","Diamonds","Hearts"]
		else:
			self.cardNames = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]
			self.colorNames = ["Trefle","Pique","Carreau","Coeur"]	
		
		Deck.shuffle(self)

		if customCardNumbers is not None:
			selectedDeck = []

			for card in self.deck:
				if self.cardNumber(card) in customCardNumbers:
					selectedDeck.extend([card])
			self.deck = selectedDeck
		
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
		
	""" Takes int (id of card) as argument and returns string of card name according to 
	deck parameters (cardNames and colorNames).
	If card is list, display all cards with '\n' between them """
	def displayCard(self, card):
		# TODO : exception if length(cardNames)*length(colorNames) != size
		
		smallWord = " de "
		
		if self.lang == "English":
			smallWord = " of "

		if(isinstance(card, int)):
			return '{}'.format(self.cardNames[Deck.cardNumber(self, card)]) + smallWord + '{}'.format(self.colorNames[Deck.cardColorNumber(self, card)])
		elif(isinstance(card, list)):
			returnString = ""
			for i in range(len(card)):
				returnString += '{}'.format(self.cardNames[Deck.cardNumber(self, card[i])]) + smallWord + '{}'.format(self.colorNames[Deck.cardColorNumber(self, card[i])])
				returnString += "\n"
			return returnString
		else:
			return "Unknown type for variable"

	def cardNumber(self, card):
		return card%len(self.cardNames)
		
	def cardColorNumber(self, card):
		return card/len(self.cardNames)
		
	def cardNumberList(self, cardList):
		
		if len(cardList) > 1:
			
			returnList = [-1]*len(cardList)
			
			for i, card in enumerate(cardList):
				returnList[i] = self.cardNumber(card)
				
			return returnList
		else:
			return self.cardNumber(cardList[0])
			
	def cardNamesList(self, cardList):
		
		cardList = self.cardNumberList(cardList)
		
		returnList = []
		
		for i, card in enumerate(cardList):
			
			returnList.append(self.cardNames[card])
			
		return returnList
