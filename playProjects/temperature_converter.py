# Temperature converter

while True:
    temp = input('Enter a temp value: ')
    if temp.isdigit():
        while True:
          current_unit_of_temp = str(input('Enter the unit of the input temp(c/f/k): ')).lower()
          if current_unit_of_temp == 'c':
            unit_to_convert_to = str(input('Enter the unit to convert to(f/k): ')).lower()
            if unit_to_convert_to == 'f':
                temp_change = float(temp)
                celcius_to_fahrenheit = (temp_change * 9/5) + 32
                print(f"{temp_change} degree celcius in fahreheit is {celcius_to_fahrenheit:.2f} degrees")
            elif unit_to_convert_to == 'k':
                temp_change = float(temp)
                celsius_to_kelvin = temp_change + 273.15
                print(f"{temp_change} degree celcius in kelvin is {celsius_to_kelvin:.2f} degrees")
            else:
                print('Input only f or k')
            break
          elif current_unit_of_temp == 'f':
            unit_to_convert_to = str(input('Enter the unit to convert to(c/k): ')).lower()
            if unit_to_convert_to == 'c':
                temp_change = float(temp)
                fahrenheit_to_celcius = (temp_change - 32) * 5/9
                print(f"{temp_change} degree fahrenheit in celcius is {fahrenheit_to_celcius:.2f} degrees")
            elif unit_to_convert_to == 'k':
                temp_change = float(temp)
                fahrenheit_to_kelvin = ((temp_change - 32) * 5 / 9) + 273.15
                print(f"{temp_change} degree fahrenheit in kelvin is {fahrenheit_to_kelvin:.2f} degrees")
            else:
                print('Only input c or k ')
            break
          elif current_unit_of_temp == 'k':
            unit_to_convert_to = str(input('Enter the unit to convert to(c/f): ')).lower()
            if unit_to_convert_to == 'c':
               temp_change = float(temp)
               kelvin_to_celcius = temp_change - 273.15
               print(f"{temp_change} degree kelvin in celcius is {kelvin_to_celcius:.2f} degrees")
            elif current_unit_of_temp == 'f':
               temp_change = float(temp)
               kelvin_to_fahrenheit = ((temp_change - 273.15) * 9/5) + 32
               print(f"{temp_change} degree kelvin in fahrenheit is {kelvin_to_fahrenheit:.2f} degrees")
            else:
               print('Only input c or k ')
            break
        start_again = input('Will you start again (y/n): ').lower()
        if start_again == 'y':
            continue
        else:
            print('Thanks for using our program ❤💖💥')
            break
    else:
        print('Please enter a number')

