# # check string is palandrome or not
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("madam"))  
# print(is_palindrome("hello"))  



# # 16-09-2025
# # delete character from string by index
# st="i love python"
# delete_char_index=2
# new_st=st[:delete_char_index]+st[delete_char_index+1:]
# print(new_st)


# # Capitalize first letter of each word in string
# st="hello world"
# stnew=st.capitalize()
# print(stnew)

# # casefold() return string in lowercase
# st="HELLO WORLD"
# stnew=st.casefold() 
# print(stnew)


# # count() no words in string

# st="i love what you like "
# n=st.count("i")
# print(n)

# # count no of substring in string
# st="i love what you like "
# n=st.count(" ")  
# print(n)

# # endswith() check string ends with given substring
# st="abes.ac.in"
# n=st.endswith(".in")
# print(n)


# # startwith()  

# st="abes.ac.in"
# print(st.startswith("abes"))


# # swapcase()

# st = "i like python"
# stnew=st.upper()
# print(stnew)

# # swapcase

# st = "i like python"
# stnew=st.swapcase()
# print(stnew)

# # tittle 

# st = "i like python"
# stnew=st.ti
# tle()
# print(stnew)


# replaced 

# st = "i like python"
# stnew=st.replace('python','java')
# print(stnew)

# # 16-09-2025
# #  write a progrm forsan each character byg loop

# st='mango'
# for i in range(len(st)):
#     print(st[i])

#     #  or 
#     st='mango'
#     for val in st:
#          print(val)

# # q1

# st = 'NH,Delhi Hapur By Pass Vijay Nagar 201009'
# alphabet = 0
# digit = 0 
# for val in st :
#     if val.isalpha():
#        alphabet=alphabet+1
#     elif val.isdigit():
#      digit +=1
# print("total no of alphabet",alphabet) 
# print("total no of digit",digit)          



# write a program to find the frequency of vowels in a string 

# s = input("Enter a string: ").lower()
# vowels = "aeiou"
# freq = {v: s.count(v) for v in vowels}

# print("Frequency of vowels:")
# for v, f in freq.items():
#     print(v, ":", f)



# write a program to find no of special symbol in a string whitespace should be ignored 

s = input("Enter a string: ")
count = 0

for ch in s:
    if not ch.isalnum() and not ch.isspace():  # not letter, not digit, not space
        count += 1

print("Number of special symbols:", count)

