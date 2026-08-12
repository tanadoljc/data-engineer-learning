class company():

    def __init__(self, com_name):
        self.com_name = com_name

    def company_info(self):
        print(f"Company name is {self.com_name}")

class country():

    def __init__(self, country_name):
        self.country_name = country_name

    def country_info(self):
        print(f"Country name is {self.country_name}")

class employee(company, country):

    def __init__(self, emp_name, com_name, country_name):
        self.emp_name = emp_name

        company.__init__(self, com_name)
        country.__init__(self, country_name)

    def emp_info(self):
        print(f"Employee name is {self.emp_name}")

    def full_info(self):
        print(f"This employee name is {self.emp_name} from {self.country_name} and works for {self.com_name}")

    def all_info_child(self):
        print("This is running from employee")
        company.company_info(self)
        country.country_info(self)
        # super().company_info()

emp1 = employee("Matthew", "ABC", "TH")

emp1.full_info()
emp1.all_info_child()