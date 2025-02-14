from models import task
import sys, argparse

def add(description: str):
    print("Add task: {}".format(task))
    task.add(description)
    print("Task added successfully (ID: 1)")

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
    print("Hello, world")
    user_input = sys.argv[1]
    if user_input == '-list':
        tasks = list()
        print(tasks)
    elif user_input == '-add':
        add(' '.join(sys.argv[2:]))