class Employee:

    # The first to initialize
    def __init__(self):
        self.name = "Mark"
    #Now because of this __init__ above, Employee class automatically initializes attributes!

    #def employeeDetails(self):
        #self.name = "Mark"

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee()
employeeTwo = Employee()
employee.displayEmployeeDetails()
#this code above gives an error since employeeDetails() was never called => constructor comes into play!
employeeTwo.displayEmployeeDetails()
