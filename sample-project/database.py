"""Simple in-memory database for tasks."""

from typing import Optional
from models import Task


class Database:
    """In-memory task database."""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create_task(
        self, title: str, description: str = "", due_date: Optional[str] = None
    ) -> Task:
        """Create and store a new task."""
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            due_date=due_date,
        )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by ID."""
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> list:
        """Retrieve all tasks."""
        return list(self.tasks.values())

    def update_task(self, task_id: int, **kwargs) -> Optional[Task]:
        """Update a task."""
        task = self.tasks.get(task_id)
        if task:
            task.update(**kwargs)
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False


# Global database instance
db = Database()
