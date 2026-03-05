# Project Manager CLI

A command-line application for managing users, projects, and tasks. This personal summary lab project provides a simple yet effective way to organize your work by creating users, assigning projects to them, and tracking tasks within those projects.

## Features

- **User Management**: Create and list users to organize project ownership
- **Project Management**: Create projects, associate them with users, and view all projects or filter by user
- **Task Management**: Add tasks to projects with descriptions, list tasks, and mark them as complete
- **Data Persistence**: All data is saved to a JSON file for persistent storage
- **Input Validation**: Built-in validation to ensure data integrity
- **User-Friendly CLI**: Interactive menu-driven interface for easy navigation

## Project Structure

```
pers_sumlab/
├── main.py                    # Application entry point with CLI menu
├── models/
│   ├── user.py                # User model class
│   ├── project.py             # Project model class
│   └── task.py                # Task model class
├── services/
│   └── project_service.py      # Business logic for user, project, and task operations
├── utils/
│   ├── file_handler.py         # File I/O and JSON data handling
│   └── validators.py           # Input validation utilities
├── data/
│   └── data.json               # Persistent data storage
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd pers_sumlab
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **Add User** - Create a new user
2. **List Users** - Display all registered users
3. **Add Project** - Create a new project and assign it to a user
4. **List All Projects** - View all projects with task completion status
5. **List User Projects** - View projects belonging to a specific user
6. **Add Task** - Add a task to a project with optional description
7. **List Tasks** - Display all tasks in a project
8. **Complete Task** - Mark a task as completed
9. **Exit** - Quit the application

### Example Workflow

1. Add a user: `John Doe`
2. Add a project: `Website Redesign` for `John Doe`
3. Add tasks to the project: `Logo Design`, `Homepage Layout`, etc.
4. Complete tasks as you progress
5. View your project statistics to track completion

## Models

### User
- `id`: Unique identifier (auto-generated UUID)
- `name`: User's name

### Project
- `id`: Unique identifier (auto-generated UUID)
- `title`: Project name
- `user_id`: Reference to the project owner
- `tasks`: List of Task objects

### Task
- `id`: Unique identifier (auto-generated UUID)
- `title`: Task name
- `description`: Optional task description
- `completed`: Boolean status indicating completion

## Data Storage

All data is stored in `data/data.json` in the following structure:
```json
{
  "users": [...],
  "projects": [...]
}
```

Data is automatically saved after any add, update, or completion operation.
