print("Ahmed Muse's Converter")

print("Temperature Converter")
print("Enter 'C' for Celsius or 'F' for Fahrenheit.")

sTemp = input("Is the temperature in Celsius or Fahrenheit (C or F): ")

if sTemp == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius equivalent is: {fahrenheit:.2f}°F")

elif sTemp == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The Fahrenheit equivalent is: {celsius:.2f}°C")

else:
    print("Invalid input. Please enter 'C' or 'F'.")


