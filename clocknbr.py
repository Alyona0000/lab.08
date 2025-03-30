import time
import math
import datetime
import turtle

class ClockNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

class ClockHand:
    def __init__(self, type_):
        self.type_ = type_
        self.angle = 0

    def update(self, time_value):
        if self.type_ == 'hour':
            self.angle = (time_value % 12) * 30
        elif self.type_ == 'minute':
            self.angle = time_value * 6
        elif self.type_ == 'second':
            self.angle = time_value * 6

    def __str__(self):
        return f"{self.type_.capitalize()} hand at {self.angle} degrees"

class ClockFace:
    def __init__(self):
        self.numbers = [ClockNumber(i) for i in range(1, 13)]

    def draw(self):
        turtle.penup()
        turtle.goto(0, -120)
        turtle.pendown()
        turtle.circle(120)
        for i, num in enumerate(self.numbers):
            x = 100 * math.sin(math.radians(i * 30))
            y = 100 * math.cos(math.radians(i * 30))
            turtle.penup()
            turtle.goto(x, y)
            turtle.write(str(num), align="center", font=("Arial", 14, "bold"))

class Clock:
    def __init__(self):
        self.face = ClockFace()
        self.hour_hand = ClockHand('hour')
        self.minute_hand = ClockHand('minute')
        self.second_hand = ClockHand('second')
        self.face.draw()  # Малюємо циферблат один раз
        self.hands_drawer = turtle.Turtle()
        self.hands_drawer.hideturtle()

    def update(self):
        now = datetime.datetime.now()
        self.hour_hand.update(now.hour)
        self.minute_hand.update(now.minute)
        self.second_hand.update(now.second)
        self.redraw_hands()
        turtle.ontimer(self.update, 1000)

    def redraw_hands(self):
        self.hands_drawer.clear()  # Очищуємо лише стрілки
        self.draw_hand(self.hour_hand, 50, "black")
        self.draw_hand(self.minute_hand, 70, "blue")
        self.draw_hand(self.second_hand, 90, "red")

    def draw_hand(self, hand, length, color):
        self.hands_drawer.penup()
        self.hands_drawer.goto(0, 0)
        self.hands_drawer.setheading(90 - hand.angle)
        self.hands_drawer.pendown()
        self.hands_drawer.pensize(3 if hand.type_ == 'hour' else 2)
        self.hands_drawer.pencolor(color)
        self.hands_drawer.forward(length)
        self.hands_drawer.penup()
        self.hands_drawer.goto(0, 0)
        self.hands_drawer.pendown()

def main():
    turtle.tracer(0, 0)
    clock = Clock()
    clock.update()
    turtle.mainloop()

if __name__ == "__main__":
    main()