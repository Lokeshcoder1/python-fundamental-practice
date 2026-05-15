from fastapi.testclient import TestClient
from api import app

client=TestClient(app)

def test_create_and_get_tasks():
    response=client.post("/tasks",json={
        'title':'test',
        'description':'test_desc',
        'priority':'high',
        'due_date':'2026-05-18'
    })
    assert response.status_code==201
    task_id=response.json()['id']

    response=client.get("/tasks")
    assert response.status_code==200
    tasks=response.json()
    assert any(t['id']==task_id for t in tasks)

def test_mark_done():
    put=client.post("/tasks",json={'title':'done','description':'done desc','priority':'low','due_date':'2026-05-18'})
    task_id=put.json()['id']
    put=client.put(f"/tasks/{task_id}/done")
    assert put.status_code==200
    get=client.get("/tasks")
    task=next(t for t in get.json() if t['id']==task_id)
    assert task['done'] is True

def test_del_task():
    delete=client.post("/tasks",json={'title':'delete','description':'delete desc','priority':'low','due_date':'2026-05-19'})
    task_id=delete.json()['id']
    delete=client.put(f"/tasks/{task_id}")
    assert delete.status_code==200
    get = client.get("/tasks")
    assert not any(t['id']==task_id for t in get.json())