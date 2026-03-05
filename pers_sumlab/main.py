import sys
from services.project_service import ProjectService

def main():
    service = ProjectService()
    
    while True:
        print("\n" + "="*40)
        print("PROJECT MANAGER")
        print("="*40)
        print("1. Add user")
        print("2. List users")
        print("3. Add project")
        print("4. List all projects")
        print("5. List user projects")
        print("6. Add task")
        print("7. List tasks")
        print("8. Complete task")
        print("9. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            name = input("Name: ")
            service.add_user(name)
        
        elif choice == "2":
            service.list_users()
        
        elif choice == "3":
            title = input("Project title: ")
            user = input("User name: ")
            service.add_project(title, user)
        
        elif choice == "4":
            service.list_projects()
        
        elif choice == "5":
            user = input("User name: ")
            service.list_projects(user)
        
        elif choice == "6":
            project = input("Project title: ")
            task = input("Task title: ")
            desc = input("Description (optional): ")
            service.add_task(project, task, desc)
        
        elif choice == "7":
            project = input("Project title: ")
            service.list_tasks(project)
        
        elif choice == "8":
            project = input("Project title: ")
            task = input("Task title: ")
            service.complete_task(project, task)
        
        elif choice == "9":
            print("Later.")
            sys.exit()
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()