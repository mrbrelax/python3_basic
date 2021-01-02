# operator dalam methods
## merubah case dari string
# merubah semua ke upper case
salam = "bro!"
print("normal =" + salam)
salam = salam.upper()
print("upper =" + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeezZzZZZ"
print("normal =" + alay)
alay = alay.lower()
print("lower =" + alay)

## pengecekan dengan isX methods
salam = "sis"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + "is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengechek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- space, tab, newline "\n"
# istitle() <-- semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# ngechek komponen startswith() endswith()
cek_start = "ViaraIndah".startswith("Viara")
print("start = " + str(cek_start))
cek_end = "ViaraIndah Pratiwi".endswith("Pratiwi")
print("end = " + str(cek_end))

# penggabungan komponen join() <- menggabungkan | split() <-- memisahkan
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter menggunakan rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")
kanan = kanan.strip()
print("'"+kanan+"'")