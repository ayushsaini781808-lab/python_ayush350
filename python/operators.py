# arithmetic operators

# + : addition
# - : subtraction
# * : multiplication
# / : division
# % : modulus
# ** : exponentiation

# print(3/2)
# print(3//2)  # floor division
# print(3**2)
# print(2**3)
# print(3**2)
# print(3+2)
# print(3-2)
# print(3*2)
# print(float(3)%2)


#comaparison operator
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to

# a=20
# b=5
# x=2
# y=3
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# print(x>y)
# print(x<y)
# print(x==y)


#assignment operator
# = : assign
# += : add and assign
# -= : subtract and assign
# *= : multiply and assign
# /= : divide and assign
# %= : modulus and assign
# **= : exponentiation and assign


# a=10
# b=10
# a += 10
# print(a)
# b *= 2
# print(b)



#logical operator 

# and : logical AND    both true required
# or : logical OR     only 1 true condition required 
# not : logical NOT      result is reverse

# a=5
# b=10
# c=(a>b)and(b==10)
# d=(a>b)or(b==10)
# e=not((a>b)or(b==10))
# print(c)
# print(d)
# print(e)


#bitwise operator
# >> : bitwise right shift    y=n/2^4
# << : bitwise left shift     y= n*2^s

# & : bitwise and 
# ^ : bitwise xor 
# | : bitwise or 
#  ~ : bitwise not 

# a=10
# b=4

# print(a&b)
# print(a|b)
# print(~b)
# print(a^b)
# print(a>>2)
# print(a<<b)

# identiy operator 

# a= "college"
# b= "abes"
# c=['college','abes']
# d=['college','abes']
# e=c
# print(c is e)  #returns True because e is a same object as c
# print(c is not e)  #returns False because e is the same object as c
# print(c is not d)  #returns True because d is a same but use not  object  the memory location is different and differently assigned 


# membership operator 

# college ="abes" # direct assignment

# ['abes','college','engineering'] # list assignment

# a,b,c,d="abes"  #sequence assignment 

# a=b=college= "abes"  #multiple target assignment

# a=5
# a+=1  # augmented assignment

a,b,c,d='abes'
print(a)
print(b)
print(c)
print(d)    