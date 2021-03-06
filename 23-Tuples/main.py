import sys
import timeit

print("====EXAMPLE TUPLE 1")
animal = ('dog','cat','monkey')
print(animal)
print(animal[0])

print("====EXAMPLE TUPLE 2====")
tuple1 = ((10,2.3),(3.5,4))
print(tuple1)
print(tuple1[0])

print("====EXAMPLE TUPLE 3====")
ganjil = [1,3,5,7,9]
genap = [2,4,6,8]
print(ganjil)
print(genap)
print(genap.index(8))

print("====EXAMPLE TUPLE 4====")
data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14]
data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14)
besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)
print("besar data list", besar_datalist)
print("besar data tuple", besar_datatuple)

print("====EXAMPLE TUPLE 5====")
data_list1 = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]",number=1000000)
data_tuple1 = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]",number=100000) 
print("waktu untuk memproses list:", data_list1)
print("waktu untuk memproses tuple1:", data_tuple1)