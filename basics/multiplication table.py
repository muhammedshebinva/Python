
number = int(input("enter the number"))
limit = int(input('enter the limit'))
limit = limit + 1
for x in range(1 , limit):
    result = int(x) * number
    print(str(x)+ 'x' +str(number)+ ' = ' + str(result))