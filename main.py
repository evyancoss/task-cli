from models import task
import argparse

def add(description: str):
    print("Add task: {}".format(task))
    uid = task.add(description)
    print("Task added successfully (ID: {})".format(uid))

def update(uid: int):
    print("Update task: {}".format(uid))

def delete(uid: int):
    print("Task: {} was deleted".format(uid))

def mark_in_progress(uid: int):
    print('')

def mark_done(uid: int):
    print('')

def list(status=None):
    print("List tasks")
    return task.list(status)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    # Subparsers for different commands
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", type=str, help="Filter by status (optional)")

    # Update task command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("uid", type=int, help="Task ID")

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("uid", type=int, help="Task ID")

    # Parse command-line arguments
    args = parser.parse_args()

    if args.command == 'list':
        tasks = list()
        print(tasks)
    elif args.command == 'add':
        add(args.description)