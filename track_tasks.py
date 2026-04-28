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

# Practice GUI:

# import tkinter as tk
# from tkinter import messagebox
#
# class TrackTasks:
#     def __init__(self):
#         self.assignments = []
#
#     def add_task(self, task):
#         self.assignments.append(task)
#
#     def update_task(self, index, new_task):
#         if 0 <= index < len(self.assignments):
#             self.assignments[index] = new_task
#         else:
#             return False
#         return True
#
#     def display_tasks(self):
#         return self.assignments
#
#
# class TaskGUI:
#     def __init__(self, root):
#         self.tracker = TrackTasks()
#         self.root = root
#         self.root.title("Task Tracker")
#
#         # Entry for task input
#         self.task_entry = tk.Entry(root, width=40)
#         self.task_entry.pack(pady=10)
#
#         # Add button
#         self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
#         self.add_button.pack()
#
#         # Update button
#         self.update_button = tk.Button(root, text="Update Selected Task", command=self.update_task)
#         self.update_button.pack()
#
#         # Listbox to display tasks
#         self.task_listbox = tk.Listbox(root, width=50)
#         self.task_listbox.pack(pady=10)
#
#     def refresh_listbox(self):
#         self.task_listbox.delete(0, tk.END)
#         for task in self.tracker.display_tasks():
#             self.task_listbox.insert(tk.END, task)
#
#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.tracker.add_task(task)
#             self.refresh_listbox()
#             self.task_entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Warning", "Please enter a task.")
#
#     def update_task(self):
#         selected = self.task_listbox.curselection()
#         new_task = self.task_entry.get()
#
#         if not selected:
#             messagebox.showwarning("Warning", "Select a task to update.")
#             return
#
#         if not new_task:
#             messagebox.showwarning("Warning", "Enter the new task text.")
#             return
#
#         index = selected[0]
#         success = self.tracker.update_task(index, new_task)
#
#         if success:
#             self.refresh_listbox()
#             self.task_entry.delete(0, tk.END)
#         else:
#             messagebox.showerror("Error", "Invalid task number.")
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TaskGUI(root)
#     root.mainloop()