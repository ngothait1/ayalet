# tools to use in projects | by Ayelet


def checkIfDigit(user_input):
    if not user_input.isdigit():
        print(
            "ERROR: Your input can only contain numbers ["
            + str(user_input)
            + "] is not a number"
        )
        return False
    return True


def checkLenInDict(dict_name):
    if len(dict_name) == 0:
        print("There's no entries yet")
        return False
    return True


def outputInt(user_input):
    while not checkIfDigit(user_input):
        user_input = input("ERROR: Enter numbers only: ")
    return user_input
