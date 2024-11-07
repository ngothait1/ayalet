class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age
        self._frinds = []
        print(
            "Since you did not choose the choices offered in our database, your entry will be saved as a general person in the system."
        )

    def addFriend(self, name):
        self._frinds.append(name)
        print("friend edded.. ")

    def printFriends(self):
        for f in self._frinds:
            print(f)

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getFriends(self):
        return self._frinds

    def printPerson(self):
        print(
            "ID "
            + str(self.getId())
            + " belong to  "
            + self.getName()
            + ", "
            + str(self.getAge())
            + " years old. "
            # + " . Your friends are "
            # + str(self.getFriends())
        )

    def printMyself(self):
        self.printPerson()


# test|down

if __name__ == "__main__":
    print("Your running file Person.py")
    test_id = 101
    test_name = "Lulu"
    test_age = 18
    person = Person(test_id, test_name, test_age)
    # id =  Person.getId()
    if person.getId() != test_id:
        print(
            "something changed: "
            + str(test_id)
            + " should be the same as "
            + str(person.getId())
        )

    if person.getName() != test_name:
        print(
            "something changed: "
            + test_name
            + " should be the same as "
            + person.getName()
        )

    if person.getAge() != test_age:
        print(
            "something changed: "
            + str(test_age)
            + " should be the same as "
            + str(person.getAge())
        )

else:
    print("Your running export file (Person.py) ")
