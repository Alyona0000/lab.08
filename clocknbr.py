import time
import math
import datetime
import turtle


class Watch:
    def __init__(self):
        self.current_time = datetime.datetime.now()

    def update_time(self):
        self.current_time = datetime.datetime.now()


class ClockFace:
    def __init__(self):
        self.numbers = [i for i in range(1, 13)]

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


class AnalogWatch(Watch):
    def __init__(self):
        super().__init__()
        self.face = ClockFace()
        self.hour_hand = ClockHand('hour')
        self.minute_hand = ClockHand('minute')
        self.second_hand = ClockHand('second')
        self.face.draw()
        self.hands_drawer = turtle.Turtle()
        self.hands_drawer.hideturtle()

    def update(self):
        self.update_time()
        self.hour_hand.update(self.current_time.hour)
        self.minute_hand.update(self.current_time.minute)
        self.second_hand.update(self.current_time.second)
        self.redraw_hands()
        turtle.ontimer(self.update, 1000)

    def redraw_hands(self):
        self.hands_drawer.clear()
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


class DigitalWatch(Watch):
    def __init__(self, is_24_hour=True):
        super().__init__()
        self.is_24_hour = is_24_hour
        self.display_drawer = turtle.Turtle()
        self.display_drawer.hideturtle()

    def display_time(self):
        self.update_time()
        time_str = self.current_time.strftime("%H:%M:%S") if self.is_24_hour else self.current_time.strftime(
            "%I:%M:%S %p")
        self.display_drawer.clear()
        self.display_drawer.penup()
        self.display_drawer.goto(0, -150)
        self.display_drawer.write(time_str, align="center", font=("Arial", 16, "bold"))
        turtle.ontimer(self.display_time, 1000)


def main():
    turtle.tracer(0, 0)
    analog_clock = AnalogWatch()
    digital_clock = DigitalWatch(is_24_hour=False)
    analog_clock.update()
    digital_clock.display_time()
    turtle.mainloop()


if __name__ == "__main__":
    main()