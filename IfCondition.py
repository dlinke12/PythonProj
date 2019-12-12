name='Alice'
if name == 'Alice':
    print('Hi, Alice')
else:
    print('Who are you?')    

if name: #Truthy value, when string is not blank, boolena returns true.
    print('True, value is not blank')
else:
    print('False, value is a blank valur')

spam= 0
while spam < 5:
        print('Hello ' + str(spam))
        spam = spam + 1 

spam = 0
while spam < 5:
        spam=spam+1
        if spam == 3:
            continue
        print('Spam is ' + str(spam))
        

print('Mat name is')
for i in range(5):
    print('Jimmy Five Times: ' + str(i))

print('Mat name is')
for i in range(10,100,3):
    print('Jimmy Five Times: ' + str(i))
