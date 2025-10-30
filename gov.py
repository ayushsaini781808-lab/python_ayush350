# gov of india announce pension scheme for senior citizen scheme for female above 60 years,  annual income limit is 2 lakh

a=int(input("enter the age"))
b=int(input("enter the annual income"))
c=input("enter the gender (male/female)")

if a>60 and b<200000 and c=="female":
    print("Eligible for pension scheme")
else:
    print("Not eligible for pension scheme")