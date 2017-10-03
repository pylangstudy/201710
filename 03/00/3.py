from random import *
import collections
# Six roulette wheel spins (weighted sampling with replacement)
print(choices(['red', 'black', 'green'], [18, 18, 2], k=6))

# Deal 20 cards without replacement from a deck of 52 playing cards
# and determine the proportion of cards with a ten-value
# (a ten, jack, queen, or king).
deck = collections.Counter(tens=16, low_cards=36)
seen = sample(list(deck.elements()), k=20)
print(seen.count('tens') / 20)

# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.
trial = lambda: choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
print(sum(trial() for i in range(10000)) / 10000)

# Probability of the median of 5 samples being in middle two quartiles
trial = lambda : 2500 <= sorted(choices(range(10000), k=5))[2]  < 7500
print(sum(trial() for i in range(10000)) / 10000)

