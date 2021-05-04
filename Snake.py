# Simple Snake Game in Python 3 for Beginners
# By @Amey tripathi

import turtle
import time
import random
import pygame

pygame.init()

main_sound = pygame.mixer.Sound("game_over.ogg")
pygame.mixer.music.load("date.ogg")

delay = 0.07

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Amey Tripathi")
wn.bgcolor("green")
wn.setup(width=1920, height=1080)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

# pencil
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('circle')
pencil.color("white")
pencil.penup()
pencil.hideturtle()
pencil.goto(10, 389)
pencil.write("-------------------------<<<<<<<Pass Here To Increase Speed By +0.05 + RESTORE POINT>>>>>>>------------------------",
             align ="center", font=("Castellar", 18, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

def main() :
    if (pygame.mixer.music.play()):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.stop(main_sound)

# Global Start
pygame.mixer.music.play(-1)


while True:
    wn.update()

    # Music for restart
    if head.xcor () > 0 or head.ycor () > 0 or head.xcor () < 0 or head.ycor () < 0:
        pygame.mixer.music.unpause()

    # Music With border
    if head.xcor () > 935 or head.xcor () < -940 or head.ycor () > 490 or head.ycor () < -500:
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(main_sound)

    # Pass from pass here...
    if head.xcor() > 1000 or head.xcor() < -1000 or head.ycor() > 389 or head.ycor() < -1000:
        head.goto(0, -449)
        head.direction = "up"
        delay = 0.04

    # Check for a collision with the border
    if head.xcor () > 935 or head.xcor () < -940 or head.ycor () > 490 or head.ycor () < -500:
        time.sleep (4)
        head.goto (0, 0)
        head.direction = "stop"
        food.goto(0, 90)

        # Hide the segments
        for segment in segments:
            segment.goto (1000, 1000)

        # Clear the segments list
        segments.clear ()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear ()
        pen.write ("Score: {}  High Score: {}".format (score, high_score), align="center",
                   font=("Courier", 24, "normal"))

        # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-922, 920)
        y = random.randint(-450, 340)
        food.goto(x, y)


        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            food.goto(0, 90)
            pygame.mixer.music.pause()

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 16, "normal"))

    time.sleep(delay)
wn.mainloop()
