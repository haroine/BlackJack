from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy

#deck = Deck(2)
#print deck

#~ strategy = Strategy("default")
strategy = Strategy("basic", strategyFile="strategies/basic_strategy.csv")

game1 = BlackJack(strategy=strategy, lang="French", sleep=1)
game1.playBlackjack()
