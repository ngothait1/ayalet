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

def chekIfDigit(user_input):
    if not user_input.isdigit():
        print("ERROR: Your input can only contain numbers [" + str(user_input) + "] is not a number")
        return False
    return True

def saveNewEntry(entries):
    id_input = input("ID: ")
    if not chekIfDigit(id_input):
        return 0
    if id_input in entries:
        print("ERROR: The ID " + id_input + " already exists.")
        return 0
    else: 
        name_input = input("Name: ")
    age_input = input("Age: ")
    if not chekIfDigit(age_input):
        return 0
    entries[id_input] = [name_input, age_input]
    print("ID [" + str(id_input) + "] saved successfuly!")
    return int(age_input)

def searchById(entries):
    id_to_search = input("Enter the ID you looking for: ")
    if not chekIfDigit(id_to_search):
        return 
    if id_to_search not in entries:
        print("ERROR: The ID [" + str(id_to_search) + "] was not found.")
        return
    else:
        print("ID found:" + str(entries[id_to_search]))
    
def calculatAgesAverage(sum_of_ages, count_entris):
    if count_entris == 0:
        print("There's no entries yet, so no average age.")
    else:
        average_ages = sum_of_ages / count_entris
        print("The average ages is : " + str(average_ages))

def printAllNames(entries):
        counter = 0
        if len(entries) == 0:
            print("There's no entries yet, so no names to print.")
            return
        else:
            print("All the names in the database: ")
            for value in entries.values():
                counter += 1
                print(str(counter) +". "+ value[0])

def printAllId(entries):
    counter = 0
    if len(entries) == 0:
        print("There's no entries yet, so no ID's to print.")
        return
    else:
        for key in entries:
            counter += 1
            print(str(counter) + " ID: "+ key)

def printAllEntries(entries):
    counter = 0
    for id, values in entries.items():
        counter += 1
        print(str(counter) + ". ID: " + str(id)) 
        print("Name: " + values[0])
        print("Age: " + str(values[1]))
        print(" ")

def printEntryByIndex(entries):
    index_input = input("Enter index to print: ")
    if not chekIfDigit(index_input):
        return
    index = int(index_input)
    if index < 0 :
        print("ERROR: Index must be a positive number (index >= 0).")
        return
    elif index >= len(entries):                                           
        print("ERROR: index out of range")
        return
    else:
        counter_index = 0
        for key, values in entries.items():
            counter_index += 1
            if counter_index == index:
                print("ID: " + key)
                print("Name: " + values[0])
                print("Age: " + str(values[1]))
def main():
    entries = {"101": ["sivan", 56], "102":["amos", 63], "103":["reut", 31]}
    sum_of_ages = 0
    count_entris = 0
    while True:
        menu()
        choice = input("Choose an option: (number 1-8) ")
        chekIfDigit(choice)
        if choice == '1':
            print("Save a new entry")
            age = saveNewEntry(entries) 
            sum_of_ages += age
            count_entris += 1
        elif choice == '2':
            print("Search by ID")
            searchById(entries)
        elif choice == '3':
            print("Print ages average")
            calculatAgesAverage(sum_of_ages, count_entris)
        elif choice == '4':
            print("Print all names: ")
            printAllNames(entries)
        elif choice == '5':
            print("Print all IDs: ")
            printAllId(entries)
        elif choice == '6':
            print("Printing all entries: ")
            printAllEntries(entries)
        elif choice == '7':
            printEntryByIndex(entries)

        elif choice == '8':
            print("Thanks for using my DB, see you next time :)")
            break 
        else:
            print("ERROR: Your option can be only numbers (1-8)")
        input("Press Enter to continue...")

main()
