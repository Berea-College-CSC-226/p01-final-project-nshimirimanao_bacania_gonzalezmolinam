# import re
#
# class valid_input:
#     tasks = "assignments"
#
#     def __init__(self, task_name="", date="", time=""):
#         self.task_name = task_name
#         self.date = date
#         self.time = time
#
#     def format_taskname(self):
#         task_name = input(int("What assignment would you like to submit?:"))
#         if task_name.strip() == "":
#             print("Task name cannot be empty I fear")
#         elif not re.match(r"^[A-Za-z0-9 ]+$", task_name):
#             print("Invalid task name, only letters & numbers please")
#         else:
#             self.task_name = task_name
#             return task_name


import re

class InputValidator:

    @staticmethod
    def validate_task_name(task_name):
        if task_name.strip() == "":
            return False, "Task name cannot be empty."

        if not re.match(r"^[A-Za-z0-9 ]+$", task_name):
            return False, "Only letters and numbers allowed."

        return True, task_name


    @staticmethod
    def validate_date(date):
        # format: MM/DD/YYYY
        if not re.match(r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}$", date):
            return False, "Date must be in MM/DD/YYYY format."

        return True, date


    @staticmethod
    def validate_time(time):
        # format: HH:MM (24-hour)
        if not re.match(r"^([01]\d|2[0-3]):([0-5]\d)$", time):
            return False, "Time must be in HH:MM (24-hour) format."

        return True, time