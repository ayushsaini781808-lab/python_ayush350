# grade divisions for student honor above 95,first bw 60-95,second bw 30-60,fail below 30
a=int(input("enter the marks")) 
if a>=95:
    print("Grade: Honor")
elif a>60 and a<=95:
    print("Grade: First")
elif a>30 and a<=60:
    print("Grade: Second")
else:
    print("Grade: Fail")
