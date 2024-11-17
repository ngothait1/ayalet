# class student
import utils
from class_Person import Person


class Student(Person):
    def __init__(self, id, name, age, field_of_study=None, year_of_study=None):
        super().__init__(id, name, age)
        self.field_of_study = (
            field_of_study if field_of_study else input("What field are you studying? ")
        )
        self.year_of_study = (
            year_of_study if year_of_study else input("Years of study? (numbers only) ")
        )
        self.year_of_study = utils.outputInt(self.year_of_study)

    def getYearOfStudy(self):
        return self.year_of_study

    def getFieldOfStudy(self):
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
            + str(self.getYearOfStudy())
            + ", in the field: "
            + self.getFieldOfStudy()
        )

    def printMyself(self):
        self.printStudent()

    def getInfoDictStuden(self):
        info = super().getInfoPersonDict()
        info.update(
            {
                "Field of study": self.getFieldOfStudy(),
                "Years of study": self.getYearOfStudy(),
            }
        )
        return info

    def getInfoDict(self):
        return self.getInfoDictStuden()


# test|down

if __name__ == "__main__":
    print("Your running the file ")
    test_id = 101
    test_name = "Lulu"
    test_age = 18
    test_field_of_study = "geography"
    test_year_of_study = 1

    studet = Student(test_id, test_name, test_age)
    #    Test was changed to input from user

    if studet.getFieldOfStudy() != test_field_of_study:
        print(
            "something changed: "
            + str(test_field_of_study)
            + " should be the same as "
            + str(studet.getFieldOfStudy())
        )

    if studet.getYearOfStudy() != test_year_of_study:
        print(
            "something changed: "
            + str(test_year_of_study)
            + " should be the same as "
            + str(studet.getYearOfStudy())
        )
    info_dict = studet.getInfoDictStuden()
    if info_dict["Field of study"] != studet.getFieldOfStudy():
        print("Field of study - test failed! ")
    if info_dict["Years of study"] != studet.getYearOfStudy():
        print("Years of study - test failed!")

    studet.printMyself()
    print(studet.getInfoDict())
else:
    print("Your running export file ")
