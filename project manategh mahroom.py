
class Person:
    # person class is
    name = ""
    birthdate = ""
    address = ""
    gender = ""
class Employee(Person):
    
    salary = 0
    work_hours = 0
    username = ""
    password= ""
    role= ""
    ispresent= None
    


    def presence(self, a):
        self.ispresent = a
        pass
    def change_password(self,password_tahgir):
        self.password = password_tahgir

class guys(Person,Employee):
    creativity=1
    teamwork=1
    projects_worked_on=1

class Tester(guys):
    problems_found = 1 #in range 0_ infinity
    def add_project(self):
        self.projects_worked_on+=1
    def change_creativity(self):
        if self.problems_found==10:
            self.creativity+=1
            self.problems_found=0
    
    def add_problemsfound(self):
        self.problems_found+=1
        self.change_creativity()
    
class Programmer(guys):
    lines_written= 1
    def add_project(self):
        self.projects_worked_on+=1
    def change_lines_written(self):
        self.lines_written+=1
        self.change_creativity2()
    def change_creativity2(self):
        if self.lines_written==100:

            self.creativity+=1
            self.lines_written=0

class Executive(Employee):
    def add_guys(self,role,name,birthdate,address,gender):
        if role=="Tester":
            new = Tester()   
        elif role=="Programmer":
            new = Programmer()
        new.name = name
        new.birthdate = birthdate
        new.address = address
        new.gender = gender
        
    add_guys(role="programmer",name="emp_1",birthdate="1990_0002030_40403030",address="kooche haye shahr",gender="male")
    def get_detail(self):
        x=input("enter employee name")
        if x == ("emp_1"):
            print(f"self.name")
            print(f"self.role")
Executive.get_detail()




















            


        






