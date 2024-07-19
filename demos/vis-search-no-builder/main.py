from psychopy import visual, event, core
from random import random

win = visual.Window()
mouse = event.Mouse()

for trials in range(3):

    core.wait(2)

    target = visual.TextStim(win, text="T", pos=(random()-0.5, random()-0.5), autoDraw=True, color='red')

    distractors = []
    for i in range(50):
        distractor = visual.TextStim(win, text="L", pos=(random()-0.5, random()-0.5), autoDraw=True)
        distractors.append(distractor)

    while not mouse.isPressedIn(target):
        win.flip()
    
    for d in distractors:
        d.setAutoDraw(False)
    target.setAutoDraw(False)
    
    win.flip()
    
