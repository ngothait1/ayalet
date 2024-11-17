import utils


class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

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
            + " belong to "
            + self.getName()
            + ", "
            + str(self.getAge())
            + " years old. "
            # + " . Your friends are "
            # + str(self.getFriends())
        )

    def printMyself(self):
        self.printPerson()

    def getInfoPersonDict(self):
        info_dict_Person = {"id": self._id, "name": self._name, "age": self._age}
        return info_dict_Person

    def getInfoDict(self):
        return self.getInfoPersonDict()


# test|down

if __name__ == "__main__":
    print("Your running the file ")
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
    info_dict = person.getInfoDict()
    if info_dict["id"] != person.getId():
        print("ID - test failed!")
    if info_dict["name"] != test_name:
        print("Name - test failed!")
    if info_dict["age"] != test_age:
        print("Age in dictionary test failed!")

else:
    print("Your running export file ")
