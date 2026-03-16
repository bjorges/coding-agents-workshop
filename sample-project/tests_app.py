"""Tests for TaskAPI."""

import pytest
from app import app
from database import db


@pytest.fixture
def client():
    """Create a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_create_task(client):
    """Test creating a new task."""
    response = client.post(
        "/tasks",
        json={
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "due_date": "2024-12-25",
        },
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Buy groceries"
    assert data["status"] == "pending"


def test_get_tasks(client):
    """Test retrieving all tasks."""
    # Create a task first
    client.post(
        "/tasks",
        json={"title": "Test task", "description": "A test"},
    )

    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0


# TODO: Add more tests
# - test_get_single_task
# - test_update_task
# - test_delete_task
# - test_invalid_input
# - test_missing_fields
# - test_task_not_found
