from datetime import datetime

def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))

            for i in range(n_tasks):
                task_description = input("Enter the task description: ")
                due_date_input = input("Enter the due date (YYYY-MM-DD): ")
                
                # Validate the due date format
                try:
                    due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue
                
                tasks.append({"task": task_description, "due_date": due_date, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                due_date_str = task["due_date"].strftime("%Y-%m-%d")
                print(f"{index + 1}. {task['task']} (Due: {due_date_str}) - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(tasks):
                print("Updating task...")
                new_task_description = input("Enter the new task description: ")
                new_due_date_input = input("Enter the new due date (YYYY-MM-DD): ")
                
                # Validate the new due date format
                try:
                    new_due_date = datetime.strptime(new_due_date_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue
                
                tasks[task_index]["task"] = new_task_description
                tasks[task_index]["due_date"] = new_due_date
                print("Task updated!")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()