# Import functions from task_manager.task_utils package
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
    # tasks
)

from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nAdd a New Task")
            try:
                title = input("Enter task title: ")

                description = input("Enter task description: ")

                due_date = input("Enter due date (YYYY-MM-DD): ")

                # Validate inputs
                if not validate_task_title(title):
                    print("Invalid task title.")
                    continue
                if not validate_task_description(description):
                    print("Invalid task description.")
                    continue
                if not validate_due_date(due_date):
                    print("Invalid due date.")
                    continue

                add_task(title, description, due_date)
            except ValueError as e:
                print(f"An error occurred: {e}")

        elif choice == "2":
            print("\n--- All Tasks ---")
            view_pending_tasks()
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                mark_task_as_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Current Progress: {progress:.1f}%")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()