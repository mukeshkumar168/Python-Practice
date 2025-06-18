"""#  double each character in a string """
# def double(s):

#     res = ''
#     for i in s:
#         res += i * 2
#     return res

# if __name__ == '__main__':
#     s = "hello"
#     print(double(s))



"""# arrange lower to upper"""
# s = "HelloWorld"

# low = []
# upp = []
# for i in s:
#     if i.islower():
#         low.append(i)
#     else:
#         upp.append(i)

# sorted_string = ''.join(low + upp)
# print(sorted_string)  



"""# count the number of substring"""
# str1 = "Welcome to USA. usa awesome, isn't it?"
# sub_string = "USA"

# temp_str = str1.lower()

# count = temp_str.count(sub_string.lower())
# print("USA count: ", count)



"""# find the sum in the string """
# input_str = "PYnative29@#8496"
# total = 0

# for i in input_str:
#     if i.isdigit():
#         total += int(i)

# print("Sum :", total)
