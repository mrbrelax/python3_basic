# tipe data : Angka Satuan yang tidak menggunakan koma (Integer)
data_integer = 1
print("data : ", data_integer, "bertipe : ", type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print("data : ", data_float, "bertipe : ", type(data_float))

# tipe data : kumpulan karakter (String)
data_string = "Mr.B"
print("data : ", data_string, "bertipe : ", type(data_string))

# tipe data : biner true/false (Boolean)
data_bool = True
print("data : ", data_bool, "bertipe : ", type(data_bool))

##### Tipe Data Khusus #####
# Bilangan Kompleks
data_complex = complex(5,6)
print("data : ", data_complex, "bertipe : ", type(data_complex))

# tipe data dari Bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double, "bertipe : ", type(data_c_double))