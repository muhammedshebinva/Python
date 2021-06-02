class BaseClass:
    def display(self):
        print("Hello")

    def displayName(self):
        print(self.name)

    def setName(self,name):
        self.name = name
    def displayName(self):
        print("name:"+self.name)

class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")

a = BaseClass()
a.display()

b = SubClass()
b.display()
b.welcome()

b.setName("Adhil")
b.displayName()