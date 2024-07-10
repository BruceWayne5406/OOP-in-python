
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
    
    def __repr__(self): #used to represent the value you want to print or return in a particular syntax
        return f"Employee({self.fname},{self.lname},{self.salary})"
    
    
        

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


harry=Employee("harry","chadhha","10000")
print(harry.fname)
print(harry.lname)

#let us understand dunder methods a.k.a magic functions
#functions involving __ __ come under this category
#for eg. __init__(), __repr__(), __str__()

print(harry.__repr__())



