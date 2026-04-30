import tkinter as tk
import re

class Create_GUi:

    def __init__(self):
        self.window = None
        self.buttons = {}
        self.input = {}

        self.tracker = TrackTasks()
        self.validate = valid_input()
        self.assignment = Task(name,duedate,done)

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Berea Busy")
        self.window.geometry("800x800")

        self.input["Name"] = tk.Entry(self.window)
        self.input["Name"].pack()

        self.input["Due date"] = tk.Entry(self.window)
        self.input["Due date"].pack()

        self.input["Turned in"] = tk.Entry(self.window)
        self.input["Turned in"].pack()

        self.output_label = tk.Label(self.window, text="")
        self.output_label.pack()

        self.create_button()
        self.window.mainloop()

   # def get_input(self):
        #name = self.input["Name"].get()
        #due = self.input["Due date"].get()
        #turned_in = self.input["Turned in"].get()

        #if not self.validate.check_none([name,due,turned_in]):
            #self.display_output("There seems to be something missing, make sure you fill in everything.")
            #return

        #if not self.validate.validate_userinput(due, turned_in):
            #self.display_output("Wrong format")
            #return

        #the_task = Task(name, due, turned_in)

        #self.tracker.add_task(the_task)

        #self.display_output("Your task was added successfully :) !")

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

    def __init__(self, name, duedate,done):    #This is the task object
        self.name=name
        self.duedate=duedate
        self.done=done
        self.time = None



        self.find_state()

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

    BBApp = Create_GUi()
    BBApp.create_window()