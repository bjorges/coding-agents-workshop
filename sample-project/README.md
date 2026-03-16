# TaskAPI — Simple Task Management REST API

A minimal REST API for managing tasks, built with Flask. Use this project to practice AI-assisted coding with Copilot, Claude, or other AI tools.

## Features

- Create, read, update, and delete tasks
- Tasks have title, description, status, due date
- In-memory storage (no database setup required)
- Simple JSON API

## Tech Stack

- **Framework**: Flask
- **Language**: Python 3.8+
- **Testing**: pytest
- **Container**: Docker

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py

# The API will be available at http://localhost:5000
```

### Run Tests

```bash
pytest tests_app.py -v
```

### Using Docker

```bash
docker build -t taskapi .
docker run -p 5000:5000 taskapi
```

## API Endpoints

- `GET /tasks` — List all tasks
- `POST /tasks` — Create a new task
- `GET /tasks/<id>` — Get a specific task
- `PUT /tasks/<id>` — Update a task
- `DELETE /tasks/<id>` — Delete a task

## Example Request

```bash
# Create a task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "description": "2% milk", "due_date": "2024-12-25"}'

# Get all tasks
curl http://localhost:5000/tasks
```

## Workshop Notes

This project is **intentionally imperfect** — it has several areas where you can practice with AI:

- ❌ Missing input validation
- ❌ No error handling for edge cases
- ❌ Hardcoded configuration values
- ❌ Incomplete test coverage
- ❌ No logging

Try asking your AI assistant to:
- Add input validation to the POST endpoint
- Add more test cases
- Move hardcoded values to environment variables
- Add error handling for missing tasks
- Add logging to track API calls

## License

MIT
