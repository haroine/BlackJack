from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy

#~ strategy = Strategy("default")
strategy = Strategy("basic", strategyFile="strategies/basic_strategy.csv")

game1 = BlackJack(strategy=strategy, lang="French", sleep=0)
game1.playBlackjack()
