import random

# Make a list called `cats` containing the filenames.
original_cats = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg']

# Make copies of the original_cats list, not shuffled yet
shuffled_cats = original_cats.copy()

# To start with, both copies are the same because we haven't shuffled yet.
print("starting values: ", shuffled_cats)

# Sat that we are on the first attempt
attempt = 0
# so, next, we say:
# While both copies are the same, keep shuffling
while True:
  if attempt == 0:
    print("attempt ", attempt, ": ", shuffled_cats)
  while shuffled_cats == original_cats:
    attempt = attempt + 1
    random.shuffle(shuffled_cats)
    print("attempt ", attempt, ": ", shuffled_cats)
  break