""" Final Assignment """

from enum import Enum
import csv

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

# global filename variable
filename = './AB_NYC_2019.csv'


# Custom Exception (EmptyDatasetError)
class EmptyDatasetError(Exception):
    def __init__(self, message):
        super().__init__(message)


# Enums


# DataSet class
class DataSet():
    header_length = 30

    class Categories(Enum):
        LOCATION = 0
        PROPERTY_TYPE = 1

    class Stats(Enum):
        MIN = 0
        AVG = 1
        MAX = 2

    def __init__(self, header=""):
        try:
            self.header = header
        except ValueError:
            self._header = ""

        self._data = None
        self._labels = {self.Categories.LOCATION: set(),
                        self.Categories.PROPERTY_TYPE: set()}
        self._active_labels = {self.Categories.LOCATION: set(),
                               self.Categories.PROPERTY_TYPE: set()}

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

    def _initialize_sets(self):
        if self._data == None:
            raise EmptyDatasetError(
                "The dataset is empty. Cannot perform any calculations.")

        for tup in self._data:
            self._labels[self.Categories.LOCATION].add(tup[0])
            self._labels[self.Categories.PROPERTY_TYPE].add(tup[1])

            self._active_labels[self.Categories.LOCATION].add(tup[0])
            self._active_labels[self.Categories.PROPERTY_TYPE].add(
                tup[1])

    def load_default_data(self):
        dataList = [
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
        self._data = dataList
        self._initialize_sets()

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        if self._data == None:
            raise EmptyDatasetError(
                "The dataset is empty. Cannot perform any calculations.")

        newList = [tup[2] for tup in self._data if
                   tup[0] == descriptor_one and tup[
                       1] == descriptor_two]

        if len(newList) == 0:
            return (None, None, None)
        else:
            return (
            min(newList), sum(newList) / len(newList), max(newList))

    def display_cross_table(self, stat: Stats):
        if self._data == None:
            raise EmptyDatasetError(
                "The dataset is empty. Cannot perform any calculations.")

        boroughs = sorted(
            [b for b in self._labels[self.Categories.LOCATION]])
        prop_types = sorted(
            [p for p in self._labels[self.Categories.PROPERTY_TYPE]])

        space_constant = 20
        print(
            f"{'':<{space_constant}}{prop_types[0]:<{space_constant + 2}}{prop_types[1]:<{space_constant}}")
        for b in boroughs:
            print(f"{b:<{space_constant}}", end="")
            for p in prop_types:
                value = self._cross_table_statistics(b, p)[stat.value]
                if value == None:
                    print(f"$ {'N/A':<{space_constant}}", end="")
                else:
                    print(f"$ {value:<{space_constant}.2f}", end="")
            print("")

    def _table_statistics(self, row_category: Categories, label: str):
        retTup = ()
        if row_category == self.Categories.LOCATION:
            newList = [tup[2] for tup in self._data if
                       tup[0] == label and tup[1] in
                       self._active_labels[
                           self.Categories.PROPERTY_TYPE]]
            retTup = (None, None, None) if len(newList) == 0 else (
            min(newList), sum(newList) / len(newList), max(newList))
        elif row_category == self.Categories.PROPERTY_TYPE:
            newList = [tup[2] for tup in self._data if
                       tup[0] in self._active_labels[
                           self.Categories.LOCATION] and tup[
                           1] == label]
            retTup = (None, None, None) if len(newList) == 0 else (
            min(newList), sum(newList) / len(newList), max(newList))

        return retTup

    def display_field_table(self, rows: Categories):
        if self._data == None:
            raise EmptyDatasetError(
                "The dataset is empty. Cannot perform any calculations.")

        print(
            "The following data are from properties matching these criteria:")
        if rows == self.Categories.LOCATION:
            for item in self.get_active_labels(
                    self.Categories.PROPERTY_TYPE):
                print(f"- {item}")
            print("")
        else:
            for item in self.get_active_labels(
                    self.Categories.LOCATION):
                print(f"- {item}")
            print("")

        space_constant = 10
        print(
            f"{'':<{space_constant * 2}}{'Minimum':<{space_constant + 2}}{'Average':<{space_constant + 2}}{'Maximum':<{space_constant}}")
        for item in sorted(self.get_labels(rows)):
            valueTup = self._table_statistics(rows, item)

            if valueTup == (None, None, None):
                printStr = f"{item:<{space_constant * 2}}{'N/A':<{space_constant + 2}}{'N/A':<{space_constant + 2}}{'N/A':<{space_constant}}"
            else:
                printStr = f"{item:<{space_constant * 2}}$ {valueTup[0]:<{space_constant}.2f}$ {valueTup[1]:<{space_constant}.2f}$ {valueTup[2]:<{space_constant}.2f}"

            print(printStr)

    @staticmethod
    def bubble_sort(list_to_sort: list):
        counter = 0
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[
                                                           i + 1], \
                                                       list_to_sort[i]
                counter += 1
        if counter == 0:
            return list_to_sort
        else:
            return DataSet.bubble_sort(list_to_sort)

    def get_labels(self, category: Categories):
        return [item for item in self._labels[category]]

    def get_active_labels(self, category: Categories):
        return [item for item in self._active_labels[category]]

    def toggle_active_label(self, category: Categories,
                            descriptor: str):
        if descriptor in self._active_labels[category]:
            self._active_labels[category].remove(descriptor)
        else:
            self._active_labels[category].add(descriptor)

    def load_file(self, file):
        dataList = []
        reader = csv.DictReader(open(file, 'r'))

        for row in reader:
            dataList.append((row["neighbourhood_group"],
                             row["room_type"], int(row["price"])))

        self._data = dataList
        self._initialize_sets()


def manange_filters(dataset: DataSet, category: DataSet.Categories):
    if dataset._data == None:
        raise EmptyDatasetError(
            "The dataset is empty. Cannot perform any calculations.")

    print("The following labels are in the dataset:")

    indexedItems = list(
        enumerate(sorted(dataset.get_labels(category)), 1))

    while True:
        for count, item in indexedItems:
            if item in dataset.get_active_labels(category):
                print(f"{count}: {item:<20}ACTIVE")
            else:
                print(f"{count}: {item:<20}INACTIVE")
        print("")

        userInput = input(
            "Please select an item to toggle or enter a blank line when you are finished: ")
        if userInput == "":
            break

        userInput = int(userInput)

        if userInput < 1 or userInput > len(indexedItems):
            print("Invalid item.\n")
            continue

        if indexedItems[userInput - 1][1] in dataset.get_active_labels(
                category):
            dataset._active_labels[category].remove(
                indexedItems[userInput - 1][1])
        else:
            dataset._active_labels[category].add(
                indexedItems[userInput - 1][1])


def currency_options(base_curr="EUR"):
    # populate list of currency names in order to be able to iterate through (for target_curr parameter in currency_converter function)
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


def currency_converter(quantity, source_curr, target_curr):
    if quantity == 0:
        raise ValueError
    if not isinstance(source_curr, str) or not isinstance(target_curr,
                                                          str):
        raise KeyError

    USD = quantity / conversions.get(source_curr)
    final_quantity = USD * conversions.get(target_curr)

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
                                      "not an apartment") == (
    None, None, None):
        print("Invalid Property Type Returns None Tuple:\tPASS")
    else:
        print("Invalid Property Type Returns None Tuple:\tFAIL")

    # 3
    if my_set._cross_table_statistics("Not a borough",
                                      "Private room") == (
    None, None, None):
        print("Invalid Borough Returns None Tuple:\t\tPASS")
    else:
        print("Invalid Borough Returns None Tuple:\t\tFAIL")

    # 4
    if my_set._cross_table_statistics("Queens", "Private room") == (
    None, None, None):
        print("No Matching Rows Returns None Tuple:\t\tPASS")
    else:
        print("No Matching Rows Returns None Tuple:\t\tFAIL")

    # 5
    if my_set._cross_table_statistics("Bronx", "Private room") == (
    40, 40, 40):
        print("One Matching Row Returns Correct Tuple:\t\tPASS")
    else:
        print("One Matching Row Returns Correct Tuple:\t\tFAIL")

    # 6
    if my_set._cross_table_statistics("Brooklyn", "Private room") == (
    50, 88.8, 120):
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
    currency_options(home_currency)
    print()
    while True:
        print(dataset.header)
        print_main()

        try:
            selection = int(input("What is your choice? "))
        except ValueError:
            print("Please input a number")
            continue

        if selection == 1:
            try:
                dataset.display_cross_table(DataSet.Stats.AVG)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 2:
            try:
                dataset.display_cross_table(DataSet.Stats.MIN)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 3:
            try:
                dataset.display_cross_table(DataSet.Stats.MAX)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 4:
            try:
                dataset.display_field_table(DataSet.Categories.LOCATION)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 5:
            try:
                dataset.display_field_table(
                    DataSet.Categories.PROPERTY_TYPE)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 6:
            try:
                manange_filters(dataset, DataSet.Categories.LOCATION)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 7:
            try:
                manange_filters(dataset,
                                DataSet.Categories.PROPERTY_TYPE)
            except EmptyDatasetError:
                print("Please load a dataset first.")
        elif selection == 8:
            dataset.load_file(filename)
            print("Data loaded!")
        elif selection == 9:
            print("Goodbye! Thank you for using the database\n")
            break
        else:
            print("Please enter a number between 1 and 9 only")
        print("\n")


def main():
    my_name = input("Please enter your name: ")
    message = "Hi " + my_name + ", Welcome to Foothill's database project"
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
            print("Header must be a string less than " + str(
                DataSet.header_length) + " characters long")
            continue
        break

    menu(air_bnb)


if __name__ == "__main__":
    main()

"""
--- sample run #1 ---
Please enter your name: Milap 
Hi Milap , Welcome to Foothill's database project
What is your home currency? USD
Enter a header for the menu: I'm done!

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

I'm done!
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
What is your choice? 8
Data loaded!


I'm done!
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
                    Entire home/apt       Private room        
Bronx               $ 127.51              $ 66.79               $ 59.80               
Brooklyn            $ 178.33              $ 76.50               $ 50.53               
Manhattan           $ 249.24              $ 116.78              $ 88.98               
Queens              $ 147.05              $ 71.76               $ 69.02               
Staten Island       $ 173.85              $ 62.29               $ 57.44               


I'm done!
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
What is your choice? 
"""