# To-Do List Application
import os

FILE_NAME = "tasks.txt"
class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                for line in file:
                    self.tasks.append(line.strip())

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self):
        task = input("Enter Task: ")
        self.tasks.append("[ ] " + task)
        self.save_tasks()
        print("Task Added Successfully!")

    def view_tasks(self):
        if not self.tasks:
            print(" No Tasks Available!")
            return

        print("\n===== YOUR TASKS =====")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_complete(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_no = int(input("Enter Task Number to Mark Complete: "))

            if 1 <= task_no <= len(self.tasks):
                task = self.tasks[task_no - 1]

                if task.startswith("[✓]"):
                    print("Task Already Completed!")
                else:
                    self.tasks[task_no - 1] = task.replace("[ ]", "[✓]")
                    self.save_tasks()
                    print("Task Marked as Complete!")

            else:
                print("Invalid Task Number!")

        except ValueError:
            print("Please Enter a Valid Number!")

    def remove_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_no = int(input("Enter Task Number to Remove: "))

            if 1 <= task_no <= len(self.tasks):
                removed = self.tasks.pop(task_no - 1)
                self.save_tasks()

                print(f" Removed: {removed}")

            else:
                print("Invalid Task Number!")

        except ValueError:
            print(" Please Enter a Valid Number!")


def main():
    todo = TodoList()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            todo.add_task()

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.mark_complete()

        elif choice == "4":
            todo.remove_task()

        elif choice == "5":
            print(" Thank You for Using To-Do List!")
            break

        else:
            print(" Invalid Choice!")


if __name__ == "__main__":
    main()