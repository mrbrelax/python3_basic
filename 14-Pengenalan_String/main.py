data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string :
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double qoute "..."
'''

data = 'menggunakan single qoute'
print(data)

data = "menggunakan double qoute"
print(data)

print('"Hallo apa kabar?"')
print("'Kabar Kamu bagaimana?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \ :
# membuat tanda ' menjadi string
print('Besok adalah hari jum\'at')
print('g\'day, isn\'t it?')
# backlash
print("C:\\Users\\Mrb")  # menggunakan \\ harus 2 kali
# tab
print("ucup\totong jauhan")  # untuk tab menggunakan \t
# backspace
print("ucup\botong, deketan")  # backspace (menjadi dekat) menggunakan \b
# newline
# LF -> Line Feed di pakai oleh unix, macos, linux
print("baris pertama.\nbaris kedua")

# CR -> Carriage return dipakai oleh commodore, acorn, lisp
print("baris pertama.\rbaris kedua")

# CRLF -> Line feed carriage return dipakai oleh windows
print("baris pertama.\r\nbaris kedua")

# 3. String literal atau RAW :
# RAW string
print(r'C:\new folder')
# multiline literal string
print(""" 
Nama : Mr.B Relax
University : Ubharajaya
""")
# multiline literal string and RAW
print(r""" 
Nama : Mr.B Relax
Semester : 3
Website : www.mrbrelax.com
""")