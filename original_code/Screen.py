
import tkinter as tk


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


if __name__ == "__main__":
    BBApp = Create_GUi()
    BBApp.create_window()

