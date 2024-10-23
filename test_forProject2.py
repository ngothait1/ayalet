# My_project  imports -> function -> code
import json
import os

import pandas as pd


def menu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save Entris to csv file")
    print("9. Exit")


def chekIfDigit(user_input):
    if not user_input.isdigit():
        print(
            "ERROR: Your input can only contain numbers ["
            + str(user_input)
            + "] is not a number"
        )
        return False
    return True


def printEntryLine(id, value):
    print("ID: " + str(id))
    print("Name: " + value[0])
    print("Age: " + str(value[1]))
    print(" ")


def checkLenInDict(entries):
    if len(entries) == 0:
        print("There's no entries yet")
        return False
    return True


def saveNewEntry(entries):
    print("Save a new entry")
    id_input = input("ID: ")
    if not chekIfDigit(id_input):
        return 0
    if id_input in entries:
        print("ERROR: The ID " + id_input + " already exists.")
        return 0
    name_input = input("Name: ")
    age_input = input("Age: ")
    while not chekIfDigit(age_input):
        age_input = input("Enter age (numbers only):")
    entries[id_input] = [name_input, age_input]
    print("ID [" + str(id_input) + "] saved successfuly!")
    return int(age_input)


def searchById(entries):
    if not checkLenInDict(entries):
        return
    id_to_search = input("Enter the ID you looking for: ")
    if not chekIfDigit(id_to_search):
        return
    if id_to_search not in entries:
        print("ERROR: The ID [" + str(id_to_search) + "] was not found.")
        return
    printEntryLine(id_to_search, entries[id_to_search])


def calculatAgesAverage(sum_of_ages, count_entris):
    if count_entris == 0:
        print("There's no entries yet, so no average age.")
    else:
        average_ages = sum_of_ages / count_entris
        print("The average ages is : " + str(average_ages))


def printAllNames(entries):
    if not checkLenInDict(entries):
        return
    counter = 0
    print("All the names in the database: ")
    for value in entries.values():
        counter += 1
        print(str(counter) + ". " + value[0])


def printAllId(entries):
    counter = 0
    if not checkLenInDict(entries):
        return
    for key in entries:
        counter += 1
        print(str(counter) + ". ID: " + key)


def printAllEntries(entries):
    if not checkLenInDict(entries):
        return
    print("Printing all entries: ")
    counter = 0
    for key, value in entries.items():
        counter += 1
        print(str(counter) + ".")
        printEntryLine(key, value)


def printEntryByIndex(entries):
    if not checkLenInDict(entries):
        return
    index_input = input("Enter index to print: ")
    if not chekIfDigit(index_input):
        return
    index = int(index_input)
    if index < 0:
        print("ERROR: Index must be a positive number (index >= 0).")
        return
    if index >= len(entries):
        print("ERROR: index out of range")
        return
    for i, (key, value) in enumerate(entries.items()):
        if i == index:
            printEntryLine(key, value)
            break
        # entries = dict name


def SaveAllentris(entries):
    path_conf_file = (
        "C:\\Users\\Ayele\\Downloads\\python_lessonse\\testing_files\\conf.json"
    )
    with open(path_conf_file) as conf_file:
        loded_conf_file = json.load(conf_file)
        column_id = loded_conf_file["ID"]
        column_name = loded_conf_file["Name"]
        column_age = loded_conf_file["Age"]

    data = []
    for key, value in entries.items():
        data.append({column_id: key, column_name: value[0], column_age: value[1]})

    userInput_FileName = input(
        "choose a file name for saving your data. Use a .csv extension!  "
    )
    if not userInput_FileName.endswith(".csv"):
        userInput_FileName += ".csv"
    current_user_path = os.getcwd()
    if os.path.exists(current_user_path) == False:
        print(
            "Error: Conf.json is missing in path "
            + current_user_path
            + " (Try cd command for the right path)"
        )
    df = pd.DataFrame(data)
    df.to_csv(
        "C:\\Users\\Ayele\\Downloads\\python_lessonse\\testing_files\\"
        + userInput_FileName,
        index=False,
    )
    print("File saved successfully ")


def main():
    count_entris = 0
    entries = {}
    sum_of_ages = 0
    while True:
        menu()
        choice = input("Choose an option: (number 1-8) ")
        if not chekIfDigit(choice):
            continue
        if choice == "1":
            age = saveNewEntry(entries)
            sum_of_ages += age
            count_entris += 1
        elif choice == "2":
            searchById(entries)
        elif choice == "3":
            calculatAgesAverage(sum_of_ages, count_entris)
        elif choice == "4":
            printAllNames(entries)
        elif choice == "5":
            printAllId(entries)
        elif choice == "6":
            printAllEntries(entries)
        elif choice == "7":
            printEntryByIndex(entries)
        elif choice == "8":
            SaveAllentris(entries)
        elif choice == "9":
            print("Thanks for using my DB, see you next time :)")
            break
        else:
            print("ERROR: Your option can be only numbers (1-8)")
        input("Press Enter to continue...")


main()
