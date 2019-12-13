def Div42by(num):
    try:
        return 42 /num
    except ZeroDivisionError:
        print('Your tried to divide by zero')

print (Div42by(0))
