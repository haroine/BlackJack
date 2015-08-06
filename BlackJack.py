from Player import Player
from Deck import Deck
from Strategy import Strategy
import copy
import time
import pandas as pd
import numpy as np

class BlackJack:
	
	# TODO constructors with list of players and deck as parameter
	def __init__(self, players, strategy=Strategy("player"), deckNumbers=6, lang="French", sleep=0, nRounds=1000):
		self.deck = Deck(deckNumbers, lang)
		self.players = players
		self.strategy = strategy
		self.sleep = sleep
		self.deckNumbers = deckNumbers
		self.lang = lang
		self.verbose = False
		self.nRounds = nRounds
		self.currentRoundNumber = 0
		
		columnsLog = ['dealerCardNumber','dealerCardName']
		
		for i, player in enumerate(self.players):
			playerNumber = str(i+1)
			columnsLog.extend(['money_player'+playerNumber,'bet_player'+playerNumber,'cards_player'+playerNumber,
								'cardsNumber_player'+playerNumber,'actions_player'+playerNumber])
								
		columnsLog.extend(['dealerCards','dealerCardsNames','nCardsInDeck'])
		
		self.logDF = pd.DataFrame(columns=columnsLog)
		
		if self.strategy.name == "player":
			self.verbose = True
	
	def setDeck(self, newDeck):
		self.deck = newDeck
	
	def sumCards(self, listCards, ace1=False, ace11=False):
		""" returns sum of the cards, counted following the blackjack rules """
		returnSum = 0
		
		for i in range(len(listCards)):
			cardNumber = self.deck.cardNumber(listCards[i])
			if(cardNumber >= 1 and cardNumber <= 9):
				returnSum += cardNumber+1
			elif(cardNumber >= 10 and cardNumber <= 12):
				returnSum += 10
			elif(cardNumber == 0): # Ace counting
				if(ace1):
					returnSum += 1
				elif(ace11):
					returnSum += 11
				else:
					if(BlackJack.isBetterSum(self, BlackJack.sumCards(self, listCards, True, False), BlackJack.sumCards(self, listCards, False, True))):
						returnSum +=1
					else:
						returnSum += 11
			else:
				print "Unknown card"
				return 0
		
		return returnSum
		
	def isBetterSum(self, s1, s2):
		""" Returns true if s1 beats or ties s2, false if s2 strictly beats s1 """
		if(s2 > 21):
			return True
		else:
			if(s1 > 21):
				return False
			else:
				if(s2 > s1):
					return False
				else:
					return True
		
		return True
		
	def displayPlayerCards(self, playerCards, n=-1):
		returnString = ""
		if(n >= len(self.players) or n < 0):
			for i in range(len(self.players)):
				returnString += self.players[i].getName() + " Cards (Total points {}) :".format(BlackJack.sumCards(self, playerCards[i]))
				returnString += "\n" + self.deck.displayCard(playerCards[i])
		else:
			returnString += self.players[n].getName() + " Cards (Total points {}) :\n".format(BlackJack.sumCards(self, playerCards[n]))
			returnString += self.deck.displayCard(playerCards[n])
			
		return returnString
		
	def displayDealerCards(self, dealerCards, show=False):
		returnString = ""
		returnString += "\nDealer Cards :"
		returnString += "\n" + self.deck.displayCard(dealerCards[0])
		if(show):
			for i in range(1,len(dealerCards)):
				returnString += "\n" + self.deck.displayCard(dealerCards[i])
			returnString += "\n------ Total points : {} \n".format(BlackJack.sumCards(self, dealerCards))
		else:
			returnString += "\n********** \n"
			
		return returnString
		
	""" Number of cards needed for one round """
	def cardsNeeded(self):

		return 4*(len(self.players)+1)
	
	""" True if there are more than cardsNeeded(self) cards left in deck """
	def enoughCardsLeft(self):

		if(len(self.deck.deck) >= BlackJack.cardsNeeded(self)):
			return True
		else:
			return False
		
	def hasBlackJack(self, listCards):
		if(len(listCards) == 2 and BlackJack.sumCards(self, listCards) == 21):
			return True
		else:
			return False
		return False

	def doubleIsValid(self, playerCards):
		# TODO : modify to comply to different casino rules

		if(len(playerCards) == 2):
			return True
		else:
			return False
			
	def splitIsValid(self, playerCards, playerSplit):
		
		if (len(playerCards) == 2 ):
			if(( self.deck.cardNumber(playerCards[0]) == self.deck.cardNumber(playerCards[1]) ) and ( not playerSplit )):
				return True
		
		return False
 
	def results(self, dealerCards, playerCards, bets, insurancesList):
		
		verbose = self.verbose
		
		if verbose:
			print "########## Round results ############"
			
		dealerBlackJack = BlackJack.hasBlackJack(self, dealerCards)
		dealerPoints = BlackJack.sumCards(self, dealerCards)
		playersPoints = []
		# Players points and players blackjacks
		for i in range(len(self.players)):
			playersPoints.append(BlackJack.sumCards(self, playerCards[i]))
		playersBlackJack = []
		for i in range(len(self.players)):
			playersBlackJack.append(BlackJack.hasBlackJack(self, playerCards[i]))
		
		## addMoney and print results
		if verbose:
			print "Dealer, total points : {}".format(dealerPoints)
			if(dealerBlackJack):
				print "Black Jack !"
			
		for i in range(len(self.players)):
			
			if verbose:
				print self.players[i].getName() + " , total points : {}".format(playersPoints[i])
				if(playersBlackJack[i]):
					print "Black Jack !"
				
			# Who wins + money earned
			
			win = 0
			if(playersPoints[i] > 21):
				if verbose:
					print "Busted."
				win = -bets[i]
			else:
				if(dealerPoints > 21):
					if verbose:
						print "Dealer is busted."
					win = bets[i]
					if(playersBlackJack[i]):
						if verbose:
							print "Black Jack pays 3:2"
						win = 1.5*bets[i]
				else:
					if(playersPoints[i] > dealerPoints):
						if verbose:
							print "Dealer pays."
						if(not playersBlackJack[i]):
							win = bets[i]
						else:
							if verbose:
								print "Black Jack pays 3:2"
							win = 1.5*bets[i]
					elif(playersPoints[i] < dealerPoints):
						if verbose:
							print "Dealer wins."
						win = -bets[i]
					else:
						if(not playersBlackJack[i] and not dealerBlackJack):
							if verbose:
								print "Tie."
							win = 0
						else:
							if(dealerBlackJack and playersBlackJack[i]):
								if verbose:
									print "Tie."
								win = 0
								# TODO : in this case, dealers pays player's BlackJack ?
							elif(dealerBlackJack and not playersBlackJack[i]):
								if verbose:
									print "Dealer has Black Jack. Dealer wins."
								win = -bets[i]
							elif(playersBlackJack[i] and not dealerBlackJack):
								if verbose:
									print "Player has Black Jack. Dealer pays 3:2."
								win = 1.5*bets[i]
							else:
								if verbose:
									print "Tie."
								win = 0
								
			## TODO : pay insurance or not
			if insurancesList[i]:
				if dealerBlackJack:
					if verbose:
						print "Insurance was taken, and dealer had a BlackJack !"
					win += bets[i]
				else:
					if verbose:
						print "Insurance was taken, but dealer didn't have a BlackJack !"
					win -= 0.5*bets[i]
			
			if (win >= 0):
				if verbose:
					print "Wins : {}".format(win)
			else:
				if verbose:
					print "Loses : {}".format(-win)
				
			self.players[i].addMoney(win)

	""" -------- Play BlackJack ! -------- """
	def playBlackjack(self):
		
		verbose = self.verbose
		defaultBet = 10
		
		keepPlaying = True
		while (keepPlaying):
			
			self.currentRoundNumber += 1
			
			print self.currentRoundNumber
			
			if self.currentRoundNumber > self.nRounds :
				self.logDF.to_csv("logDF.csv")
				return 0
			
			self.logDF.loc[self.currentRoundNumber] = np.nan
			
			if self.sleep > 0:
				time.sleep(self.sleep)
				
			if verbose:
				print "--- New Round ----"
				
			self.logDF['nCardsInDeck'][self.currentRoundNumber] = len(self.deck.deck)
			
			## playersSplit2 is extended if a player splits, while playersSplit
			## will always have len(self.players) elements
			playersSplit = [False]*len(self.players)
			playersSplit2 = [False]*len(self.players) 
			insurancesList = [False]*len(self.players)
			
			### Display Players (and eject those who haven't enough money left) :
			
			
			
			playersToEject = []
			for i in range(len(self.players)):
				if(self.players[i].getMoney() > 0):
					if verbose:
						print self.players[i]
						
					self.logDF['money_player'+str(i+1)][self.currentRoundNumber] = self.players[i].getMoney()
				else:
					if verbose:
						print self.players[i].getName() + " has no money left."
						print self.players[i].getName() + " is out of the game !"
					playersToEject.append(i)
			
			if(len(playersToEject) > 0):
				for i in range(len(playersToEject)):
					self.players.pop(playersToEject[i])
					
			if(len(self.players) < 1):
				print "No more players."
				return 0
			
			### Ask for bets
			bets = []
			for i in range(len(self.players)):
				keepAsking = True
				while (keepAsking):
					
					questionText = ""
					if verbose:
						questionText = self.players[i].getName() + ", what is your bet (10) ? "
						
					inputBet = self.strategy.getInput(questionText, "BET")
					
					## Default bet
					if inputBet == "":
						inputBet = defaultBet
					
					try:
						currentBet = int(inputBet)
						if (currentBet <= self.players[i].getMoney()):
							keepAsking = False
							bets.append(currentBet)
						else:
							print "You dont have enough money to place this bet !"
					except ValueError:
					   print "Not a valid bet !"
			
			### Give cards to players + to dealer
			dealerCards = self.deck.drawCard(2)
			
			if verbose:
				print BlackJack.displayDealerCards(self, dealerCards)
				
			dealerCardNumber = self.deck.cardNumber(dealerCards[0])
			self.logDF['dealerCardNumber'][self.currentRoundNumber] = dealerCardNumber
			self.logDF['dealerCardName'][self.currentRoundNumber] = self.deck.cardNames[dealerCardNumber]
			
			playerCards = []
			for i in range(len(self.players)):
				cards = self.deck.drawCard(2)
				playerCards.append(cards)
				
			if verbose:
				print BlackJack.displayPlayerCards(self, playerCards)
			
			### If dealer has Ace, player can choose insurance
			if(self.deck.cardNumber(dealerCards[0]) == 0):
				for i in range(len(self.players)):
					
					questionText = ""
					if verbose:
						questionText = self.players[i].getName() + ", do you want the insurance Y/N (N) ?"
						
					playerAction = self.strategy.getInput(questionText, "INSURANCE")
			
					if playerAction == "Y":
						insurancesList[i] = True
						
			
			### Ask for players' actions
			i = 0 ## i counts the number of players (including splits)
			j = 0 ## j counts the number of original players
			cont = True
			playersBackup = copy.deepcopy(self.players)
			playersActions = []
			#~ for i in range(len(self.players)):
			while cont:
				

				
				keepAsking = True
				playerActionList = []
				while (keepAsking):
					
					#~ print "-------------------",i
					#~ print "------jjjjj--------",j

					noaction = ""
					finalPlayerAction = noaction
					
					if (BlackJack.sumCards(self, playerCards[i]) >= 21):
							if verbose:
								print "You cannot ask for a card anymore" # TODO : better text here
							keepAsking = False
							
					else:
						
						questionText = ""
						
						if verbose:
							splitString = ""
							
							print BlackJack.displayPlayerCards(self, playerCards, i)
							
							if(self.splitIsValid(playerCards[i], playersSplit2[i])):
								splitString = "to split (P),"
							
							if(BlackJack.doubleIsValid(self, playerCards[i])):
								stringInput = ", do you want "+splitString+" to hit (H), to stay (S) or to double (D) ? "
							else:
								stringInput = ", do you want "+splitString+" to hit (H) or to stay (S) ? "
								
							questionText = self.players[i].getName() + stringInput

						#~ playerAction = raw_input(self.players[i].getName() + stringInput)
						playerAction = self.strategy.getInput(questionText, "ACTION",
										self.deck.cardNumber(dealerCards[0]), self.deck.cardNumberList(playerCards[i]), BlackJack.sumCards(self, playerCards[i]),
										BlackJack.doubleIsValid(self, playerCards[i]), self.splitIsValid(playerCards[i], playersSplit2[i]))
						
						finalPlayerAction = playerAction
						
						if(playerAction == "H"):
							if (BlackJack.sumCards(self, playerCards[i]) >= 21):
								if verbose:
									print "You cannot ask for a card anymore" # TODO : better text here
								keepAsking = False
								finalPlayerAction = noaction
							else:
								playerCards[i].append(self.deck.drawCard())
								if verbose:
									print BlackJack.displayPlayerCards(self, playerCards, i)
						elif(playerAction == "D"):
							if(BlackJack.doubleIsValid(self, playerCards[i])):
								if verbose:
									print "Your bet has been doubled."
								bets[i] = 2*bets[i]
								playerCards[i].append(self.deck.drawCard())
								if verbose:
									print BlackJack.displayPlayerCards(self, playerCards, i)
									print "You've chose to Double, you cannot ask for a card anymore"
								keepAsking = False
							else:
								finalPlayerAction = noaction
								if verbose:
									print "You can't double in this situation."
						elif(playerAction == "S"):
							keepAsking = False
						elif(playerAction == "P"):
							if(self.splitIsValid(playerCards[i], playersSplit2[i])):
								
								playersSplit[j] = True
								playersSplit2[i] = True
								
								self.players.insert(i+1,copy.copy(self.players[i]))
								self.players[i].name = self.players[i].name + " - hand #1"
								self.players[i+1].name = self.players[i+1].name + " - hand #2"
								
								splittedCard = playerCards[i][1]
								playerCards[i] = [playerCards[i][0], self.deck.drawCard()]
								
								playerCards.insert(i+1, [splittedCard, self.deck.drawCard()])
								
								bets.insert(i+1, bets[i])
								insurancesList.insert(i+1, insurancesList[i])
								playersSplit2.insert(i+1, playersSplit2[i])
								
								## j will be incremented twice at the end of the loop, so decrementing here
								## makes it equal to the number of *real* players 
								j = j-1
								
								#~ print self.players
								#~ print playerCards
								#~ print bets
								#~ print BlackJack.displayPlayerCards(self, playerCards, i)
								
							else:
								finalPlayerAction = noaction
								print "Cannot split here."
						else:
							print "Not a valid choice."
							
					playerActionList.extend(finalPlayerAction)
					print "--------------",finalPlayerAction
						
					if len(playerActionList) < 1:
						playerActionList = [noaction]
						
					playersActions.append(playerActionList)
							
				i = i+1
				j = j+1
				
				if (i >= len(self.players)):
					cont = False
					
			### Make dealer draw or stay
			keepDrawing = True
			while (keepDrawing):
				if verbose:
					print BlackJack.displayDealerCards(self, dealerCards, True) # Show Dealer cards
					
				if(BlackJack.sumCards(self, dealerCards) <= 16):
					if verbose:
						print "Dealer draws"
					dealerCards.append(self.deck.drawCard())
				else:
					if verbose:
						print "Dealer stands"
					keepDrawing = False
			
			### Display win or lose and addMoney
			BlackJack.results(self, dealerCards, playerCards, bets, insurancesList)
			
			self.logDF['dealerCards'][self.currentRoundNumber] = str(dealerCards).strip('[]')
			self.logDF['dealerCardsNames'][self.currentRoundNumber] = str(self.deck.cardNamesList(dealerCards)).strip('[]')

			
			## TODO : correct amount of money for players who splitted
			print playersActions
			k = 0
			for i in range(len(playersBackup)):
				cardsPlayer = playerCards[i]
				
				## When players are given cards that don't call for action
				## (e.g. Black Jack), actionsPlayer can be non existent
				try:
					actionsPlayer = playersActions[i]
				except:
					actionsPlayer = ""
				if playersSplit[i]:
					moneyWithSplitResult = self.players[k].money + self.players[k+1].money - playersBackup[i].money
					#~ print "with split result : ", moneyWithSplitResult
					playersBackup[i].money = moneyWithSplitResult
					k = k+1
					cardsPlayer.extend(playerCards[k])
					actionsPlayer.extend(playersActions[k])
				else:
					playersBackup[i].money = self.players[k].money
					
				self.logDF['cards_player'+str(i+1)][self.currentRoundNumber] = str(cardsPlayer).strip('[]')
				self.logDF['cardsNumber_player'+str(i+1)][self.currentRoundNumber] = str(self.deck.cardNamesList(cardsPlayer)).strip('[]')
				self.logDF['bet_player'+str(i+1)][self.currentRoundNumber] = bets[i]

				#~ print actionsPlayer
				try:
					self.logDF['actions_player'+str(i+1)][self.currentRoundNumber] = str(actionsPlayer).strip('[]')
				except:					
					## When players are given cards that don't call for action
					## (e.g. Black Jack), actionsPlayer can be non existent
					pass
					
				k = k+1

			
			self.players = playersBackup
			
			### If there are enough cards left in deck, continue, else stop
			if(not BlackJack.enoughCardsLeft(self)):
				print "No more cards left in deck. Cards will be shuffled."
				keepPlaying = False
				self.deck = Deck(self.deckNumbers, self.lang)
				
				#~ try:
					#~ BlackJack.playBlackjack(self)
				#~ except:
					#~ print "End of game"
					#~ print self.deck
					#~ return 0
					
				self.playBlackjack()
