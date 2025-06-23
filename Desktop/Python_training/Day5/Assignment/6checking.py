def checking(s, item):

    """Checks item in the set"""

    if item in s:
        return 'found'
    else:
        return 'not found'

book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"} 
items = "Angels and Demons"
print(checking(book_set, items))