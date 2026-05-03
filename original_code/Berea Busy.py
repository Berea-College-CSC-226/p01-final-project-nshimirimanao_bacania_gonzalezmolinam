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
import tkinter as tk
import re
import time # added on 05.01.26

class Create_GUI:

    def __init__(self):
        self.window = None
        self.buttons = {}
        self.input = {}

        self.tracker = TrackTasks()
        self.validate = valid_input()


    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Berea Busy")
        self.window.geometry("800x800")

        self.input["Name"] = tk.Entry(self.window)
        self.input["Name"].pack()

        self.input["Due date"] = tk.Entry(self.window)
        self.input["Due date"].pack()

        self.output_label = tk.Label(self.window, text="")
        self.output_label.pack()

        self.create_button()
        self.window.mainloop()

    def add_task(self):
        name = self.input["Name"].get()
        due = self.input["Due date"].get()
       # done = self.input["Turned in"].get()

        if not self.validate.check_none([name,due]):
            self.display_output("There seems to be something missing, make sure you fill in everything.")
            return

        if not self.validate.validate_userinput(due):
            self.display_output("Wrong format")
            return

        task = Task(name, due, done)

        self.tracker.add_task(task)

        self.display_output("Another task for the busy bee!")

    def display_output(self,message):

        self.output_label.config(text=message)

    def create_button(self):

        self.buttons["add"] = tk.Button (self.window, text = "Add New Task", command=self.add_task)
        self.buttons["add"].pack()


class Task:

    """
    This function is going to represent an assignment and store its details
    such as the name, the due date and when it was submitted)
    """

    def __init__(self, name, duedate, done):    #This is the task object
        self.name = name
        self.duedate = duedate
        self.done = done
        self.time = None
        self.points = 0

        self.find_state()
        self.reward_system()

    def find_state(self):
        """
        This function is going to check if the assignment was early, on time or late
        """
        if self.done < self.duedate:
            self.state = "Early"
        elif self.done == self.duedate:
            self.state = "Yay! On time"
        else:
            self.state = "Late"

    def reward_system(self):

        """
        This function is going to give in  points based on the submission status
        so early is 10 points, on time is 5 and if teh student submitted it late so that is -5 points
        """
        if self.time == "Early":
            self.points=10
        elif self.time == "Yay! On time":
            self.points=5

        else:
            self.points=-5


    def user_info(self):
        return (
            f"Assignment: {self.name}\n"
            f"Due Date: {self.duedate}\n"
            f"Submitted: {self.turnedin}\n"
            f"Status: {self.time}\n"
        )

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


class TrackTasks:
    def __init__(self):
        self.assignments =[]

    def add_task(self, task):
        self.assignments.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.assignments):
            self.assignments[index] = new_task
        else:
            print("invalid task number. please try again")

    def display_tasks(self):
        for i, task in enumerate(self.assignments, start=1):
            print(f'{i}. {task}')

if __name__ == "__main__":

    BBApp = Create_GUI()
    BBApp.create_window()