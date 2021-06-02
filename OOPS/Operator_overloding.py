class Name_Printing:
    def set_name(self, name):
        self.name=name
    #Special add Function
    def __add__(self, other):
        name=self.name+" "+other.name
        return name

first_name=Name_Printing()
second_name=Name_Printing()

first_name.set_name("Adhil")
second_name.set_name("Basheer")

full_name=first_name+second_name
print(full_name)