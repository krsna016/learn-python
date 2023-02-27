rivers = ["Ganga","Yamuna","Saraswati"]
rivers.append("Bhramaputra")
rivers.insert(2,"Kaveri")
popped = rivers.pop(0)
print(rivers)
del rivers[len(rivers)-1]
print(rivers)
rivers.remove("Saraswati")
print(rivers)
print(sorted(rivers))
print(rivers)
rivers.reverse()
print(rivers)
