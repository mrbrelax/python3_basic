# example Loop Controls break and continue statements
print("====BREAK====")
count = 0
while count <= 5:
    if count == 3:
        break
    else:
        print(count)
    count=count+1
print("thank you")

print("====CONTINUE====")
for letter in "amuls":
    if letter == 'u':
        continue
    else:
        print(letter)
print("thank you")

var = 10
while var > 0:
    var = var-1
    if var == 3:
        continue
    print(var)
print("Thank You")

print("====RANGE====")
number = 20
for number in range(10,25):
    print(number)
    if number is 20:
        print('angka ditemukkan',number)
        break
    else:
        print(number)
print("finish")