#My_project  imports -> function -> code
def menu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")

def saveNewEntry(entries):
    id_input = input("ID: ")
    if not id_input.isdigit():
        print("ERROR: Your ID can only contain numbers " + str(id_input) + " is not a number")
        input("Press Enter to continue...")
        return None
    if id_input in entries:
        print("ERROR: The ID " + str(id_input) + " already exists.")
        input("Press Enter to continue...")            #creat function ToContinue 
        return None
    else: 
        name_input = input("Name: ")
    age_input = input("Age: ")
    if not age_input.isdigit():
        print(f"ERROR: Age must be a number. ['{age_input}'] is not valid.")
        age_input = 0
        input("Press Enter to continue...")
        return None
    else:
        entries[id_input] = [name_input, age_input]
        print("ID [" + str(id_input) + "] saved successfuly!")
        input("Press Enter to continue...")
        return int(age_input)

def searchById(entries):
    id_to_search = input("Enter the ID you looking for: ")
    if not id_to_search.isdigit():
        print(f"ERROR: ID must be a number. ['{id_to_search}'] is not valid.")
    elif id_to_search not in entries:
        print(f"ERROR: The ID ['{id_to_search}'] was not found.")
    else:
        return "ID found:" + entries[id_to_search]
    
#def calculatAgesAverage(entries,):

def printAllNames(entries):
    for name in entries.values():
        name = entries[0]
        if len(entries) == 0:
            print("There's no entries yet, so no names to print.")
            return
        else:
            print("All the names in the database: ")
            print(name)

def printAllId(entries):
    if len(entries) == 0:
        print("There's no entries yet, so no ID's to print.")
        return
    else:
        for key in entries:
            print(key)

def PrintAllEntries(entries):
    for id, values in entries.items():
        print("ID: " + str(id))
        print("Name: " + str(values[0] ))
        print("Age: " + str(values[1] ))
        print(" ")

def PrintEntryByIndex(entries):
    index_input = input("Enter index to print: ")
    if not index_input.isdigit():
        print("ERROR: Index must be a positive number.")
        return
    index = int(index_input)
    if index < 0 :
        print("ERROR: index must be a positive number (index >= 0)")
        return
    elif index >= len(entries):                                            #להשאיר את המינוס אחד?
        print("ERROR: index out of range")
        return
    else:
        entry = list(entries.items())[index]
        print("ID: " + str(entry[0]) + " Name: " + str(entry[1][0]) + " Age: " + str(entry[1][1]))

def main():
    entries = {}
    sum_of_ages = 0
    age_count = 0
    while True:
        menu()
        choice = input("Choose an option: ")
        if not choice.isdigit():
            print("ERROR: Your option can be only numbers (1-8)")
            continue
        if choice == '1':
            print("Save a new entry")
            age = saveNewEntry(entries)
            if age is not None: 
                sum_of_ages += age
                age_count += 1
        elif choice == '2':
            print("Search by ID")
            searchById(entries)
        elif choice == '3':
            print("Print ages average")
            if age_count == 0:
                print("There's no entries yet, so no average age.")
                return
            else:
                ages_average = sum_of_ages/age_count
                print("The average age is: " + str(ages_average))
        elif choice == '4':
            print("Print all names: ")
            printAllNames(entries)
        elif choice == '5':
            print("Print all IDs: ")
            printAllId(entries)
        elif choice == '6':
            print("Printing all entries: ")
            PrintAllEntries(entries)
        elif choice == '7':
            PrintEntryByIndex(entries)
        elif choice == '8':
            print("Thanks for using my DB, see you next time :)")
            break 
        else:
            print("ERROR: Your option can be only numbers (1-8)")

main()
