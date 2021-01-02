# operasi dan manupulasi string
# 1. menyambung string (concatenate)
nama_depan = "Ucup"
nama_tengah = "D"
nama_belakang = "Fame"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string
# mengecek apakah ada component char atau string didalam string
D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*3)
print(5*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-1):" + nama_lengkap[-1])
print("index ke-(-2):" + nama_lengkap[-2])
print("index ke-[0:4]:" + nama_lengkap[0:4])
print("index ke-[3:8]:" + nama_lengkap[3:8])
print("index ke-[2,4,6,8,10]:" + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord("'")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong paraotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))
