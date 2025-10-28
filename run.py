
def display_menu():
    print("\n Todo list menu")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")
    print("---------------")



def view_tasks(task_lists):
    if not task_lists:
        print("your todo is empty")
    else:
        for i, task in enumerate(task_lists, 1):
            print(f"{i}. {task}")


def add_task(task_lists):
    task = input("Enter the task you want to add: ")
    if task:
        task_lists.append(task)
        print("successfully added task!")
    else:
        print("No task entered. Please try again.")




def main():
   
    # single source of truth: data
    tasks = []
    while True:

        display_menu()
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        else:
            print("Invalid choice, Please enter a number between 1-4")



main()


#1. Store data somewhere
#2. Request data from the user
#3. check what data is entered, depending on the data, do something
#4. What happens when the user enrers 2, call a function to add the taks to the existing tasks in the list

