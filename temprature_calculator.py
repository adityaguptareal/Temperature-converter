def formula(temp):
    return((temp*9/5) + 32 )

temperature=int(input("Enter the temperature in Celsius: "))
convert_temp=formula(temperature)
print(f'The velaue of {temperature} in Farenheit {convert_temp}')