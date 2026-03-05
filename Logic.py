import Database

class Operation:
    def __init__(self):
        self.database = Database.Json()

    def add_task(self, description):
        id_counter = self.database.generate_id()
        data = {"id" : id_counter, "task" : description, "status" : None}
        self.database.tasks.append(data)
        self.database.save_task()
        print(f"Task added successfully (ID:{id_counter})")

    def update_add(self, id, description):
        for 

