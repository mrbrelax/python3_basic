class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self, value):
        self.speed = value
    def get_speed(self):
        return self.speed

    def set_color(self, value):
        self.color = value

    def get_color(self):
        return self.color

ford = Car(300, 'Black')
honda = Car(320, 'Grey')
audi = Car(350, 'White')

ford.set_speed(300)
ford.speed = 400
print(ford.get_speed(), ford.get_color())