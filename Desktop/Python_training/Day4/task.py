def add_task(queue):
    """
        Function add task to the queue
        returns:
            str: Task added
    """

    task = input('Enter Task: ')
    queue.append(task)
    print('Task added')

def process_task(queue):
    """
        Function removes task from 
        returns:
            str: task processed status
    """

    if queue:
        task = queue.pop(0) # removes the first element in queue
        print(f'Task: {task} processed and removed')
    else:
        print('No task')

def show_task(queue):

    """
    Function shows all task 
    Returns:
        str: returns all task
    """
    if not queue:
        print('no pending task')
    else:
        print('\npending task')
        for i, task in enumerate(queue, start=1):
            print(f'{i}. {task}')

#  main function
if __name__ == '__main__':

    queue=[]

    while True:
        print()
        print("====Task Manager====")
        print('1. Add task\n2. Process Task\n3. show task\n4. Exit')

        # user choice
        choice = int(input('Enter choice: '))
        if choice == 1:
            add_task(queue)
        elif choice == 2:
            process_task(queue)
        elif choice == 3:
            show_task(queue)
        elif choice == 4:
            print("Exiting Byeee")
            break
        else:
            print('Invalid input')
        