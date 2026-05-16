from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from typing import List
from SQLite_Taskmanager import TaskTracker

app=FastAPI()
tracker=TaskTracker()
class TaskCreate(BaseModel):
    title:str=Field(...,min_length=1,max_length=100)
    description:str=''
    priority:str
    due_date:str=Field(...,pattern=r'^\d{4}-\d{2}-\d{2}$')

@app.get('/tasks',response_model=List[dict])
def get_task(sort_by:str=None):
    "Retrieving all the tasks"
    if sort_by in ['priority','due_date']:
        tasks=tracker.get_all_tasks(sort_by)
    else:
        tasks=tracker.get_all_tasks()
    return tasks

@app.post("/tasks",status_code=201)
def create_task(task_data : TaskCreate):
    try:
        new_id=tracker.add_task(
            title=task_data.title,
            description=task_data.description,
            priority_str=task_data.priority,
            due_date=task_data.due_date
        )

        return {"message": "Task created", "id":new_id}
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.put('/tasks/{task_id}/done')
def mark_task_done(task_id:int):
    if tracker.mark_done(task_id):
       return {"message": f"Task {task_id} marked done"}
    raise HTTPException(status_code=404,detail="Task Not Found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if tracker.remove_task(task_id):
        return {f"'message':Task id {task_id} is removed successfully"}
    raise HTTPException(status_code=404, detail="Task Not Found")
