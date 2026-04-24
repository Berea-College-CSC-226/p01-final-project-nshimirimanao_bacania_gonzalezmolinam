import tkinter as tk
class Create_GUi:

    def __init__(self):
        self.window = None
        self.buttons = {}
        self.input = {}

        #self.tracker = Track_tasks()
       # self.validate = Valid_input()

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

    def get_input(self):
        name = self.input["Name"].get()
        due = self.input["Due date"].get()
        turned_in = self.input["Turned in"].get()

        if not self.validate.check_none([name,due,turned_in]):
            self.display_output("There seems to be something missing, make sure you fill in everything.")
            return

        if not self.validate.validate_userinput(due, turned_in):
            self.display_output("Wrong format")
            return

        the_task = Task(name, due, turned_in)

        self.tracker.add_task(the_task)

        self.display_output("Your task was added successfully :) !")

    def display_output(self,message):

        self.output_label.config(text=message)

    def create_button(self):

        self.buttons["add"] = tk.Button (self.window, text = "Add New Task", command=self.get_input)
        self.buttons["add"].pack()

if __name__ == "__main__":

    BBApp = Create_GUi()
    BBApp.create_window()

