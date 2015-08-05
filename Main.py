from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy
from Player import Player

players = [Player("Player 1", 1000), Player("Player 2", 1000)]

#~ strategy = Strategy("player")
strategy = Strategy(name="basic", strategyFile="strategies/basic_strategy.csv")

game1 = BlackJack(players=players, strategy=strategy, lang="French", sleep=0)
game1.playBlackjack()
