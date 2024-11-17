# finel project - still in *TEST*

# import json
import os

import pandas as pd
import utils
from class_Employee import Employee
from class_Menu import Menu
from class_Person import Person
from class_Student import Student

global entries
entries = {}


def templateMenu():
    print("Menu to chose frome: ")
    for option in Menu:
        print(str(option.value) + ". " + option.name.replace("_", " ").title())


def saveNewEntry():
    person_types = [Employee, Student, Person]
    print("Save a new entry")
    user_type_selection = input(
        "Please choose: Enter '1' For employee entry '2' for student and '3' for person: "
    )
    if not utils.checkIfDigit(user_type_selection):
        return 0
    index = int(user_type_selection) - 1
    if index >= len(person_types):
        print("ERROR: Your choice out of range (1-3).")
        return
    elif index < 0:
        print("ERROR: Your choice must be a positive number (index >= 0).")
        return
    id_input = input("ID: ")
    if not utils.checkIfDigit(id_input):
        return 0
    if id_input in entries:
        print("ERROR: The ID " + id_input + " already exists.")
        return 0
    name_input = input("Name: ")
    age_input = input("Age: ")
    age_input = utils.outputInt(age_input)
    person = person_types[index](id_input, name_input, age_input)
    entries[id_input] = person
    print("ID [" + str(id_input) + "] saved successfuly!")
    return int(age_input)


def searchById():
    if not utils.checkLenInDict(entries):
        return
    id_to_search = input("Enter the ID you looking for: ")
    if not utils.checkIfDigit(id_to_search):
        return
    if id_to_search not in entries:
        print("ERROR: The ID [" + str(id_to_search) + "] was not found.")
        return
    entries[id_to_search].printMyself()


def calculatAgesAverage():
    people = []
    if len(entries) == 0:
        print("There's no entries yet, so no average age.")
    else:
        for person in entries.values():
            people.append(person)
        total_age = sum(int(person.getAge()) for person in people)
        average_ages = total_age / len(people)
        print("The average ages is : " + str(average_ages))


def printAllNames():
    if not utils.checkLenInDict(entries):
        return
    counter = 0
    print("All the names in the database: ")
    for name in entries.values():
        counter += 1
        print(str(counter) + ". " + name.getName())


def printAllId():
    counter = 0
    if not utils.checkLenInDict(entries):
        return
    for key in entries:
        counter += 1
        print(str(counter) + ". ID: " + key)


def printAllEntries():
    if not utils.checkLenInDict(entries):
        return
    print("Printing all entries: ")
    counter = 0
    for person in entries.values():
        counter += 1
        print(str(counter) + ".")
        person.printMyself()


def printEntryByIndex():
    if not utils.checkLenInDict(entries):
        return
    index_input = input("Enter index to print: ")
    if not utils.checkIfDigit(index_input):
        return
    index = int(index_input)
    if index < 0:
        print("ERROR: Index must be a positive number (index >= 0).")
        return
    if index >= len(entries):
        print("ERROR: index out of range")
        return
    for i, person in enumerate(entries.values()):
        if i == index:
            person.printMyself()
        # break
        # entries = dict name


def SaveAllEntris():
    try:
        data = []
        for person in entries.values():
            person_to_list = person.getInfoDict()
            data.append(person_to_list)
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
    except FileNotFoundError as e:
        print(e)
        print("ERROR: you have file Error when you try to save tha data. ")
    except PermissionError as e:
        print("Permission Error: " + str(e))
    except Exception as e:
        print("Unexpected Error: while saving the data | " + str(e))


def main():
    while True:
        templateMenu()
        choice = input("Choose an option: (number 1-8) ")
        if not utils.checkIfDigit(choice):
            continue
        if choice == Menu.SAVE_NEW_ENTRY:
            saveNewEntry()
        elif choice == Menu.SEARCH_BY_ID:
            searchById()
        elif choice == Menu.PRINT_AGES_AVERAGE:
            calculatAgesAverage()
        elif choice == Menu.PRINT_ALL_NAMES:
            printAllNames()
        elif choice == Menu.PRINT_ALL_IDS:
            printAllId()
        elif choice == Menu.PRINT_ALL_ENTRIES:
            printAllEntries()
        elif choice == Menu.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex()
        elif choice == Menu.SAVE_ENTRY_TO_CSV_FILE:
            SaveAllEntris()
        elif choice == Menu.EXIT:
            print("Thanks for using my DB, see you next time :)")
            break
        else:
            print("ERROR: Your option can be only numbers (1-8)")
        input("Press Enter to continue...")


try:
    main()
except KeyboardInterrupt as e:
    print(str(e) + " invalid keyboard input. ")
except Exception:
    print("Error: Unexpected error occurred")
finally:
    print("Thanks for using my DB, see you next time :)")
