"""# count digit letter symbol"""
#  def find_counts(s):
#     digit_count = 0
#     letter_count = 0
#     symbol_count = 0

#     for i in s:
#         if i.isalpha():
#             letter_count+=1
#         elif i.isdigit():
#             digit_count+=1
#         else:
#             symbol_count+=1

#     print(f'digits: {digit_count} letter: {letter_count} symbol: {symbol_count}')

# s = "P@yn2at&#i5ve"
# find_counts(s)


"""# remove duplicates"""
# def remove_duplicates(input_string):
 

#     return "".join(sorted(set(input_string)))

# s = 'hello'
# print(remove_duplicates(s))


"""# email checking"""
# import re
# def is_valid_email(email):
#     pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
#     return bool(re.match(pattern, email))

# email = 'abc@gmail.com'
# print(is_valid_email(email))



"""# Find Day of Week"""
# from datetime import datetime

# given_date = datetime(2020, 7, 26)

# print(given_date.today().weekday())

# print(given_date.strftime('%A'))


"""Calculate the date 4 months from the current date"""
# from datetime import datetime

# from dateutil.relativedelta import relativedelta


# given_date = datetime(2020, 2, 25).date()

# add_month = 4
# new_date = given_date + relativedelta(months = add_month)
# print(new_date)


"""Days Until New Year"""

# from datetime import datetime

# today = datetime.now()
# print(today)
# next_new_year = datetime(today.year + 1, 1, 1) # 2026-01-01

# days_until_new_year = (next_new_year - today).days  

# print(f"{days_until_new_year} days until New Year")


    

""" Adding Hours to Time"""
# from datetime import datetime, timedelta

# input_time = input("time (HH:MM): ")
# hours_add = int(input("hours to add: "))


# time = datetime.strptime(input_time, "%H:%M")

# new_time = time + timedelta(hours=hours_add)


# print("New time:", new_time.strftime("%H:%M"))