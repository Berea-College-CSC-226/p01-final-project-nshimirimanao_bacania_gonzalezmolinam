class Task:

    """
    This function is going to check the status of the assignments,
    if they're late, on time or early
    """



    def __init__(self, name, duedate,done):    #This is the task object
        self.name=name
        self.duedate=duedate
        self.done=done
        self.time = None
