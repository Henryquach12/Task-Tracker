import Database

class Operation:
    def __init__(self):
        self.database = Database.Json()

    def add_task(self, description, task=None):
        id_counter = self.database.generate_id()
        data = {"id" : id_counter, "task" : description, "status" : None}
        self.database.tasks.append(data)
        self.database.save_task()
        print(f"Task added successfully (ID:{id_counter})")

    def update_task(self, ID, description):
        for task in self.database.tasks:
            if task["id"] == ID:
                task["task"] = description
                return self.database.save_task()
        print("No record was found! Check ID again...")

    def delete_task(self, ID):
        self.database.tasks = [task for task in self.database.tasks if task["id"] != ID]
        for task in self.database.tasks:
            if task["id"] > ID:
                task["id"] -= 1
        self.database.save_task()
                


