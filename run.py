
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




def main():
    display_menu()
    # single source of truth: data
    tasks = ["I wanna eat", "I wanna code", "Get some eggs later"]
    choice = input("Enter your choice: ")

    if choice == '1':
        view_tasks(tasks)



main()