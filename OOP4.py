
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
    
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)

harsh=Employee("harsh","ruhil",50000000000000000)

print(harsh.__dict__)#prints all the attributes of the instance in the form of a dictionary

harsh.increment=10
print(harsh.__dict__)

print(Employee.__dict__)#prints all the attributes of employee class as a dictionary
print(harsh.salary)


Employee.change_increment(20)# the value of increment ghas changed for the whole "employee" class from 1.5 to 20 
harsh.increase()

print(harsh.salary)
lovish=Employee.from_str("lovish-jackson-16000")

print(lovish.fname)

#Let us understand the concept of inheritance here

class programmer(Employee): # this creates a programmer class that already has all the attributes and methods of the employee class and more
    def __init__(self,fname,lname,salary,proglang,exp):
        super(). __init__(fname,lname,salary)#Calls the init function of the super class i.e ERmployee here.
        self.proglang=proglang
        self.exp=exp

harry=programmer("harry","chadhha","10000","php","1yr")
print(harry.proglang)