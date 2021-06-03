#to create file
f=open("code_file.py","w")
f.write("print('this file is creared by file_sample')")
f.close()
#to read file
with open("code_file.py","r") as f:
    x=f.read()
print(x)