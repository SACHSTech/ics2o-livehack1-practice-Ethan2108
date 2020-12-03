#Asks user for the amount of degrees fahrenheit
f = float(input("Degrees fahrenheit: "))

#Tells user the amount of degrees celsius after conversion
print(f , "degrees fahrenheit equals", float((f - 32) * (5/9) ), "degrees celsius.")
