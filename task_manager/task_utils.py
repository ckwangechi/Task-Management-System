from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return

    tasks[index]["completed"] = True
    print(f"Task '{tasks[index]['title']}' marked as complete.")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for i, task in enumerate(pending, 1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return 0

    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)

    progress = (completed / total) * 100

    print(f"\nProgress: {completed}/{total} tasks completed ({progress:.2f}%)")
    return progress