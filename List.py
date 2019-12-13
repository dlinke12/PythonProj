for i in [0,1,2,3]:
  print (i)

print(list(range(4)))
print(list(range(0,100,2)))


cat = ['fat','orange','loud']
size,color,disposition = cat
print (size)
print(color)
print(disposition)


cat = ['fat','orange','loud','Zoe']
print(cat.index('orange'))
cat.append('moose')
cat.insert(1,'Chicken')
cat.remove('orange')
cat.sort()
print(cat)
cat.sort(reverse=True)
print(cat)
cat.sort(key=str.lower) # Ensures that the string values are sorted correctly with lower and upper case characters
print(cat)

