print("====EXAMPLE 1====")
def student(name, age, *marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)
    # print('marks', marks)
    for x in marks:
        print(x)

student('Mr.B', 19, 95, 70, 80, 50)

print("====EXAMPLE 2====")
def student1(name, age, **marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)
    for key, value in marks.items():
        print(key, ' ', value)
student1('Mr.B', 19, english=95, math=70, physics=80, biology=50)