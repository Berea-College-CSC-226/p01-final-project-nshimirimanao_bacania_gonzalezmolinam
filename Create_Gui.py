import tkinter as tk
class Create_GUi:

    def __init__(self):
        self.window = None
        self.buttons = {}
        self.input = {}

        #self.tracker = Track_tasks()
       # self.validate = Valid_input()

    def create_window(self):
        self.window = tk.TK()
        self.window.title("Berea Busy")
        self.window.size(800,800)

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

    def display_output(self):

        pass
    def create_button(self):
        pass

   ## def main():
        ##pass
   ## main()

