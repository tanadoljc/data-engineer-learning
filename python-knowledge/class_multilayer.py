class company():

    def __init__(self, com_name):
        self.com_name = com_name

    def company_info(self):
        print(f"Company name is {self.com_name}")

class department(company):

    def __init__(self, dept_name, com_name):
        self.dept_name = dept_name
        company.__init__(self, com_name)

    def dept_info(self):
        print(f"This employee is from {self.dept_name} and works for {self.com_name}")

class employee(department):

    def __init__(self, emp_name, dept_name, com_name):
        self.emp_name = emp_name
        department.__init__(self,dept_name, com_name)

    def all_info(self):
        print(f"This employee name is {self.emp_name} of {self.dept_name} Department from {self.com_name}")

emp1 = employee("Matthew", "CPE", "Chula")

emp1.company_info()