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