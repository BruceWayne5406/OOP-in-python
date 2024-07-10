
#Here we are creating an employee class
class Employee:
    increment=1.5

    def __init__(self,fname,lname,salary):#constructor function
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def increase(self):
        self.salary=self.salary*self.increment
    
    @classmethod#class methods are used to modify the code for a class,that is why they take the whole class as a parameter instead of taking self as a pareameter
    def change_increment(cls,amount):
        cls.increment=amount

harsh=Employee("harsh","ruhil",50000000000000000)

print(harsh.__dict__)#prints all the attributes of the instance in the form of a dictionary

harsh.increment=10
print(harsh.__dict__)

print(Employee.__dict__)#prints all the attributes of employee class as a dictionary
print(harsh.salary)


Employee.change_increment(20)# the value of increment ghas changed for the whole "employee" class from 1.5 to 20 
harsh.increase()

print(harsh.salary)
