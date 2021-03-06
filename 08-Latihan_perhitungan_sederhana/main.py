# latihan konversi satuan temperature 
# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("Suhu adalah",celcius,'Celcius')

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah",reamur,"Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit",fahrenheit,"Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin",kelvin,"Kelvin")

# Latihan
kelvin = ((fahrenheit-32)*(5/9))+273
print("suhu adalah", kelvin,"kelvin")