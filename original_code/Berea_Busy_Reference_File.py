# referencing chatgpt by asking it to add " how would you make this into a program that tracks homework assignments,
# has a timer to make sure they're being submitted on time, include a reward system, ensure valid input is being given,
# and has a checkmark box that can separate the ones that are to be completed and the ones that are done with the rewards
# being + 10 points if early, + 5 points if on time, -5 points if late. Here is the code: (Berea Busy Final.py)"

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re


class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = False
        self.completed_time = None
        self.points = 0
        self.state = "To Do"

    def mark_done(self):
        self.done = True
        self.completed_time = datetime.now()

        if self.completed_time < self.due_date:
            self.state = "Early"
            self.points = +10
        elif self.completed_time == self.due_date.date():
            self.state = "On Time"
            self.points = +5
        else:
            self.state = "Late"
            self.points = -5

    def time_left(self):
        now = datetime.now()

        if self.done:
            return self.state

        if now > self.due_date:
            return "Overdue"

        remaining = self.due_date - now
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{days}d {hours}h {minutes}m {seconds}s left"


class ValidInput:
    @staticmethod
    def valid_name(name):
        return name.strip() != "" and re.match(r"^[A-Za-z0-9 ]+$", name)

    @staticmethod
    def valid_due_date(date_text):
        try:
            return datetime.strptime(date_text, "%m/%d/%Y %H:%M")
        except ValueError:
            return None


class HomeworkTrackerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Berea Busy")
        self.window.geometry("900x700")

        self.tasks = []
        self.total_points = 0

        self.name_entry = None
        self.date_entry = None
        self.todo_frame = None
        self.done_frame = None
        self.points_label = None

        self.create_window()

    def create_window(self):
        self.window.config(bg="lightblue") #makes background blue #found reference code from python guide https://pythonguides.com/tkinter-frame-background-color/

        title = tk.Label(self.window, text="Berea Busy Task Tracker", font=("Helvetica", 22), bg="lightblue")
        title.pack(pady=10)

        form_frame = tk.Frame(self.window)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Assignment Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Due Date: MM/DD/YYYY HH:MM").grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(form_frame, width=30)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        add_button = tk.Button(form_frame, text="Add Assignment", command=self.add_task)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.points_label = tk.Label(self.window, text="Total Points: 0", font=("Arial", 16),bg="lightblue")
        self.points_label.pack(pady=10)

        sections_frame = tk.Frame(self.window)
        sections_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.todo_frame = tk.LabelFrame(sections_frame, text="To Be Completed", font=("Arial", 14))
        self.todo_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.done_frame = tk.LabelFrame(sections_frame, text="Done", font=("Arial", 14))
        self.done_frame.pack(side="right", fill="both", expand=True, padx=10)

        self.update_timer()
        self.window.mainloop()

    def add_task(self):
        name = self.name_entry.get()
        due_text = self.date_entry.get()

        if not ValidInput.valid_name(name):
            messagebox.showerror("Invalid Input", "Assignment name cannot be empty and can only use letters, numbers, and spaces.")
            return

        due_date = ValidInput.valid_due_date(due_text)

        if due_date is None:
            messagebox.showerror("Invalid Date", "Use this format: MM/DD/YYYY HH:MM")
            return

        task = Task(name, due_date)
        self.tasks.append(task)

        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        self.refresh_tasks()

    def complete_task(self, task):
        if not task.done:
            task.mark_done()
            self.total_points += task.points
            self.points_label.config(text=f"Total Points: {self.total_points}")
            self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        for widget in self.done_frame.winfo_children():
            widget.destroy()

        for task in self.tasks:
            if task.done:
                text = f"✓ {task.name}\n{task.state}: {task.points} points"
                label = tk.Label(self.done_frame, text=text, anchor="w", justify="left")
                label.pack(fill="x", padx=10, pady=5)
            else:
                var = tk.IntVar()

                text = f"{task.name}\nDue: {task.due_date.strftime('%m/%d/%Y %H:%M')}\n{task.time_left()}"

                checkbox = tk.Checkbutton(
                    self.todo_frame,
                    text=text,
                    variable=var,
                    command=lambda t=task: self.complete_task(t),
                    anchor="w",
                    justify="left"
                )

                checkbox.pack(fill="x", padx=10, pady=5)

    def update_timer(self):
        self.refresh_tasks()
        self.window.after(1000, self.update_timer)


if __name__ == "__main__":
    app = HomeworkTrackerGUI()

    # test run
    # 05/03/2026 12:59

    # 05/03/2026 12:30