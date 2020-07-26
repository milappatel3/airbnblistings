""" Assignment five asks the user's name, currency and prints a
friendly greeting. The user will be presented with a menu and
asked to make a selection. The user will get a response, but the
functions are not yet implemented."""

# global conversions dictionary
conversions = {
    "USD": 1,
    "EUR": .9,
    "CAD": 1.4,
    "GBP": .8,
    "CHF": .95,
    "NZD": 1.66,
    "AUD": 1.62,
    "JPY": 107.92
}

# global home currency variable
home_currency = ""


def currency_options(base_curr="EUR"):
    # populate list of currency names in order to be able to iterate through (for target_curr parameter in currency_converter function)
    currency_names = []
    for curr in conversions:
        currency_names.append(curr)

    # print the table intro and header
    print(f"Options for converting from {base_curr}:")
    for curr in conversions:
        print(f"{curr}", end="\t")
    print("")

    # print converted values in table format
    for i in range(10, 100, 10):
        for j in range(len(conversions)):
            print(
                f"{currency_converter(i, base_curr, currency_names[j]):.2f}",
                end="\t")
        print("")


def currency_converter(quantity, source_curr, target_curr):
    if quantity == 0:
        raise ValueError
    if not isinstance(source_curr, str) or not isinstance(target_curr,
                                                          str):
        raise KeyError

    USD = quantity / conversions.get(source_curr)
    final_quantity = USD * conversions.get(target_curr)

    # print("{} in {} is {} in {}".format(quantity, source_curr,
    # final_quantity, target_curr))

    return final_quantity


def unit_test():
    try:
        currency_converter(125, 35, "AUD")
    except KeyError:
        print("PASS: Invalid Source Currency Raises KeyError")

    try:
        currency_converter(125, "EUR", 35)
    except KeyError:
        print("PASS: Invalid Target Currency Raises KeyError")

    try:
        currency_converter(0, "EUR", "AUD")
    except ValueError:
        print("PASS: Zero Quantity Raises ValueError")

    if currency_converter(125, "USD", "GBP") == 100.0:
        print("PASS: Conversion from USD to GBP")

    if currency_converter(125, "GBP", "USD") == 156.25:
        print("PASS: Conversion from GBP to USD")

    if currency_converter(2.8, "CAD", "JPY") == 215.84:
        print("PASS: Conversion from CAD to JPY")


def print_main():
    """ Display the main menu text. """
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """ Ask user menu selection and response appropriately"""
    currency_options(home_currency)
    while True:
        print_main()

        try:
            selection = int(input("What is your choice? "))
        except ValueError:
            print("Please input a number")
            continue

        if selection == 1:
            print("Average Rent Functionality is not implemented yet")
        elif selection == 2:
            print("Minimum Rent Functionality is not implemented yet")
        elif selection == 3:
            print("Maximum Rent Functionality is not implemented yet")
        elif selection == 4:
            print(
                "Min/Avg/Max by Location Functionality is not "
                "implemented yet")
        elif selection == 5:
            print(
                "Min/Avg/Max by Property Type Functionality is not "
                "implemented yet")
        elif selection == 6:
            print(
                "Adjustments based on Location Functionality is not "
                "yet")
        elif selection == 7:
            print(
                "Adjustments by Property Type Functionality is not "
                "implemented yet")
        elif selection == 8:
            print("Load Data Functionality is not implemented yet")
        elif selection == 9:
            print("Goodbye! Thank you for using the database\n")
            break
        else:
            print("Please enter a number between 1 and 9 only")
        print("\n")


def main():
    my_name = input("Please enter your name: ")
    message = "Hi " + my_name + ", Welcome to Foothill's database " \
                                "project"
    print(message)

    global home_currency
    while home_currency not in conversions:
        home_currency = input("What is your home currency? ")

    menu()


if __name__ == "__main__":
    main()

"""
--- sample run #1 ---
Please enter your name: Milap
Hi Milap, Welcome to Foothill's database project
What is your home currency? MON
What is your home currency? USD
Options for converting from USD:
USD	EUR	CAD	GBP	CHF	NZD	AUD	JPY	
10.00	9.00	14.00	8.00	9.50	16.60	16.20	1079.20	
20.00	18.00	28.00	16.00	19.00	33.20	32.40	2158.40	
30.00	27.00	42.00	24.00	28.50	49.80	48.60	3237.60	
40.00	36.00	56.00	32.00	38.00	66.40	64.80	4316.80	
50.00	45.00	70.00	40.00	47.50	83.00	81.00	5396.00	
60.00	54.00	84.00	48.00	57.00	99.60	97.20	6475.20	
70.00	63.00	98.00	56.00	66.50	116.20	113.40	7554.40	
80.00	72.00	112.00	64.00	76.00	132.80	129.60	8633.60	
90.00	81.00	126.00	72.00	85.50	149.40	145.80	9712.80	
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
Average Rent Functionality is not implemented yet


Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
Goodbye! Thank you for using the database
"""