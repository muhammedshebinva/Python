class BaseClass:
    def __init__(self):
        print("Base Init")

    def hello(self):
        print("hello")


class SubClass(BaseClass):
    # if we create a constructor to sub class only the sub class constroctor
    # will works. this is known as method/ constructor over riding
    def __init__(self):
        print("SubClass Init")
    #to call the base init constructor use classname.__init__(self) or super().__init__()
        # to solve Over Riding
        super().__init__()

    def hai(self):
        print("hai")


# if we called the subclass which inheritad the base class conatin an
# Constructor then the base class constructor calls
x = SubClass()
x.hai()
