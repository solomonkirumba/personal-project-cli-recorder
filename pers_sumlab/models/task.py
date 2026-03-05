class Task:
    def __init__(self, task_id: str, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["description"],
            data["completed"]
        )