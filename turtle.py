print("Attention: running only on jupyter-notebook\n\n\n\n\n\n\n\n")
import turtle
from random import choice
#wn = turtle.Screen()
alex= turtle.Turtle()
for i in range(4):
    r_l = choice(['left','right'])
    d = choice(list(range(1, 361)))
    if r_l == 'left':
        alex.left(d)
    else:
        alex.right(d)
    alex.forward(choice(list(range(100, 200))))
turtle.exitonclick()
