from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy
from Player import Player
import sys
from HiLoStrategy import HiLoStrategy

players = [Player("Player 1", 10000),Player("Player 2", 10000)]

## With a small number of decks, python's recursion limit is often
## exceeded.
sys.setrecursionlimit(15000)

customCardNumbers = None
positiveCount = [9,10,11,12]
negativeCount = [1,2,3,4,5]

human = Strategy("player") ## Play with human input (keyboard)
basicStrategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## Basic strategy
hiLoStrategy = HiLoStrategy(name="custom", strategyFile="strategies/basic_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## Basic strategy with Hi-Lo count
randomStrategy = Strategy(name="random", strategyFile="strategies/randomStrategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## "Random" strategy

strategyList = [hiLoStrategy, randomStrategy]



game1 = BlackJack(players=players, strategyList=strategyList, lang="French", sleep=0, nRounds=1000, 
				deckNumbers=6, logFile="data/test_custom_deck.csv", 
				customCardNumbers=customCardNumbers, negativeCount=negativeCount, positiveCount=positiveCount)

game1.playBlackjack()
