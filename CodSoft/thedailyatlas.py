import json
import os


class task_atlas:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\n***** The Daily Atlas *****")
        for i, task in enumerate(self.tasks, 1):
            status = "☑️" if task["completed"] else "⬜"
            print(f"{i}. {status} {task['task']}")
        print("-----------------------------------\n")

    def mark_task_complete(self, task_no):
        if 1 <= task_no <= len(self.tasks):
            self.tasks[task_no - 1]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid Task number")

    def delete_task(self, task_no):
        if 1 <= task_no <= len(self.tasks):
            del self.tasks[task_no - 1]
            self.save_tasks()
        else:
            print("Invalid Task number")

    def edit_task(self, task_no, new_task):
        if 1 <= task_no <= len(self.tasks):
            self.tasks[task_no - 1]["task"] = new_task
            self.save_tasks()
        else:
            print("Invalid Task number")


def main():
    atlas = task_atlas()

    while True:
        print("\n***** The Daily Atlas *****")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")
        print("-----------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            if task:
                atlas.add_task(task)
            else:
                print("Task description cannot be empty.")
        elif choice == "2":
            atlas.list_tasks()
        elif choice == "3":
            try:
                task_no = int(input("Enter Task number to be mark as completed: ").strip())
                atlas.mark_task_complete(task_no)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                task_no = int(input("Enter Task number to be deleted: ").strip())
                atlas.delete_task(task_no)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            try:
                task_no = int(input("Enter Task number to be edited: ").strip())
                new_task = input("Enter new task description: ").strip()
                if new_task:
                    atlas.edit_task(task_no, new_task)
                else:
                    print("Task description cannot be empty.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
