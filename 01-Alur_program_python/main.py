import time
start_time = time.time()
print("Hello World")

# ini adalah comment
a = 10 # ini adalah comment juga
"""ada apa dengan ucup dan si otong ganteng dalam comment multiline"""
print(a)
for i in range(1,1000) :
    a = 10
print(time.time() - start_time, "detik")

# kita bisa mengcompile python ke bytecode dengan cara "python3 -m py_compile Main.py"