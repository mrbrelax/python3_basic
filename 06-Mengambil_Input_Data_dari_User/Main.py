# data yang dimasukkan pasti string (str)
data = input("Masukkan data: ")
print("data = ", data, ",type = ", type(data))

# Jika kita ingin mengambil int, maka :
data_int = int(input("Masukkan data: "))
print("data = ", data_int, ",type = ", type(data_int))

# Float
angka = float(input("Masukkan data: "))
print("data = ", angka, ",type = ", type(angka))

# Bagaimana dengan Boolean (bool)
biner = bool(int(input("Masukkan nilai boolean: ")))
print("data = ", biner, ",type = ", type(biner))