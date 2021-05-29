#with out argument with out return value
def display():
    print("hello world")

display()

#with argument with out return value
def name(name):
    print("name : "+name)

name("shebin")

#with argument with return value
def sum(num1, num2):
    sum = int(num1) + int(num2)
    return sum

result = sum(10, 10)
print("result= "+str(result))

#with out argument with return value

def show():
    firstName="shebin"
    lastName="vs"

    fullName=firstName+lastName
    return fullName

Fname=show()
print("name: "+ Fname)

#function
def address(name, palce="wayanad"):
    print(" name:"+name+" \n place:"+palce)
address("shebin")