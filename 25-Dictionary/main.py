print("====EXAMPLE DICTIONARY 1====")
D = {'name': 'Mr.B', 'age': '19', 'year': 2001}
print(D)
print(D['name'])
print(D['age'])

print("====EXAMPLE DICTIONARY 2====")
E = {'name':'Tom', 15:15, 15.1:15.1, True: True, (2,3): 5}
print(E[(2,3)])
print(E[True])
print(E[15])
print(len(E))
print(E.get('name'))
print(E.clear())
print(E)
print(D.update({'name':'Shin'}))
print(D)
print(D.keys())
print(D.values())
print(D.items())
print(D.popitem())