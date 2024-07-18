import random
for i in range(10):
    # Make a list called `cats` containing the filenames.
    cats = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg']

    # Shuffle the list
    import random
    shuffled_cats = cats.copy()
    attempt = 0
    while shuffled_cats == cats:
        attempt = attempt + 1
        random.shuffle(cats)
        print(attempt, cats)
        print(" ")