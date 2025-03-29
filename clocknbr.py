import time
import math

class ClockNumber: #клас для представлення цифри на годиннику
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return str(self.number)
#виводить у текстовому формать
    

class ClockHand:  # клас для представлення стрілки годинника
    
    def __init__(self, type_):
        self.type_ = type_  # 'hour', 'minute', 'second'
        self.angle = 0
        #type_ — тип стрілки: може бути 'hour', 'minute' або 'second'. Це визначає, 
        # чи є стрілка годинниковою, хвилинною чи секундною. angle — ініціалізація кута нахилу стрілки, спочатку встановлений в 0
    def update(self, time_value): # Оновлення кута нахилу стрілки
        if self.type_ == 'hour':
            self.angle = (time_value % 12) * 30
            #Для годинної стрілки ('hour'): Кут обчислюється за формулою 
            # (time_value % 12) * 30, де time_value — це годинник у 24-годинному форматі.
            #  % 12 забезпечує, що годинна стрілка обертається від 1 до 12.
        elif self.type_ == 'minute':
            self.angle = time_value * 6
        elif self.type_ == 'second':
            self.angle = time_value * 6
            #Для хвилинної стрілки та секундної стрілки ('minute' і 'second'):
            # #Кут обчислюється за формулою time_value * 6, оскільки одна хвилина або одна секунда — це 6 градусів на циферблаті.
    
    def __str__(self):
        return f"{self.type_.capitalize()} hand at {self.angle} degrees"
    #Метод __str__ дозволяє повернути текстове представлення об'єкта, 
    # щоб легко побачити інформацію про стрілку. self.type_.capitalize() — перетворює тип стрілки 
    # (наприклад, 'hour' на 'Hour'). self.angle — повертає кут, на який нахилена стрілка.
    
#виводить у текстовому вигляді тип стрілки та кут нахилу стрілки.