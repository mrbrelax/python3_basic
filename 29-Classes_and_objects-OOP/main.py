print("====EXAMPLE 1====")
class Car:
    pass
Ford = Car()
Honda = Car()
Audi = Car()

Ford.speed = 200
Honda.speed = 220
Audi.speed = 250

Ford.color = 'Red'
Honda.color = 'Blue'
Audi.color = 'black'
print(Ford.speed)
print(Ford.color)

print("====EXAMPLE 2====")
class Cars:
    pass
MercedesBenz = Cars()
Bmw = Cars()
Ferari = Cars()

MercedesBenz.speed = 300
Bmw.speed = 320
Ferari.speed = 350

MercedesBenz.color = 'Black'
Bmw.color = 'Grey'
Ferari.color = 'Red'

print("Car MercedesBenz with speed =", MercedesBenz.speed, "and with Colored =", MercedesBenz.color)