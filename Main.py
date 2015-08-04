from Deck import Deck
from BlackJack import BlackJack
from Strategy import Strategy

#deck = Deck(2)
#print deck

strategy = Strategy("default")

game1 = BlackJack(strategy=strategy, lang="French")
game1.playBlackjack()
