from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    
    if len(title.strip()) < 3:
        raise ValueError("Task title must be at least 3 characters long.")
    
    return True
    
def validate_task_description(description):
    if not isinstance(description, str) or len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    
    if len(description.strip()) < 5:
        raise ValueError("Task description must be at least 5 characters long.")
    
    return True
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")

    return True