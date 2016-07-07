import turtle
t = turtle.Turtle()
win = turtle.Screen()

t.pu()
t.bk(300)
t.pd()

def tree(length,t):
    if length < 5:
        return None
    else:
        t.forward(length)
        t.right(60)
        tree(length-30,t)
        t.left(120)
        tree(length-30,t)
        t.right(60)
        t.backward(length)

tree(180,t)
