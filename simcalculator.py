# wap in python to implement simple calculator
a=int(input("enter the first number"))  
b=int(input("enter the second number")) 
choice=int(input("1.addition\n2.subtraction\n3.multiplication\n4.division\n enter your choice"))
if choice==1:
    c=a+b
elif choice==2:
    c=a-b
elif choice==3:
    c=a*b
elif choice==4:
    c=a/b
else:
    print("Invalid choice")
print("Result:", c)
