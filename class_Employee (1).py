# employee
# creating  Class employee
import utils
from class_Person import Person


class Employee(Person):
    def __init__(self, id, name, age, job_role=None, salary_amount=None):
        super().__init__(id, name, age)
        self.job_role = job_role if job_role else input("What is your job role? ")
        self.salary_amount = (
            salary_amount if salary_amount else input("Enter your salary amount:  ")
        )
        self.salary_amount = utils.outputInt(self.salary_amount)

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
    print("Your running the file")
    test_id = 101
    test_name = "Lulu"
    test_age = 18
    test_job_role = "soc analyst"
    test_salary_amount = "15000"

    employee = Employee(test_id, test_name, test_age, test_job_role, test_salary_amount)

    #    Test was changed to input from user
    if employee.getJobRole() != test_job_role:
        print(
            "Something changed!: "
            + test_job_role
            + " should be the same as "
            + employee.getJobRole()
        )

    if employee.getSalaryAmount() != test_salary_amount:
        print(
            "something changed!: "
            + str(test_salary_amount)
            + " should be the same as "
            + (employee.getSalaryAmount())
        )

    # Test for func getInfoDict
    info_dict = employee.getInfoDictEmployee()
    if info_dict["job role"] != employee.getJobRole():
        print("Job role - test failed!")
    if info_dict["salary amount"] != employee.getSalaryAmount():
        print("Salary amount - test failed!")
        print(
            info_dict["salary amount"]
            + " should be the same as "
            + employee.getSalaryAmount()
        )

    employee.printMyself()
    print(employee.getInfoDict())
else:
    print("Your running export file ")
