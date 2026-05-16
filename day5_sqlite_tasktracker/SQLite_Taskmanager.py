import sqlite3
from typing import List
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import os
from logger import set_logger

class Priority(Enum):
    HIGH='high'
    MEDIUM='medium'
    LOW='low'
@dataclass
class Task:
    id:int
    title:str
    description:str
    priority:Priority
    due_date:str
    done:bool =False
    created_at:str=None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at=datetime.now().isoformat()

    def to_dict(self):
        return{
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'priority':self.priority.value,
            'due_date':self.due_date,
            'done':self.done,
            'created_at':self.created_at
        }

class TaskTracker:
    def __init__(self):
        self.logger=set_logger("TaskTracker")
        db_path=os.getenv('DATABASE_PATH','Tasks.db')
        self.logger.info(f"Database is creating at {db_path}")
        self.conn=sqlite3.connect(db_path,check_same_thread=False)
        self.cursor=self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE  IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT NOT NULL,
        due_date TEXT NOT NULL,
        done BOOL DEFAULT 0,
        created_at TEXT)
        """)
        self.conn.commit()
    def add_task(self, title, description, priority_str, due_date):
        try:
            priority = Priority(priority_str.lower())
        except ValueError as e:
            self.logger.error(f"validation error {e}")
            raise ValueError(f"Invalid priority: {priority_str}. Use high/medium/low.")
        self.cursor.execute("""INSERT INTO tasks
        (title, description, priority, due_date, done, created_at) values(?,?,?,?,?,?) """,
                            (title,description,priority.value,due_date,0,datetime.now().isoformat()))
        self.conn.commit()

        new_id=self.cursor.lastrowid
        self.logger.info(f'Task added with id: {new_id}')
        return new_id

    def remove_task(self,task_id:int):
        try:
            self.cursor.execute("DELETE  FROM  tasks WHERE id = (?)",(task_id,))
            self.conn.commit()
            self.logger.info(f"Task removed with id {task_id}")
            return self.cursor.rowcount>0
        except sqlite3.Error as e:
            self.logger.error(f"validation error {e}")
            return False

    def mark_done(self,task_id:int):
        try:
            self.cursor.execute("UPDATE tasks SET done=1 WHERE id ==(?)",(task_id,))
            self.conn.commit()
            self.logger.info(f"Task marked done with id {task_id}")
            return self.cursor.rowcount >0
        except sqlite3.Error as e:
            self.logger.error(f"validation error {e}")
            return False


    def get_all_tasks(self,sort_by:str='priority') ->List[dict]:
        if sort_by=='priority':
            query="""
            SELECT * FROM tasks
            ORDER BY CASE priority
                WHEN 'high' THEN 0
                WHEN 'medium' THEN 1
                WHEN 'low' THEN 2
            END
            """
        elif sort_by=='due_date':
            query="SELECT * FROM  tasks ORDER BY due_date"
        else:
            query="SELECT * FROM tasks"
        self.cursor.execute(query)
        rows=self.cursor.fetchall()
        tasks=[]
        for row in rows:
            tasks.append({
                'id':row[0],
                'title':row[1],
                'description':row[2],
                'priority':row[3],
                'due_date':row[4],
                'done':bool(row[5]),
                'created_at':row[6]
            })
        return tasks





