"""Configuration for TaskAPI."""

import os

# Server configuration
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000

# Database configuration
# TODO: Move these to environment variables
DATABASE_TIMEOUT = 30
DATABASE_RETRY_ATTEMPTS = 3

# API configuration
API_VERSION = "v1"
MAX_TASKS_PER_REQUEST = 100

# TODO: Add logging configuration
# TODO: Add CORS configuration
