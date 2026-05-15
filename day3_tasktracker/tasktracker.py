import json
from datetime import datetime
from dataclasses import dataclass,asdict
from pathlib import Path
from enum import Enum

class Priority(Enum):
    HIGH='high'
    MEDIUM='medium'
    LOW='low'
@dataclass
class Task:
    title:str
    description:str
    priority:Priority
    due_date:str
    done:bool =False
    created_at:str=None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at=datetime.now().isoformat()

class TaskTracker:
    def __init__(self):
        self.tasks=[]

    def add_task(self, title, description, priority_str, due_date):
        try:
            priority = Priority(priority_str.lower())
        except ValueError:
            raise ValueError(f"Invalid priority: {priority_str}. Use high/medium/low.")
        task = Task(title, description, priority,due_date)
        self.tasks.append(task)
        return True

    def remove_task(self,idx):
        if idx-1 <= len(self.tasks):
            self.tasks.pop(idx-1)
            return True
        return False

    def mark_done(self,idx):
        self.tasks[idx-1].done=True
        return True

    def list_tasks(self,sort_by='priority'):

        if sort_by=='priority':
            self.sort_by_priority()
        elif sort_by=='due_date':
            self.sort_by_duedate()
        for i,task in enumerate(self.tasks):
            status = "✓" if task.done else "✗"
            print(f'{status}Task{i+1}\nTitle: {task.title} \nDescription: {task.description} \nPriority: {task.priority.value} \nCreated_at :{task.created_at} \nDueDate: {task.due_date}')
            print()
    def sort_by_priority(self):
        priority_order={Priority.HIGH:0,Priority.MEDIUM:1,Priority.LOW:2}
        self.tasks=sorted(self.tasks,key=lambda t: priority_order[t.priority])


    def sort_by_duedate(self):
        self.tasks=sorted(self.tasks,key=lambda t:t.due_date)



    def save_to_file(self,filename:str='tasks.json'):
        data=[]
        for task in self.tasks:
            task_dict=asdict(task)
            task_dict['priority']=task.priority.value
            data.append(task_dict)
        try:
            with open(filename,'w') as f:
                json.dump(data,f,indent=2)
                return
        except IOError:
            return []

    def load_from_file(self,filename:str='tasks.json'):

        if not Path(filename).exists():
            self.tasks= []

        try:
            with open(filename,'r') as f:
                data=json.load(f)
                self.tasks=[]
                for item in data:
                    priority_enum=Priority(item['priority'])
                    task=Task(
                        title=item['title'],
                        description=item['description'],
                        priority=priority_enum,
                        created_at=item['created_at'],
                        due_date=item['due_date']
                    )
                    self.tasks.append(task)
        except(json.JSONDecodeError,IOError):
            self.tasks=[]




