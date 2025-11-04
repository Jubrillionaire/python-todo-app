
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


def remove_task(task_lists):
    view_tasks(task_lists)
    if not task_lists:
        return 

    try:
        task_num_str = input("Enter the task number you want to remove: ")
        task_num = int(task_num_str)

        #check whether the user enters the value between 1 and the lengh of the list
        if 1 <= task_num <= len(task_lists):

            removed_task = task_lists.pop(task_num - 1)
            print(f"Successfully removed task: {removed_task}")
        else:
            print("Error: Task number out of range. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")






def main():
   
    # single source of truth: data
    tasks = ["i wanna eat", "i wanna sleep", "i wanna code"]
    while True:

        display_menu()
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            print("Invalid choice, Please enter a number between 1-4")



main()


#1. Store data somewhere
#2. Request data from the user
#3. check what data is entered, depending on the data, do something
#4. What happens when the user enrers 2, call a function to add the taks to the existing tasks in the list




# users enters an index  1, 2 , 3

# check whether the user enters the value between 1 and the lengh of the list
  # if uservalue >= 1  && uservalue < length of the todolist
  #  remove the todo 
      # we need the task lisk
      # we also need the user value
      # we look within the list and delete the todo that matches with the user value - 1 
  # else throw an error messag  that says todo can only be within the range of the exisiting list



