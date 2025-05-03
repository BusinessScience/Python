import turtle

from matplotlib.pyplot import pause

window = turtle.Screen()
window.title('The Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

paused = False


def new_turtle(x, y, speed, color, shape, shape_size_w=None, shape_size_l=None):
    obj = turtle.Turtle()
    obj.speed(speed)
    obj.shape(shape)
    obj.color(color)
    obj.penup()
    obj.shapesize(shape_size_w, shape_size_l)
    obj.goto(x, y)
    if shape_size_w is not None and shape_size_l is not None:
        obj.shapesize(shape_size_w, shape_size_l)
    obj.goto(x, y)
    return obj


def paddle_change(which, distance):
    y = which.ycor() + distance
    which.sety(y)


right = new_turtle(350, 0, 0, 'yellow', 'square', 5, 1)
left = new_turtle(-350, 0, 0, 'violet', 'square', 5, 1)
ball = new_turtle(0, 0, 0, 'white', 'circle')

window.listen()
window.onkeypress(lambda: paddle_change(left, 20), 'w')
window.onkeypress(lambda: paddle_change(left, -20), 's')
window.onkeypress(lambda: paddle_change(right, 20), 'Up')
window.onkeypress(lambda: paddle_change(right, -20), 'Down')

window.onkeypress(lambda: globals().__setitem__('paused', False), 'space')

ball.dx = 0.2
ball.dy = -0.2

while True:
    window.update()
    if paused:
        continue

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 390 or ball.xcor() < -390:
        globals().__setitem__('paused', True)
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ((340 < ball.xcor() < 350) and (right.ycor()-40 < ball.ycor() < right.ycor()+40)):
        ball.setx(340)
        ball.dx *= -1

    if ((-340 > ball.xcor() > -350) and (left.ycor()-40 < ball.ycor() < left.ycor()+40)):
        ball.setx(-340)
        ball.dx *= -1
