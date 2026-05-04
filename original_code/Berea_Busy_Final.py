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

from datetime import datetime, timedelta

class Task:

    """
    This function is going to represent an assignment and store its details
    such as the name, the due date and when it was submitted)
    """

    def __init__(self, name, duedate_str,done_str):    #This is the task object
        self.name=name
        self.duedate=duedate
        self.done=done
        self.time = None


        self.name
        self.duedate = datetime.strptime(duedate_str,  "%m-%d-%Y %H:%M")
        self.done = datetime.strptime(done_str,  "%m-%d-%Y %H:%M")

        self.status = None
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
            f"Due Date: {self.duedate.strftime("%m-%d-%Y %H:%M")}\n"
            f"Submitted: {self.done.strftime("%m-%d-%Y %H:%M")}\n"
            f"Status: {self.status}\n"
            f"Points Earned: {self.points}\n"
        )


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