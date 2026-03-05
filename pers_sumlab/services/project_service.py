import uuid
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_handler import load_data, save_data
from utils.validators import validate_non_empty

class ProjectService:
    def __init__(self):
        self.data = load_data()
        self.users = [User.from_dict(u) for u in self.data.get("users", [])]
        self.projects = [Project.from_dict(p) for p in self.data.get("projects", [])]
    
    def _save(self):
        self.data["users"] = [u.to_dict() for u in self.users]
        self.data["projects"] = [p.to_dict() for p in self.projects]
        save_data(self.data)
    
    # ---------- USERS ----------
    def add_user(self, name):
        try:
            name = validate_non_empty(name, "Name")
            user_id = str(uuid.uuid4())[:8]
            self.users.append(User(user_id, name))
            self._save()
            print(f"User added: {name} (ID: {user_id})")
        except ValueError as e:
            print(f"Error: {e}")
    
    def list_users(self):
        if not self.users:
            print("No users found.")
            return
        print("\nUsers:")
        for u in self.users:
            print(f"  {u.id}: {u.name}")
    
    # ---------- PROJECTS ----------
    def add_project(self, title, user_name):
        try:
            title = validate_non_empty(title, "Title")
            user_name = validate_non_empty(user_name, "User name")
            
            user = next((u for u in self.users if u.name.lower() == user_name.lower()), None)
            if not user:
                print(f"User '{user_name}' not found")
                return
            
            project_id = str(uuid.uuid4())[:8]
            self.projects.append(Project(project_id, title, user.id))
            self._save()
            print(f"Project added: {title} for {user.name}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def list_projects(self, user_name=None):
        if user_name:
            user = next((u for u in self.users if u.name.lower() == user_name.lower()), None)
            if not user:
                print(f"User '{user_name}' not found")
                return
            projects = [p for p in self.projects if p.user_id == user.id]
            print(f"\nProjects for {user.name}:")
        else:
            projects = self.projects
            print("\nAll Projects:")
        
        if not projects:
            print("  No projects found.")
            return
        
        for p in projects:
            user = next((u for u in self.users if u.id == p.user_id), None)
            username = user.name if user else "Unknown"
            task_count = len(p.tasks)
            done_count = sum(1 for t in p.tasks if t.completed)
            print(f"  {p.id}: {p.title} (User: {username}) - Tasks: {done_count}/{task_count} complete")
    
    # ---------- TASKS ----------
    def add_task(self, project_title, task_title, description=""):
        try:
            project_title = validate_non_empty(project_title, "Project title")
            task_title = validate_non_empty(task_title, "Task title")
            
            project = next((p for p in self.projects if p.title.lower() == project_title.lower()), None)
            if not project:
                print(f"Project '{project_title}' not found")
                return
            
            task_id = str(uuid.uuid4())[:8]
            task = Task(task_id, task_title, description)
            project.add_task(task)
            self._save()
            print(f"Task added to '{project.title}': {task_title}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def complete_task(self, project_title, task_title):
        try:
            project_title = validate_non_empty(project_title, "Project title")
            task_title = validate_non_empty(task_title, "Task title")
            
            project = next((p for p in self.projects if p.title.lower() == project_title.lower()), None)
            if not project:
                print(f"Project '{project_title}' not found")
                return
            
            task = next((t for t in project.tasks if t.title.lower() == task_title.lower()), None)
            if not task:
                print(f"Task '{task_title}' not found in project")
                return
            
            task.mark_complete()
            self._save()
            print(f"Task marked complete: {task_title}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def list_tasks(self, project_title):
        try:
            project_title = validate_non_empty(project_title, "Project title")
            project = next((p for p in self.projects if p.title.lower() == project_title.lower()), None)
            if not project:
                print(f"Project '{project_title}' not found")
                return
            
            print(f"\nTasks in '{project.title}':")
            if not project.tasks:
                print("  No tasks.")
                return
            
            for t in project.tasks:
                status = "Done" if t.completed else "Pending"
                print(f"  [{status}] {t.title}: {t.description or 'No description'}")
        except ValueError as e:
            print(f"Error: {e}")