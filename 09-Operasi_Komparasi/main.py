# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not
# "=" : assignment
# "==" : membandingkan
a = 4
b = 2

# lebih besar dari >
print("===LEBIH BESAR DARI (>)===")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(a,'>',3,'=',hasil)
hasil = b > 2
print(a,'>',2,'=',hasil)

# Kurang dari <
print("===KURANG DARI (<)===")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(a,'<',3,'=',hasil)
hasil = b < 2
print(a,'<',2,'=',hasil)

# Lebih dari sama dengan >=
print("===LEBIH DARI SAMA DENGAN(>=)===")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 2
print(a,'>=',2,'=',hasil)

# Kurang dari sama dengan <=
print("===KURANG DARI SAMA DENGAN(<=)===")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 2
print(a,'<=',2,'=',hasil)

# Sama dengan (==)
print("===SAMA DENGAN(==)===")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(a,'==',4,'=',hasil)

# Tidak sama dengan (!=)
print("===TIDAK SAMA DENGAN(!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity
print("===Object Identity(is)===")
x = 5 # ini adalah assignment membuat objek 
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

# Object Identity (is not)
print("===Object Identity(is not)===")
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',x,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)

x = 5
y = 6
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y 
print('x is not y =',hasil)