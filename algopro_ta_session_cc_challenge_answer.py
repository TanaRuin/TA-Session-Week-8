# -*- coding: utf-8 -*-


input_filename = "country_info.txt"

countries = {}
with open (input_filename) as country_file:
  country_file.readline()
  for row in country_file:
    data = row.strip("\n").split("|")
    country, capital, code, code3, dialing, timezone, currency = data
    country_dict = {
        'name' : country,
        'capital' : capital,
        'country_code' : code,
        'cc3' : code3,
        'dialing_code' : dialing,
        'timezone' : timezone,
        'currency' : currency,

    }

    countries[code] = country_dict
    countries[country.lower()] = country_dict


while True:
    # Ask the user for input
    user_input = input("Please enter the country name or code (or 'quit' to exit): ")

    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break

    # Check if the entered input is a country name
    if user_input.lower() in countries:
        capital_value = countries[user_input.lower()]['capital']
        print(f"The capital of {countries[user_input.lower()]['name']} ({user_input.lower()}) is {capital_value}")

    # Check if the entered input is a country code
    elif user_input.upper() in countries:
        capital_value = countries[user_input.upper()]['capital']
        print(f"The capital of {countries[user_input.upper()]['name']} ({user_input.upper()}) is {capital_value}")

    else:
        print(f"Country '{user_input}' not found in the dictionary.")

"""# New Section"""
