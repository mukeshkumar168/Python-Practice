def count_of_string(str):
    count = 0
    for char in str:
        count+= 1
    return count

str = input("Enter a string: ")
print(count_of_string(str))