from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy
from Player import Player
import sys
from HiLoStrategy import HiLoStrategy

players = [Player("Player 1", 10000)]

sys.setrecursionlimit(15000)
#~ strategy = Strategy("player") ## Play with human input (keyboard)
#~ strategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv") ## Basic strategy
hiLoStrategy = HiLoStrategy(name="custom", strategyFile="strategies/basic_strategy.csv") ## Basic strategy with Hi-Lo count
#~ randomStrategy = Strategy(name="basic", strategyFile="strategies/randomStrategy.csv") ## Random strategy

game1 = BlackJack(players=players, strategy=hiLoStrategy, lang="French", sleep=0, nRounds=10000, 
				deckNumbers=6, logFile="logDF_analysis_hilo.csv")

game1.playBlackjack()
