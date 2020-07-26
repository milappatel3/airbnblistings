""" User can input their borough and type of housing to see the
associated housing """

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


# Custom Exception (EmptyDatasetError)
class EmptyDatasetError(Exception):
    def __init__(self, message):
        super().__init__(message)


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

    def load_default_data(self):
        datalist = [
            ("Staten Island", "Private room", 70),
            ("Brooklyn", "Private room", 50),
            ("Bronx", "Private room", 40),
            ("Brooklyn", "Entire home / apt", 150),
            ("Manhattan", "Private room", 125),
            ("Manhattan", "Entire home / apt", 196),
            ("Brooklyn", "Private room", 110),
            ("Manhattan", "Entire home / apt", 170),
            ("Manhattan", "Entire home / apt", 165),
            ("Manhattan", "Entire home / apt", 150),
            ("Manhattan", "Entire home / apt", 100),
            ("Brooklyn", "Private room", 65),
            ("Queens", "Entire home / apt", 350),
            ("Manhattan", "Private room", 99),
            ("Brooklyn", "Entire home / apt", 200),
            ("Brooklyn", "Entire home / apt", 150),
            ("Brooklyn", "Private room", 99),
            ("Brooklyn", "Private room", 120),
        ]

        self._data = datalist

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        if self._data is None:
            raise EmptyDatasetError(
                "The dataset is empty. Cannot perform any "
                "calculations.")

        newlist = [tup[2] for tup in self._data if
                   tup[0] == descriptor_one and tup[
                       1] == descriptor_two]

        if len(newlist) == 0:
            return None, None, None
        else:
            return min(newlist), sum(newlist) / len(newlist), \
                   max(newlist)


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
            print(
                f"{currency_converter(i, base_curr, currency_names[j]):.2f}",
                end="\t")
        print("")

    # print using no extra list
    # for i in range(10, 100, 10):
    #     print(f"{currency_converter(i, base_curr, 'USD'):.2f}\
    #     t{currency_converter(i, base_curr, 'EUR'):.2f}\
    #     t{currency_converter(i, base_curr, 'CAD'):.2f}\
    #     t{currency_converter(i, base_curr, 'GBP'):.2f}\
    #     t{currency_converter(i, base_curr, 'CHF'):.2f}\
    #     t{currency_converter(i, base_curr, 'NZD'):.2f}\
    #     t{currency_converter(i, base_curr, 'AUD'):.2f}\
    #     t{currency_converter(i, base_curr, 'JPY'):.2f}\t")


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
    my_set = DataSet("This is my DataSet!")

    # 1
    try:
        my_set._cross_table_statistics("Brooklyn", "Private room")
    except EmptyDatasetError:
        print("Method Raises EmptyDataSet Error:\t\tPASS")

    my_set.load_default_data()

    # 2
    if my_set._cross_table_statistics("Brooklyn",
                                      "not an apartment") == \
            (None, None, None):
        print("Invalid Property Type Returns None Tuple:\tPASS")
    else:
        print("Invalid Property Type Returns None Tuple:\tFAIL")

    # 3
    if my_set._cross_table_statistics("Not a borough",
                                      "Private room") == \
            (None, None, None):
        print("Invalid Borough Returns None Tuple:\t\tPASS")
    else:
        print("Invalid Borough Returns None Tuple:\t\tFAIL")

    # 4
    if my_set._cross_table_statistics("Queens", "Private room") == \
            (None, None, None):
        print("No Matching Rows Returns None Tuple:\t\tPASS")
    else:
        print("No Matching Rows Returns None Tuple:\t\tFAIL")

    # 5
    if my_set._cross_table_statistics("Bronx", "Private room") == \
            (40, 40, 40):
        print("One Matching Row Returns Correct Tuple:\t\tPASS")
    else:
        print("One Matching Row Returns Correct Tuple:\t\tFAIL")

    # 6
    if my_set._cross_table_statistics("Brooklyn", "Private room") == \
            (50, 88.8, 120):
        print("Multiple Matching Rows Returns Correct Tuple:\tPASS")
    else:
        print("Multiple Matching Rows Returns Correct Tuple:\tFAIL")


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
    unit_test()
    print()

    # my_name = input("Please enter your name: ")
    # message = "Hi " + my_name + ", Welcome to Foothill's database
    # project"
    # print(message)

    # global home_currency
    # while home_currency not in conversions:
    #     home_currency = input("What is your home currency? ")

    # air_bnb = DataSet()
    # while True:
    #     header = input("Enter a header for the menu: ")
    #     try:
    #         air_bnb.header = header
    #     except ValueError:
    #         print("Header must be a string less than " +
    #         str(DataSet.header_length) + " characters long")
    #         continue
    #     break

    # menu(air_bnb)


if __name__ == "__main__":
    main()

"""
--- sample run #1 ---
Method Raises EmptyDataSet Error:		PASS
Invalid Property Type Returns None Tuple:	PASS
Invalid Borough Returns None Tuple:		PASS
No Matching Rows Returns None Tuple:		PASS
One Matching Row Returns Correct Tuple:		PASS
Multiple Matching Rows Returns Correct Tuple:	PASS
"""