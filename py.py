from turtle import *
from random import random
bgcolor('black')
color('cyan')
for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    right(angle)
    fd(steps)
    left(1)
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")