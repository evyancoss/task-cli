from datetime import datetime
import json, os, random

def file_tasks():
    if not os.path.exists('src/tasks.json'):
        with open('src/tasks.json', 'w') as file:
            json.dump([], file)

    with open('src/tasks.json', 'r') as file:
        return json.load(file)
    

def list(status = None):
        tasks = file_tasks()
        tasks = [task for task in tasks] 
        return tasks

def add(description: str):
        tasks = file_tasks()
        uid = random.randint(1, 1000)

        new_task= {
            'uid': uid,
            'description':description,
            'status':'todo',
            'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt':''
        }
        
        tasks.append(new_task)

        with open('src/tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)

        return new_task['uid']
    
    
list()