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

human = Strategy("player") ## Play with human input (keyboard)
basicStrategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv") ## Basic strategy
hiLoStrategy = HiLoStrategy(name="custom", strategyFile="strategies/basic_strategy.csv") ## Basic strategy with Hi-Lo count
randomStrategy = Strategy(name="basic", strategyFile="strategies/randomStrategy.csv") ## "Random" strategy

strategyList = [basicStrategy, randomStrategy]

game1 = BlackJack(players=players, strategyList=strategyList, lang="French", sleep=0, nRounds=10000, 
				deckNumbers=6, logFile="logDF_test_2_strategies.csv")

game1.playBlackjack()
