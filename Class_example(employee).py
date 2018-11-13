class Employee:
    #Attribute (Adjective)

    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    # Verb (Method)
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")



def main():

    employeeOne = Employee()
    print(employeeOne.name)

    
main()
    
    
