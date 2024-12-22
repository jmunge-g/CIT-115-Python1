"""
The code convert temperatures
between Celsius and Fahrenheit
"""
name = "Name's Temp converter"
print(f"{name}")


def getUserInput():
    # try catch is used to validate user
    # 's input
    try:
        temperature = float(input("Enter a temperature: "))
        tempScale = input("Enter temperature scale (F or f for Fahrenheit or C or c for Celsius): ")
        if tempScale.lower() == 'f':
            # using while loop to validate the
            # temperature entered by the user
            while temperature > 212:
                print("Temp can not be > 212”")
                temperature = float(input("Enter a temperature: "))
            celsius = (5.0 / 9) * (temperature - 32)
            print(f"The Fahrenheit equivalent is: {celsius:.1f}")
        elif tempScale.lower() == 'c':
            while temperature > 100:
                print("Temp can not be > 100”")
                temperature = float(input("Enter a temperature: "))
            fahrenheit = ((9.0 / 5.0) * temperature) + 32
            print(f"The Celsius equivalent is: {fahrenheit:.1f}")
        else:
            print("Invalid temperature scale")
    except ValueError:
        print("Enter a valid numerical value")
        # a program exits here if the user enters non-numerical value
        exit(1)


# call the function
getUserInput()
