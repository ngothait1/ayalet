import json
import os

import pandas as pd

from class_Employee import Employee
from class_Person import Person
from class_Student import Student


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


def checkLenInDict(entries):
    if len(entries) == 0:
        print("There's no entries yet")
        return False
    return True


def saveNewEntry(entries):
    person_types = [Employee, Student, Person]
    print("Save a new entry")
    user_type_selection = input(
        "Please choose: Enter '1' For employee entry '2' for student and '3' for person: "
    )
    if not chekIfDigit(user_type_selection):
        return 0
    index = int(user_type_selection) - 1
    if index >= len(person_types):
        print("ERROR: Index out of range.")
        return
    elif index < 0:
        print("ERROR: Index must be a positive number (index >= 0).")
        return
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
    person = person_types[index](id_input, name_input, age_input)
    entries[id_input] = person
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
    entries[id_to_search].printMyself()


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
    for name in entries.values():
        counter += 1
        print(str(counter) + ". " + name.getName())


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
        value.printMyself()


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
            value.printMyself()
        # break
        # entries = dict name


def SaveAllEntris(entries):
    data = []
    for val in entries.values():
        val_do_list = val.getInfoDict()
        data.append(val_do_list)
    user_input_filename = input(
        "choose a file name for saving your data. Use a .csv extension!  "
    )
    if not user_input_filename.endswith(".csv"):
        user_input_filename += ".csv"
    df = pd.DataFrame(data)
    save_path = os.path.join(
        "C:\\Users\\Ayele\\Downloads\\python_lessonse\\testing_files\\",
        user_input_filename,
    )
    # save_file to csv
    df.to_csv(save_path, index=False)
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
            # test for age| down
            if age is False or age is None:
                print("Invalid input. Please enter a valid number for age.")
                continue
            sum_of_ages += int(age)
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
            SaveAllEntris(entries)
        elif choice == "9":
            print("Thanks for using my DB, see you next time :)")
            break
        else:
            print("ERROR: Your option can be only numbers (1-8)")
        input("Press Enter to continue...")


main()
