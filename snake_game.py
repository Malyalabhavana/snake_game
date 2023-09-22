import turtle
import time
import random

#screen
wn = turtle.Screen()
wn.title("snake Game")
wn.bgcolor("forestgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake Headr
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction="stop"

#apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(0, 100)

#score board
sc = turtle.Turtle()
sc.speed(0)
sc.shape("circle")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0 High Score: 0" , align="center" , font=("consolas", 24, "bold"))

delay = 0.1
segments=[]

#score
score=0
highScore=0

def goUp():
    if head.direction != "down":
        head.direction = "up"
def goDown():
    if head.direction != "up":
        head.direction = "down"
def goLeft():
    if head.direction != "right":
        head.direction = "left"
def goRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

#keyboard
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goLeft, "a")
wn.onkeypress(goDown, "s")
wn.onkeypress(goRight, "d")

while True:
    wn.update()
    move()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    if head.distance(apple)<20:
        x= random.randint(-280, 280)
        y= random.randint(-280, 280)
        apple.goto(x, y)

        score+=1
        delay-= 0.001

        #new
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        if score > highScore:
            highScore = score
        sc.clear()
        sc.write("score: {} High Score: {}".format(score, highScore), align="center", font=("consolas", 24, "bold"))

   

    #collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction="stop"


            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score=0
            delay=0.1

        #score
            sc.clear()
            sc.write("score: {} High Score: {}".format(score, highScore), align="center", font=("consolas", 24, "bold"))

     #add new body
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x, y)
    #move segment
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].gotor(x, y)


    time.sleep(delay)
wn.mainloop()





