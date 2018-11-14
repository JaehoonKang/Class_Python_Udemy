class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name= ", self.name)
        # age only exists in this method of employeeDetails
        age = 30
        print("Age =". age)

    #Instance Method
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ", self.name)

        # age cannot be accessed here => self needs to be defined
        print("Age: ", age)

    # this doesn't need any parameter => @staticmethod comes into play
    @staticmethod
    def welcomeMessage():
        print("Welcome")

employee = Employee()
employee.employeeDetails()
employee.welcomeMessage()
