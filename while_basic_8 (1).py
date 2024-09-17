def countTo_while(max_number):
    number = 0
    while number <= max_number:
        print(number)
        number += 1

def countTo_for(max_number):
    for number in range(max_number + 1):
        print(number)

def feedList_2():
    names = []
    user_input = input("Please write name: ")
    while user_input != "stop":
        names.append(user_input)
        user_input = input("Please write name: ")
    print(names)

def iterateList_while(input_list):
    index = 0
    while index < len(input_list):
        print(input_list[index])
        index += 1

def count_toMax(max_number):
    number = 0
    while number <= max_number:
        print(number)
        number += 1 

def feedList_1():
    food = []
    while True:
        user_input = input("Enter food you like: ")
        food.append(user_input)
        if user_input == "stop":
            return food

def feedList():
    food = []
    user_input = input("Enter food you like: ")
    while user_input != "stop":
        food.append(user_input)
        user_input = input("Enter food you like: ")
    return food

def iterate_list(input_list):
    index = 0
    while index < len(input_list):
        print(input_list[index])
        index += 1

def creatYourDict():
    output_dict = {}
    while True:
        key_input = input("Enter a key for the dictinery or stop to finish: ")
        if key_input == "stop":
            break
        value_input = input("Enter a value for the dictinery: ")
        output_dict[key_input]=value_input
    return output_dict

print(creatYourDict())

test = [1, 2, 3, 4, 5, 6, 7]
iterate_list(test)

while True:
    user_input = input("Do you whant to continue? y/n: ")
    if user_input == "y":
        print("Ok, continue")
        break
    elif user_input == "n":
        print("Ok, we stop")
        break