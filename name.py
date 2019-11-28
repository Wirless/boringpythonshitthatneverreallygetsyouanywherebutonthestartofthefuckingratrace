##2c

def kelvintemp(temp):
    '''
    (num) -> num
    Input a temperature to be converted from Fahrenheit into Kelvin
    >>>kelvintemp(50)
    283.15
    '''
    result = (temp + 459.67) * 5/9
    return result


#main body
temp = float(input("Enter the temperature in degrees Fahrenheit: "))
print()
x = f"{temp} degrees Fahrenheit is equal to {kelvintemp(temp)} Kelvin."
print(x)

