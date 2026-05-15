from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from typing import List
from Taskmanager import TaskTracker

app=FastAPI()
tracker=TaskTracker()
tracker.load_from_file('tasks.json')
class TaskCreate(BaseModel):
    title:str=Field(...,min_length=1,max_length=100)
    description:str=''
    priority:str
    due_date:str=Field(...,pattern=r'^\d{4}-\d{2}-\d{2}$')

@app.get('/tasks',response_model=List[dict])
def get_task():
    "Retrieving all the tasks"
    return [task.to_dict()for task in tracker.tasks]

@app.post("/tasks",status_code=201)
def create_task(task_data : TaskCreate):
    try:
        task=tracker.add_task(
            id=tracker._next_id,
            title=task_data.title,
            description=task_data.description,
            priority_str=task_data.priority,
            due_date=task_data.due_date
        )
        tracker.save_to_file()
        return {f"'message':Task Created task_id{tracker._next_id-1}"}
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.put('/tasks/{task_id}/done')
def mark_task_done(task_id:int):
    for task in tracker.tasks:
        if task.id==task_id:
            task.done=True
            tracker.save_to_file()
            return {f"'message':Task id {task_id} is marked done"}
    raise HTTPException(status_code=404,detail="Task Not Found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for i,task in enumerate(tracker.tasks):
        if task.id==task_id:
            tracker.tasks.pop(i)
            tracker.save_to_file()
            return {f"'message':Task id{task_id} is deleted successfully"}
    raise HTTPException(status_code=404,detail="Task Not Found")
