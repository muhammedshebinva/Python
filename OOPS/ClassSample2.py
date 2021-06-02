
#differet objects have differnt memory spase

class DisplayName:
    def namePass(self,n):
        self.name=n
    def printName(self):
        print(self.name)

x=DisplayName()
y=DisplayName()

x.namePass("shebin")
y.namePass("adhil")

x.printName()
y.printName()