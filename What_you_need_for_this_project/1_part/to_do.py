import os

Todo_file = "todo.txt"

def load_tasks():
    if not os.path.exists(Todo_file):
        return[]
    with open(Todo_file, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(Todo_file, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("\n No tasks The lsit is empty")
        return
    print('\n To-Do List:')
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    
    while True:
        print("menu: ")
        print("1. View Tasks")
        print("2. Add Task ")
        print("3. Task Done")
        print("4. Exit Program")
           
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            show_tasks(tasks)
            
        elif choice == '2':
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!\n")
        elif choice == '3':
            show_tasks(tasks)
            index = input("Enter task number to mark as done: ").strip()
            if index.isdigit():
                index = int(index)
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' marked as done and removed.\n")
                else:
                    print("Invalid task number.\n")
            else:
                print("Please enter a valid number.\n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
            