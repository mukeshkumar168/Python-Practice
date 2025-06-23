try:
    
    str1 = "Emma is a data scientist who knows Python. Emma works at google."
    sub = "Emma"

    # Find the last occurrence
    position = str1.rfind(sub)

    if position != -1:
        print(f"Last occurrence at index: {position}")
    else:
        print(f"'{sub}' not found .")

except Exception as e:
    print(f"Error: {e}")
