class Car:
    def __init__(self, speed, color):
        print("Car speed =", speed, "with color =", color)
        self.speed = speed
        self.color = color
        print("the __init__ is called")

MercedesBenz = Car(300, 'Black')
Bmw = Car(320, 'Grey')
Ferari = Car(350, 'Red')