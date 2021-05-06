# sum of 1 to 10 num
# 1+2+3+4+5.....+10

# # total = 0
# # for i in range(1,11):
# #     total += i
# # print(total)

# sum of user enter number

# # # n = int(input("Enter the number: "))
# # # total = 0
# # # for i in range(1, n+1):
# # #     total += i
# # # print(total)

# sum of user enter number # like "1254"----->"1+2+5+4"

# total = 0
# num= input("Enter a number: ")
# for i in range(0, len(num)):
#     total += int(num[i])
# print(total)

#practice for loop
# ask user name and count each character
#"Rishabh vishwakarma"
# R : 1
# i : 2
# s : 2
# h : 3
# a : 4
# b : 1
#   : 1
# v : 1
# w : 1
# k : 1
# r : 1
# m : 1

name = input("Please Enter your name: ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
