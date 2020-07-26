""" Assignment two asks the user's name and prints a friendly greeting.
    The user will be presented with a menu and asked to make a
     selection. The user will get a response, but the functions are
     not yet implemented."""


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
    print_main()
    try:
        selection = int(input("What is your choice? "))
    except ValueError:
        print("Please input a number")
    else:
        if selection == "1":
            print("Average Rent Functionality is not implemented yet")
        elif selection == "2":
            print("Minimum Rent Functionality is not implemented yet")
        elif selection == "3":
            print("Maximum Rent Functionality is not implemented yet")
        elif selection == "4":
            print("Min/Avg/Max by Location Functionality is "
                  "not implemented yet")
        elif selection == "5":
            print("Min/Avg/Max by Property Type Functionality is "
                  "not implemented yet")
        elif selection == "6":
            print("Adjustments based on Location Functionality is "
                  "not yet")
        elif selection == "7":
            print("Adjustments by Property Type Functionality is "
                  "not implemented yet")
        elif selection == "8":
            print("Load Data Functionality is not implemented yet")
        elif selection == "9":
            print("Quitting now")
        else:
            print("Please enter a number between 1 and 9 only")


def main():
    my_name = input("Please enter your name:")
    message = "Hi " + my_name + ", Welcome to Foothill's " \
                                "database project"
    print(message)
    menu()


if __name__ == "__main__":
    main()


"""
--- sample run #1 ---


--- sample run #2 ---


--- sample run #3 ---


--- sample run #4 ---
"""