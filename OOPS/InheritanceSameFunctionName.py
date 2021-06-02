class First:
    def display(self):
        print("First")


class Second:
    def display(self):
        print("Second")


class Third(First, Second):
    def display_third(self):
        print("Third")

x = Third()
x.display_third()
#here the function names are same in first and second classes so the left one calls, from class Third(First, Second)
x.display()

print(Third.mro())