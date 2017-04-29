from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy
from Player import Player
import sys
from HiLoStrategy import HiLoStrategy
from TestStrategy import TestStrategy
from RandomStrategy import RandomStrategy

players = [Player("Player 1", 10000),Player("Player 2", 10000)]

## With a small number of decks, python's recursion limit is often
## exceeded.
sys.setrecursionlimit(15000)

customCardNumbers = None
positiveCount = [1,2,3,4,5]
negativeCount = [0,9,10,11,12,13]

human = Strategy("player", negativeCount=negativeCount, positiveCount=positiveCount) ## Play with human input (keyboard)
basicStrategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## Basic strategy
hiLoStrategy = HiLoStrategy(name="custom", strategyFile="strategies/basic_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## Basic strategy with Hi-Lo count
randomFileStrategy = Strategy(name="random", strategyFile="strategies/random_drawn_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount) ## "Random" strategy
testStrategy = TestStrategy(name="test", strategyFile="strategies/basic_strategy.csv", negativeCount=negativeCount, positiveCount=positiveCount)
randomStrategy = RandomStrategy(name="random", negativeCount=negativeCount, positiveCount=positiveCount)

strategyList = [basicStrategy, randomStrategy]



game1 = BlackJack(players=players, strategyList=strategyList, lang="French", sleep=0, nRounds=1000, 
				deckNumbers=1, logFile="data/test_custom_deck.csv", 
				customCardNumbers=customCardNumbers, negativeCount=negativeCount, positiveCount=positiveCount)


game2 = BlackJack(players=[Player("Player 1", 10000)], strategyList=[randomStrategy], lang="French", sleep=0, nRounds=10000, 
				deckNumbers=6, logFile="data/random_1_player.csv", 
				customCardNumbers=customCardNumbers, negativeCount=negativeCount, positiveCount=positiveCount)

gameHuman = BlackJack(players=[Player("Player 1", 10000)], strategyList=[human], lang="French", sleep=0, nRounds=10000, 
				deckNumbers=1, logFile="data/human_game_log.csv", 
				customCardNumbers=customCardNumbers, negativeCount=negativeCount, positiveCount=positiveCount)

game2.playBlackjack()
