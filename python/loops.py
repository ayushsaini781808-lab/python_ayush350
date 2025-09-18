
# # write a program to print all even numbers from 75 to 150 
# i=75
# while(i<=150):
#     if(i%2==0):
#         print(i)
#     i=i+1


# print natural numbers using for loop
# i=1
# n=int(input("enter a number"))
# while(i<=n):
#     print(i)
#     i=i+1

# 10-sep-2025
# table of 5 by for loop

# print pattern 1*5,2*5,3*5

# n=int(input("enter a number"))
# for i in range(1,11):   
#     print(i, "*" , n ,"=" ,i*n)



    # pattern print 3 * in 3 lines 


# for i in range(1,4):
#     print("*"*3)



    # pattern print by nested for loop without 
    # ***
    # ***
    # ***


# char='*'
# for i in range(3):
#     for j in range(3):
#         print(char,end="")
#     print()

# print pattern 
# ***
# **
# *

# char = '*'
# for i in range(3):
#     for j in range(1, 4-i):
#         print(char,end=" ")
#     print()


# print pattern 
# *
# **
# ***

# char = '*'
# for i in range(3):
#     print(char * (i + 1))


    # print pattern
    # ***
    # **
    # *


# char = '*'
# for i in range(3):    
#     print(char * (3 - i))


# print pattern
#   --*
#   -**
#   ***

# char = '*'
# for i in range(3):
#     for j in range(3-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(char,end="")
#     print()


# print pattern
# ***
# -**   
# --*

# char = '*'
# for i in range(3):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(3-i):
#         print(char,end="")
#     print()



# pattern reverse pyramid
#     * * * *
#      * * *
#       * *
#        *

# 11-sep-2025

# char = '*'
# for i in range(4):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(4-i):
#         print(char,end=" ")
#     print()


# A=10
# C=35
# B=25
# if(A+B-C):
#     print("true")
# else:
#     print("false")


for i in (2,4):
    print(i)
    # answer is 2,4 because range is not used here