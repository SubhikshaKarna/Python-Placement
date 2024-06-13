class Person(object):

    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print(f"My name is{self.name}")
        print(f"IdNumber: {self.idnumber}")

#child class

class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary 
        self.post=post
        Person.__init__(self,name,idnumber)
    
    def details(self):
        print(f"My name is {self.name}")
        print(f"IdNumber:{self.idnumber}")
        print(f"Post:{self.post}")

#Creation of an object variable or an instance

a=Employee('Rahul',886012,200000,"Intern")
a.display()
a.details()