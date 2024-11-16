# class student
import utils
from class_Person import Person


class Student(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.field_of_study = input("What field are you studying? ")
        year_of_study = self.year_of_study = input("Years of study? (numbers only) ")
        while not utils.checkIfDigit(year_of_study):
            year_of_study = input(
                "ERROR: Enter yers of study *numbers only!* (example in month: 0.6)"
            )

    def getYear_of_study(self):
        return self.year_of_study

    def getField_of_study(self):
        return self.field_of_study

    def chekIfDigit(user_input):
        if not user_input.isdigit():
            print(
                "ERROR: Your input can only contain numbers ["
                + str(user_input)
                + "] is not a number"
            )
            return False
        return True

    def printStudent(self):
        super().printPerson()
        print(
            "years of study: "
            + str(self.getYear_of_study())
            + ", in the field: "
            + self.getField_of_study()
        )

    def printMyself(self):
        self.printStudent()

    def getInfoDictStuden(self):
        info = super().getInfoPersonDict()
        info.update(
            {
                "Field of study": self.getField_of_study(),
                "Years of study": self.getYear_of_study(),
            }
        )
        return info

    def getInfoDict(self):
        return self.getInfoDictStuden()


# test|down

if __name__ == "__main__":
    print("Your running file (Student.py) ")
    test_id = 101
    test_name = "Lulu"
    test_age = 18
    # test_field_of_study = "geography"
    # test_year_of_study = 1

    studet = Student(test_id, test_name, test_age)
    # #    Test was changed to input from user

    # if studet.getField_of_study() != test_field_of_study:
    #     print(
    #         "something changed: "
    #         + str(test_field_of_study)
    #         + " should be the same as "
    #         + str(studet.getField_of_study())
    #     )

    # if studet.getYear_of_study() != test_year_of_study:
    #     print(
    #         "something changed: "
    #         + str(test_year_of_study)
    #         + " should be the same as "
    #         + str(studet.getYear_of_study())
    #     )

    studet.printMyself()
    print(studet.getInfoDict())
else:
    print("Your running export file (Student.py) ")
