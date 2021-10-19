d = {'nom': "Dupuis", 'prenom': "Jacque", 'age': 30}

# 1
d.update({'prenom': "Jacques"})

# 2
keys = d.keys()
print(keys)

# 3
values = d.values()
print(values)

# 4
items = d.items()
print(items)

# 5
print(str(d.get('prenom')) + " " + str(d.get('nom')) + " a " + str(d.get('age')) + " ans.")