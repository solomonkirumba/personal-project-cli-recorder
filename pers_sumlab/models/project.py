from models.task import Task

class Project:
    def __init__(self, project_id: str, title: str, user_id: str, tasks=None):
        self.id = project_id
        self.title = title
        self.user_id = user_id
        self.tasks = tasks or []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "user_id": self.user_id,
            "tasks": [t.to_dict() for t in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        p = cls(data["id"], data["title"], data["user_id"])
        p.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return p