import random

# Make a list called `cats` containing the filenames.
cats = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg']

# Make a copy of the cats list
shuffled_cats = cats.copy()

# If the shuffled list is the same as the original list 
# then shuffle the original list
while shuffled_cats == cats:
  random.shuffle(cats)
  print(cats)