# Operator bitwise adalah operator biner (binary)
a = 9
b = 5
# Bitwise OR (|)
c = a | b
print('\n============OR===========')
print('nilai :', a, ', binary : ', format(a, '08b'))
print('nilai :', b, ', binary : ', format(b, '08b'))
print('-------------------------------(|)')
print('nilai :', c, ', binary : ', format(c, '08b'))

# Bitwise AND (&)
c = a & b
print('\n==========AND==========')
print('nilai :', a, ',binary :', format(a, '08b'))
print('nilai :', b, ',binary :', format(b, '08b'))
print('-------------------------------(&)')
print('nilai :', c, ',binary :', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n==========XOR==========')
print('nilai :', a, ',binary :', format(a, '08b'))
print('nilai :', b, ',binary :', format(b, '08b'))
print('-------------------------------(^)')
print('nilai :', c, ',binary :', format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print('\n==========NOT==========')
print('nilai :', a, ',binary :', format(a, '08b'))
print('-------------------------------(~)')
print('nilai :', c, ',binary :', format(c, '08b'))
print('--------------------------------(^)')  # di flip dengan XOR
d = 0b0001001
e = 0b1111111
print('nilai :', e ^ d, ', binary :', format(e ^ d, '08b'))

# shifting (geser):
# shift right (>>) (geser ke kanan)
c = a >> 2
print('\n==========>>=========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('-------------------------------(>>)')
print('nilai :', c, ', binary :', format(c, '08b'))

# Shift Left (<<) (geser ke kiri)
print('\n==========<<=========')
c = a << 2
print('nilai :', a, ', binary :', format(a, '08b'))
print('--------------------------------(<<)')
print('nilai :', c, ', binary :', format(c, '08b'))
