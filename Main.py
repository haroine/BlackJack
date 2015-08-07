from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy
from Player import Player

players = [Player("Player 1", 1000), Player("Player 2", 1000)]

#~ strategy = Strategy("player")
strategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv")

for i in [5,4,3,2,1]:
	
	print "----",i,"decks"
	
	game1 = BlackJack(players=players, strategy=strategy, lang="French", sleep=0, nRounds=10000, 
					deckNumbers=i, logFile="logDF_10k_"+str(i)+".csv")
	game1.playBlackjack()
