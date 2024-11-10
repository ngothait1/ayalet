# employee
# creating  Class employee
from class_Person import Person


class Employee(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.job_role = input("What is your job role?  ")
        self.salary_amount = input("Enter your salary amount:  ")

    def getJobRole(self):
        return self.job_role

    def getSalaryAmount(self):
        return self.salary_amount

    def printEmployee(self):
        super().printPerson()
        print(
            "job position "
            + self.getJobRole()
            + ", with a salary amount "
            + str(self.getSalaryAmount())
        )

    def printMyself(self):
        self.printEmployee()

    def getInfoDictEmployee(self):
        info = super().getInfoPersonDict()
        info.update(
            {"job role": self.getJobRole(), "salary amount": self.getSalaryAmount()}
        )
        return info

    def getInfoDict(self):
        return self.getInfoDictEmployee()


# test|down

if __name__ == "__main__":
    print("Your running file Employee.py")
    test_id = 101
    test_name = "Lulu"
    test_age = 18

    employee = Employee(test_id, test_name, test_age)

    ##    Test was changed to input from user
    # if employee.getJobRole() != test_job_role:
    #     print(
    #         "something changed!: "
    #         + test_job_role
    #         + " should be the same as "
    #         + employee.getJobRole()
    #     )

    # if employee.getSalaryAmount() != test_salary_amount:
    #     print(
    #         "something changed!: "
    #         + str(test_salary_amount)
    #         + " should be the same as "
    #         + (employee.getSalaryAmount())
    #     )

    employee.printMyself()
    print(employee.getInfoDict())
else:
    print("Your running export file (Employee.py) ")
