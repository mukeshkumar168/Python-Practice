class Stack:

    """Stack class
    Methods:
        push - push item in stack
        pop - pop last item 
        peek - top element
        display - return all elements
        is_empty - checks stack empty or not"""

    def __init__(self):
        self.stack = []  # declaring stack

    def push(self, item):   # add item in stack
        self.stack.append(item)
        print(f'Pushed: {item}')

    def pop(self):     # removing item in stack

        if not self.is_empty():
            item = self.stack.pop()
            print(f'Popped: {item}')
        else:
            print('stack is empty')

    def peek(self):     # Gets top element
        if not self.is_empty():
            print(f'Top stack: {self.stack[-1]}')

        else:
            print('stack is empty')

    def display(self):      # diplay all element
        if self.stack:
            print(f'Stack')
            for item in reversed(self.stack):
                print(item)

        else:
            print('stack is empty ')

    def is_empty(self):     # checks stack is empty
        return len(self.stack) == 0

# main function
if __name__ == "__main__":

    s = Stack()  #creating object

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        # user choice
        choice = input("Enter choice: ")

        if choice == '1':
            val = input("item: ")
            s.push(val)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")