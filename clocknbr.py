ffeefvigfsffsffffuymport time
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
            turtle.pendown()
            turtle.write(str(num), align="center", font=("Arial", 14, "bold"))


class Clock:
    def __init__(self):
        self.face = ClockFace()
        self.hour_hand = ClockHand('hour')
        self.minute_hand = ClockHand('minute')
        self.second_hand = ClockHand('second')

    def update(self):
        turtle.clear()
        self.face.draw()
        now = datetime.datetime.now()
        self.hour_hand.update(now.hour)
        self.minute_hand.update(now.minute)
        self.second_hand.update(now.second)
        self.draw_hand(self.hour_hand, 50, "black")
        self.draw_hand(self.minute_hand, 70, "blue")
        self.draw_hand(self.second_hand, 90, "red")
        turtle.update()
        turtle.ontimer(self.update, 1000)  # Автоматичне оновлення кожну секунду

    def draw_hand(self, hand, length, color):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90 - hand.angle)
        turtle.pendown()
        turtle.pensize(3 if hand.type_ == 'hour' else 2)
        turtle.pencolor(color)
        turtle.forward(length)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()


def main():
    turtle.tracer(0, 0)
    clock = Clock()
    clock.update()  # Запускаємо оновлення без потоків
    turtle.mainloop()

##
if __name__ == "__main__":
    main()
