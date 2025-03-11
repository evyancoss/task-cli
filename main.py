from models import task
import argparse

def add(description: str):
    print("Add task: {}".format(task))
    uid = task.add(description)
    print("Task added successfully (ID: {})".format(uid))

def update(uid: int, description: str):
    uid = task.update(uid,description)
    print("Update task: {}".format(uid))

def delete(uid: int):
    print("Task: {}".format(uid))
    return task.delete(uid)

def status(uid: int, status: str):
    return task.change_status(uid,status)
    

def list_tasks(status=None):
    print("List tasks")
    return task.list(status)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    # Subparsers for different commands
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("--description", type=str, help="Task description")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", type=str, help="Filter by status done / todo / in-progress (optional)")

    # Update task command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("uid", type=int, help="Task ID")
    update_parser.add_argument("--description", type=str, help="New description", default=None)

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("uid", type=int, help="Task ID")

    mark_in_progress = subparsers.add_parser("mark-in-progress", help="Change task to mark_in_progress")
    mark_in_progress.add_argument("uid", type=int, help="Task ID")
    
    mark_done = subparsers.add_parser("mark-done", help="Change task to mark-done")
    mark_done.add_argument("uid", type=int, help="Task ID")

    # Parse command-line arguments
    args = parser.parse_args()
    
    if args.command == "list":
        tasks = list_tasks(args.status)
        print(tasks)

    elif args.command == "add":
        add(args.description)

    elif args.command == "update":
        update(args.uid,args.description)

    elif args.command == "delete":
        delete(args.uid)

    elif args.command == "mark-in-progress":
        status(args.uid,"mark-in-progress")

    elif args.command == "mark-done":
        status(args.uid,"mark-done")
