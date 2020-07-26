""" User can input currency and header if under valid constraints
and then move on to selections"""

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


# DataSet class
class DataSet:
    header_length = 30

    def __init__(self, header=""):
        try:
            self.header = header
        except ValueError:
            self._header = ""
        self._data = None

    @property
    def header(self):
        # print("Getting value...")
        return self._header

    @header.setter
    def header(self, value):
        # print("Setting value...")
        if isinstance(value, str) and len(value) < self.header_length:
            self._header = value
        else:
            raise ValueError


def currency_options(base_curr="EUR"):

    # populate list of currency names in order to be able to iterate
    # through (for target_curr parameter in currency_converter function)
    currency_names = []
    for curr in conversions:
        currency_names.append(curr)

    # print the table intro and header
    print(f"\nOptions for converting from {base_curr}:")
    for curr in conversions:
        print(f"{curr}", end="\t")
    print("")

    # print converted values in table format
    for i in range(10, 100, 10):
        for j in range(len(conversions)):
            print(f"{currency_converter (i, base_curr, currency_names[j]):.2f}", end="\t")
        print("")

    # print using no extra list
    # for i in range(10, 100, 10):
    #     print(f"{currency_converter(i, base_curr, 'USD'):
    #     .2f}\t{currency_converter(i, base_curr, 'EUR'):.2f}\
    #     t{currency_converter(i, base_curr, 'CAD'):.2f}\t{currency_
    #     converter(i, base_curr, 'GBP'):.2f}\t{currency_converter
    #     (i, base_curr, 'CHF'):.2f}\t{currency_converter(i, base_curr,
    #     'NZD'):.2f}\t{currency_converter(i, base_curr, 'AUD'):.2f}\t
    #     {currency_converter(i, base_curr, 'JPY'):.2f}\t")


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
    valid_string = "Hello Database!"
    invalid_string = "Hello Database, this is your captain, Bob!"

    # 1
    testset1 = DataSet()
    if testset1.header == "":
        print("Testing constructor with default parameter: PASS")
    else:
        print("Testing constructor with default parameter: FAIL")

    # 2
    testset2 = DataSet(valid_string)
    if testset2.header == valid_string:
        print("Testing constructor with valid header argument: PASS")
    else:
        print("Testing constructor with valid header argument: FAIL")

    # 3
    testset3 = DataSet(invalid_string)
    if testset3.header == "":
        print("Testing constructor with invalid header argument: PASS")
    else:
        print("Testing constructor with invalid header argument: FAIL")

    # 4
    testset1.header = valid_string
    if testset1.header == valid_string:
        print("Testing setter with valid argument: PASS")
    else:
        print("Testing setter with valid argument: FAIL")

    # 5
    try:
        testset1.header = invalid_string
    except ValueError:
        print("Testing setter with invalid argument: PASS")


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


def menu(dataset: DataSet):
    """ Ask user menu selection and response appropriately"""
    while True:
        currency_options(home_currency)
        print()
        print(dataset.header)
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
            print("Min/Avg/Max by Location Functionality is not "
                  "implemented yet")
        elif selection == 5:
            print("Min/Avg/Max by Property Type Functionality is not"
                  " implemented yet")
        elif selection == 6:
            print("Adjustments based on Location Functionality is not "
                  "yet")
        elif selection == 7:
            print("Adjustments by Property Type Functionality is not "
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
    unit_test()
    print()

    my_name = input("Please enter your name: ")
    message = "Hi " + my_name + ", Welcome to Foothill's database " \
                                "project"
    print(message)

    global home_currency
    while home_currency not in conversions:
        home_currency = input("What is your home currency? ")

    air_bnb = DataSet()
    while True:
        header = input("Enter a header for the menu: ")
        try:
            air_bnb.header = header
        except ValueError:
            print("Header must be a string less than " +
                  str(DataSet.header_length) + " characters long")
            continue
        break

    menu(air_bnb)


if __name__ == "__main__":
    main()


"""
--- sample run #1 ---
Testing constructor with default parameter: PASS
Testing constructor with valid header argument: PASS
Testing constructor with invalid header argument: PASS
Testing setter with valid argument: PASS
Testing setter with invalid argument: PASS

Please enter your name: Milap
Hi Milap, Welcome to Foothill's database project
What is your home currency? EUR
Enter a header for the menu: This header is wayyyyyyyyyy to long, must 
be less than 30 characters long
Header must be a string less than 30 characters long
Enter a header for the menu: Data about Airbnb

Options for converting from EUR:
USD	EUR	CAD	GBP	CHF	NZD	AUD	JPY	
11.11	10.00	15.56	8.89	10.56	18.44	18.00	1199.11	
22.22	20.00	31.11	17.78	21.11	36.89	36.00	2398.22	
33.33	30.00	46.67	26.67	31.67	55.33	54.00	3597.33	
44.44	40.00	62.22	35.56	42.22	73.78	72.00	4796.44	
55.56	50.00	77.78	44.44	52.78	92.22	90.00	5995.56	
66.67	60.00	93.33	53.33	63.33	110.67	108.00	7194.67	
77.78	70.00	108.89	62.22	73.89	129.11	126.00	8393.78	
88.89	80.00	124.44	71.11	84.44	147.56	144.00	9592.89	
100.00	90.00	140.00	80.00	95.00	166.00	162.00	10792.00	

Data about Airbnb
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



Options for converting from EUR:
USD	EUR	CAD	GBP	CHF	NZD	AUD	JPY	
11.11	10.00	15.56	8.89	10.56	18.44	18.00	1199.11	
22.22	20.00	31.11	17.78	21.11	36.89	36.00	2398.22	
33.33	30.00	46.67	26.67	31.67	55.33	54.00	3597.33	
44.44	40.00	62.22	35.56	42.22	73.78	72.00	4796.44	
55.56	50.00	77.78	44.44	52.78	92.22	90.00	5995.56	
66.67	60.00	93.33	53.33	63.33	110.67	108.00	7194.67	
77.78	70.00	108.89	62.22	73.89	129.11	126.00	8393.78	
88.89	80.00	124.44	71.11	84.44	147.56	144.00	9592.89	
100.00	90.00	140.00	80.00	95.00	166.00	162.00	10792.00	

Data about Airbnb
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