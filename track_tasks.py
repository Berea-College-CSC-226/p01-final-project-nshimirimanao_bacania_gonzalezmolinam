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
