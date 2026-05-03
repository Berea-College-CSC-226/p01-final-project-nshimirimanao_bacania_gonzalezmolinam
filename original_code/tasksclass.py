
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