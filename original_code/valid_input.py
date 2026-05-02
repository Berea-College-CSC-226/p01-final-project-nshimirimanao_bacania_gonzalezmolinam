import re

class valid_input:
    tasks = "assignments"

    def __init__(self, task_name="", date="", time=""):
        self.task_name = task_name
        self.date = date
        self.time = time

    def format_taskname(self):
        task_name = input(int("What assignment would you like to submit?:"))
        if task_name.strip() == "":
            print("Task name cannot be empty I fear")
        elif not re.match(r"^[A-Za-z0-9 ]+$", task_name):
            print("Invalid task name, only letters & numbers please")
        else:
            self.task_name = task_name
            return task_name

        return task_name

