""" Assignment four asks the programmer to input a quantity, original
source of currency and final source of currency. The user can enter any
 quantity they would like as long as it is within the parameters.
 """

conversions = {
        "USD": 1,
        "EUR": .9,
        "CAD": 1.4,
        "GBP": .8,
        "CHF": .95,
        "NZD": 1.66,
        "AUD": 1.62,
        "JPY": 107.92,
    }


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
    """ Ask user menu selection and response appropriately. Continue
    to ask until the user decides to quit. """
    while True:
        print_main()

        try:
            selection = int(input("What is your choice? "))
        except ValueError:
            print("Please input a number")
            continue
        if selection == 1:
            print("Average Rent Functionality is not "
                  "implemented yet")
        elif selection == 2:
            print("Minimum Rent Functionality is not "
                  "implemented yet")
        elif selection == 3:
            print("Maximum Rent Functionality is not "
                  "implemented yet")
        elif selection == 4:
            print("Min/Avg/Max by Location Functionality is "
                  "not implemented yet")
        elif selection == 5:
            print("Min/Avg/Max by Property Type Functionality is "
                  "not implemented yet")
        elif selection == 6:
            print("Adjustments based on Location Functionality is "
                  "not yet")
        elif selection == 7:
            print("Adjustments by Property Type Functionality is "
                  "not implemented yet")
        elif selection == 8:
            print("Load Data Functionality is not implemented yet")
        elif selection == 9:
            print("Quitting now")
            print("Sorry to see you go")
            break
        else:
            print("Please enter a number between 1 and 9 only")


def currency_converter(quantity: int, source_curr: str,
                       target_curr: str):
    """ Users can do conversions between different currency types """
    if quantity == 0:
        raise ValueError
    if not isinstance(source_curr, str):
        raise KeyError
    if not isinstance(target_curr, str):
        raise KeyError

    USD = quantity / conversions[source_curr]
    final_quantity = USD * conversions[target_curr]

    print("{} in {} is {} in {}".format(quantity, source_curr,
                                        final_quantity, target_curr))

    return final_quantity


def main():
    my_name = input("Please enter your name:")
    message = "Hi " + my_name + ", Welcome to Foothill's database " \
                                "project"
    print(message)
    menu()
    currency_converter(100, "EUR", "CAD")
    # unit_test()


def unit_test():
    """ Unit test cases for programmer to test accuracy of code"""
    try:
        currency_converter(125, 35, "AUD")
    except KeyError:
        print("PASS: Invalid Source Currency Raises KeyError")
    try:
        currency_converter(125, "AUD", 35)
    except KeyError:
        print("PASS: Invalid Target Currency Raises KeyError")
    try:
        currency_converter(0, "EUR", "AUD")
    except ValueError:
        print("PASS: Zero Quantity Raises ValueError")
    if currency_converter(100, "USD", "GBP") == 80:
        print("PASS: Conversion from USD to GBP")
    if currency_converter(100, "CAD", "USD") == 71.42857142857143:
        print("PASS: Conversion from CAD to USD")
    if currency_converter(100, "EUR", "CAD") == 155.55555555555554:
        print("PASS: Conversion from EUR to CAD")


if __name__ == "__main__":
    main()


"""
---sample run #1---
PASS: Invalid Source Currency Raises KeyError
PASS: Invalid Target Currency Raises KeyError
PASS: Zero Quantity Raises ValueError
100 in USD is 80.0 in GBP
PASS: Conversion from USD to GBP
100 in CAD is 71.42857142857143 in USD
PASS: Conversion from CAD to USD
100 in EUR is 155.55555555555554 in CAD
PASS: Conversion from EUR to CAD
"""