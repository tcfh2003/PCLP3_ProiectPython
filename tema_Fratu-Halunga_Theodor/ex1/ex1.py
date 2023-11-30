from employee import Employee

# Fratu-Halunga Theodor-Corneliu => X = 12 , Y = 15

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = 'F01' + str(department)

    def display_employee(self):
        print("Name : ", self.name)


def __main__():
    manager_list = []
    for i in range(5):
        print("Provide details for Manager " + str(i))
        name = input("Name : ")
        salary = input("Salary : ")
        department = input("Department : ")
        manager_list.append(Manager(name, salary, department))
        print('\n')

    for manager in manager_list:
        print("display_employee() din clasa Manager: ")
        manager.display_employee()

        employee = Employee(manager.name, manager.salary)
        print("display_employee() din clasa Employee: ")
        employee.display_employee()

        print('\n')

    print("Pentru Manager, emp_count = ", manager_list[0].empCount)
    print("Pentru Employee, emp_count = ", Employee(manager_list[0].name, manager_list[0].salary).empCount)


if __name__ == '__main__':
    __main__()