with open("labs/Temp-Converter.txt", "w") as TempConverter:
    TempConverter.write("Temperature Converter\n")
    TempConverter.write("Celsius to Fahrenheit: (C * 9/5) + 32\n")
    TempConverter.write("Fahrenheit to Celsius: (F - 32) * 5/9\n")
    TempConverter.write("\nCelsius to Fahrenheit conversions:\n")
    for celsius in range(-300, 212):
        fahrenheit = (celsius * 9/5) + 32
        TempConverter.write(format(f"{celsius:>8.3f}°C = {fahrenheit:>8.3f}°F\n"))
    TempConverter.write("\nFahrenheit to Celsius conversions:\n")
    for fahrenheit in range(-300, 212):
        celsius = (fahrenheit - 32) * 5/9
        TempConverter.write(format(f"{fahrenheit:>8.3f}°F = {celsius:>8.3f}°C\n"))