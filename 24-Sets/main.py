print("====EXAMPLE SETS 1====")
superhero = set()
superhero.add("wiro sableng")
superhero.add("gundala")
superhero.add("saras 008")
superhero.add(212)
print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.union(genap))
print(ganjil.intersection(prima))

print("====EXAMPLE SETS 2====")
a = {1,2.4,2,4,9,'aaa','abc',9,2}
b = set([1,4,3,'abc',87])
c = set()
print(a)
print(b)
print(c)
print(len(a))
# for x in a:
#     print(x)
c.add("3,4,5")
print(c)

c.update([2,'abc',3])
print(c)

a.remove(2.4)
print(a)

b.discard(3)
print(b)

print(a.pop())
a.union(b)
print(a|b|c)
print(a.union(b,c))
print(a&b)
print(a.intersection(b,c))
print(a-b)
print(a.difference(c))
d = frozenset(a)
print(d)