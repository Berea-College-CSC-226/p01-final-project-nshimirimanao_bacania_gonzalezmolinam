import tkinter as tk
import re
import time #using this for clock as a timer

class Create_GUi:


   def __init__(self):
       self.window = None
       self.buttons = {}
       self.input = {}


       # self.tracker = Track_tasks()
       # self.validate = Valid_input()


   def create_window(self):
       self.window = tk.Tk()
       self.window.title("Berea Busy")
       self.window.geometry("800x800")


       '''
       This is going to make the frame be in the center
       '''


       center_frame = tk.Frame(self.window)
       center_frame.pack(expand=True)

       self.output_label = tk.Label(center_frame, text="Name")
       self.output_label.pack()

       self.input["Name"] = tk.Entry(center_frame, text="Name")
       self.input["Name"].pack()

       self.output_label = tk.Label(center_frame, text="Due date")
       self.output_label.pack()

       self.input["Due date"] = tk.Entry(center_frame)
       self.input["Due date"].pack()

       self.window.mainloop()

class Task:

    def __init__(self, name, duedate, done):
        self.name = name
        self.duedate = duedate
        self.done = done
        self.time = None      ####CREATE CLOCK
        # self.points = 0
        # self.state = 0

# timer to be implemented and displayed
#
#     def timer(self):
#         from datetime import datetime, timedelta
#         # Setting a due date
#         due_date = datetime(2026, 5, 1, 23, 27)  # May 10, 2026, at 5:00 PM
#         now = datetime.now()
#
#         # Checking if overdue
#         if now > due_date:
#             print("Assignment is overdue!")
#         else:
#             time_left = due_date - now
#             print(f"Time remaining: {time_left}")



    def find_state(self):
        if self.done < self.duedate:
            self.state = "Early!"
        elif self.done == self.duedate:
            self.state = "You did your work on time!"
        else:
            self.state = "Late... Better luck next time!"

    def reward_system(self):
        if self.state == "Early":
            self.points += 10
        elif self.state == "You did your work on time!":
            self.points += 5
        else:
            self.points -= 5

## user info is placed into here

class valid_input(Task):
    #
    # def __init__(self, task):
    #     self.task_name = task
    def format_taskname(self):
        task_name = input(int("What assignment would you like to submit?:"))
        if task_name.strip() == "":
            print("Task name cannot be empty I fear")
        elif not re.match(r"^[A-Za-z0-9]+$", task_name):
            print("Invalid task name, only letters ad numbers please.")
        else:
            self.task_name = task_name
            return task_name

class TrackTasks(Task, Create_GUi):
    def __init__(self):
        self.assignments = []

    def add_task(self, task):
        self.assignments.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.assignments):
            self.assignments[index] = new_task
        else:
            print("Already added. Please try again.")

    def display_tasks(self):
        for i, task in enumerate(self.assignments, start=1):
            print(f"{i}.{task}")

if __name__ == "__main__":

    BBApp = Create_GUi()
    BBApp.create_window()