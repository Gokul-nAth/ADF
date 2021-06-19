class Employee:
    def __init__(self,name,age,gender,salary,state,city):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
        self.state=state
        self.city=city

    def printDetails(self):
        print('\nEmployee name \t: '+self.name+'\nEmployee age\t:',self.age,'\nEmployee gender\t: '+self.gender+'\nEmployee salary\t:',self.salary,'\nEmployee state\t: '+self.state+'\nEmployee city\t: '+self.city)
try:
    t=int(input('Enter the number of students : '))
    for i in range(0,t):
        try:
            name=input('Enter the name : ')
            if(name.isdigit()):
                print('Name should not contain numerical values')
                raise ValueError
            if(len(name)<3):
                print('Name should contains more than 2 characters')
                raise ValueError
            age=int(input('Enter the age : '))
            if(age<18 or age>60):
                print('Age should be (>)18 or (<)60')
                raise ValueError
            gender=input('Enter the gender : ')
            if(gender.lower()!='male' or gender.lower()!='female' or gender.lower()!='others'):
                print('Gender must be either Male/Female/Others')
                raise ValueError
            salary=int(input('Enter the salary : '))
            if(salary<10000 or salary>60000):
                print('Salary should be (>)10000 or (<)60000')
                raise ValueError
            state=input('Enter the state : ')
            if(len(state)>5):
                print('Enter a valid state name')
                raise ValueError
            city=input('Enter the city : ')
            if(len(city)):
                print('Enter a valid city name')
                raise ValueError
            object=Employee(name,age,gender,salary,salary,city)
            object.printDetails()
        except ValueError:
            print('Invalid value entered')
except ValueError:
    print('Enter a valid numerical value')