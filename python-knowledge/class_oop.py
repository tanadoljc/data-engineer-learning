class employee():

    # class attribute
    company_name = 'XYZ'

    def __init__(self, emp_name, emp_dept):
        # instance attribute
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # Instance Method: must have 'self', have to declare var (Alternative way)
    def changes(self, company_name):
        self.company_name = company_name

    @classmethod # does not have to declare var first, just call directly
    def changesInClass(cls, company_name):
        cls.company_name = company_name

    @staticmethod      # add this line then it'll sent 'N+1'  param (a,b,emp1)
    def addition(a,b): # not require 'self', not relevant
        return a+b
    
    @property # This is getter
    def info(self):
        print(f"Employey {self.emp_name} works for {self.emp_dept}")

    @info.setter # This is setter
    def info(self, emp_details): # able to pass only '1' value (list)
        self.emp_name = emp_details[0]
        self.emp_dept = emp_details[1]


emp1 = employee("Matthew", "IT")
emp1.info = ["Most", "Dev"]

emp1.info