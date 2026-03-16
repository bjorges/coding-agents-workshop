from datetime import datetime
from typing import Optional


class Task:
    """Represents a single task."""

    def __init__(
        self,
        id: int,
        title: str,
        description: str = "",
        status: str = "pending",
        due_date: Optional[str] = None,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status  # pending, in_progress, completed
        self.created_at = datetime.now().isoformat()
        self.due_date = due_date

    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "due_date": self.due_date,
        }

    def update(self, **kwargs):
        """Update task fields."""
        allowed_fields = {"title", "description", "status", "due_date"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
