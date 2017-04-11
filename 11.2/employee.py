# the Employee class holds general information
# about the employees name and number
# it will be the parent class for ProductionWorker class


class Employee(object):
    """
        accepts employee_name and employee_number
    """
    def __init__(self, employee_name="", employee_number=0):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # Add Mutator Methods
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # Add Accessor Methods
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def __str__(self):
        emp_info = "Employee Name: " + self.__employee_name + \
                   "Employee Number: " + str(self.__employee_number)
        return emp_info

# The ProductionWorker class represents a subclass of the Employee class
# The __init__ method accepts arguments for employee_name and employee_number


class ProductionWorker(Employee):
    """
        The ProductionWorker class extends the Employee class and
        adds the additional methods shift and rate
    """
    def __init__(self, employee_name, employee_number, shift, rate):

        Employee.__init__(self, employee_name, employee_number)
        # will call the parent class and pass arguments to it

        # Initialize shift and rate
        self.__shift = shift
        self.__rate = rate

    # Add Mutator Methods

    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

    # Add Accessor Methods

    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate

    def __str__(self):
            emp_info = "Employee Name: " + self.get_employee_name() + \
                       "\nEmployee Number: " + str(self.get_employee_number()) + \
                       "\nShift: " + str(self.__shift) + \
                       "\nHourly Rate: " + str(self.__rate)
            return emp_info
