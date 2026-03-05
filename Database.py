import json
import os
class Json:
    def __init__(self):
        self.file = "task_tracker.json"
        self.check_file()
        self.tasks = self.load_task()
        self.generate_id()

    def check_file(self):
        if not os.path.exists(self.file) or os.stat(self.file).st_size == 0:
            with open(self.file, "w") as f:
                json.dump([], f)

    def save_task(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)
    
    def load_task(self):
        with open(self.file, "r") as f:
            self.tasks = json.load(f)
        return self.tasks
    
    def generate_id(self):
        id_counter = max((task["id"] for task in self.tasks), default=0) +1
        return id_counter



            