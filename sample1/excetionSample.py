
num1=int(input("enter two numbers"))
num2=int(input())

try:
    result = num1 / num2
    print(str(num1)+"/"+str(num2)+"="+str(result))
    print("try Completed")
except:
    print("can't divided with zero")

print("program Completed")