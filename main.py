class Employee:
    def __init__(self, company):
        self.company = company  #instance variable
    #company = "Infosys" #Class variable
    #def __init__(self): #instance methods (self is object of instance)
        #print("I am in Employee constructor")
    #def get_name(self): #instance methods
        #print("My name is Employee")
    def get_company(self):
        print(f"my company name is{self.company}")

    #@classmethod
    #def get_id(cls):
        #print("my id is one")  # class variable and class methods are accessed by class only

a = Employee("Infosys")
a.get_company()
b = Employee("tcs")
b.get_company()
#print(a.company)
#print(a.get_name())  #it printed none
#print(a.get_id())
#assert a is not b


