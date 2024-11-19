import sys

# Data storage
candidates = []
projects = []

# Candidate Functions
def create_candidate():
    print("\n--- Create Candidate ---")
    name = input("Name: ")
    position = input("Position: ")
    level = input("Level: ")
    expected_salary = float(input("Expected Salary: "))
    candidate = {
        "name": name,
        "position": position,
        "level": level,
        "expected_salary": expected_salary
    }
    candidates.append(candidate)
    print(f"Candidate {name} added successfully!\n")

def view_candidates():
    print("\n--- View Candidates ---")
    if not candidates:
        print("No candidates available.\n")
        return
    
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}. {candidate['name']} - {candidate['position']} - {candidate['level']} - ${candidate['expected_salary']}")
    print()

def update_candidate():
    view_candidates()
    if not candidates:
        return
    try:
        choice = int(input("Enter candidate number to update: "))
        if 1 <= choice <= len(candidates):
            candidate = candidates[choice - 1]
            print(f"Updating {candidate['name']}...")
            candidate['name'] = input(f"New Name [{candidate['name']}]: ") or candidate['name']
            candidate['position'] = input(f"New Position [{candidate['position']}]: ") or candidate['position']
            candidate['level'] = input(f"New Level [{candidate['level']}]: ") or candidate['level']
            candidate['expected_salary'] = float(input(f"New Expected Salary [{candidate['expected_salary']}]: ") or candidate['expected_salary'])
            print("Candidate updated successfully!\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

def delete_candidate():
    view_candidates()
    if not candidates:
        return
    try:
        choice = int(input("Enter candidate number to delete: "))
        if 1 <= choice <= len(candidates):
            candidate = candidates[choice - 1]
            print(f"Deleting {candidate['name']}...")
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == 'yes':
                candidates.pop(choice - 1)
                print("Candidate deleted successfully!\n")
            else:
                print("Deletion canceled.\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

# Project Functions
def add_project():
    print("\n--- Add Project ---")
    project_name = input("Project Name: ")
    position = input("Required Position: ")
    level = input("Required Level: ")
    budget = float(input("Project Budget: "))
    project = {
        "name": project_name,
        "position": position,
        "level": level,
        "budget": budget
    }
    projects.append(project)
    print(f"Project {project_name} added successfully!\n")

def view_projects():
    print("\n--- View Projects ---")
    if not projects:
        print("No projects available.\n")
        return
    
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project['name']} - {project['position']} - {project['level']} - ${project['budget']}")
    print()

def update_project():
    view_projects()
    if not projects:
        return
    try:
        choice = int(input("Enter project number to update: "))
        if 1 <= choice <= len(projects):
            project = projects[choice - 1]
            print(f"Updating {project['name']}...")
            project['name'] = input(f"New Project Name [{project['name']}]: ") or project['name']
            project['position'] = input(f"New Required Position [{project['position']}]: ") or project['position']
            project['level'] = input(f"New Required Level [{project['level']}]: ") or project['level']
            project['budget'] = float(input(f"New Project Budget [{project['budget']}]: ") or project['budget'])
            print("Project updated successfully!\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

def delete_project():
    view_projects()
    if not projects:
        return
    try:
        choice = int(input("Enter project number to delete: "))
        if 1 <= choice <= len(projects):
            project = projects[choice - 1]
            print(f"Deleting {project['name']}...")
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == 'yes':
                projects.pop(choice - 1)
                print("Project deleted successfully!\n")
            else:
                print("Deletion canceled.\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

# Main Menu
def main_menu():
    while True:
        print("\n--- Recruitment Manager ---")
        print("1. Manage Candidates")
        print("2. Manage Projects")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            manage_candidates()
        elif choice == "2":
            manage_projects()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

# Sub-menus
def manage_candidates():
    while True:
        print("\n--- Manage Candidates ---")
        print("1. Create Candidate")
        print("2. View Candidates")
        print("3. Update Candidate")
        print("4. Delete Candidate")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            create_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            update_candidate()
        elif choice == "4":
            delete_candidate()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

def manage_projects():
    while True:
        print("\n--- Manage Projects ---")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            update_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
