import Database
from datetime import date

class Operation:
    def __init__(self):
        self.database = Database.Json()
        self.time = date.today().isoformat()

    def add_task(self, description, task=None):
        id_counter = self.database.generate_id()
        data = {"id" : id_counter, "task" : description, "status" : 'todo', "createdAt": self.time, "updateAt": self.time}
        self.database.tasks.append(data)
        self.database.save_task()
        print(f"Task added successfully (ID:{id_counter})")

    def update_task(self, ID, description):
        for task in self.database.tasks:
            if task["id"] == ID:
                task["task"] = description
                task["updateAt"] = self.time
                print(f"Task updated successfully (ID:{ID})")
                return self.database.save_task()
        print("No record was found! Check ID again...")

    def delete_task(self, ID):
        valid_id = any(task["id"] == ID for task in self.database.tasks)
        if not valid_id:
            print("ID of task does not exist!")
            return
        self.database.tasks = [task for task in self.database.tasks if task["id"] != ID]
        for task in self.database.tasks:
            if task["id"] > ID:
                task["id"] -= 1
        print(f"Task deleted successfully (ID:{ID})")
        self.database.save_task()

    def mark_task(self, ID, status):
        valid_id = any(task["id"] == ID for task in self.database.tasks)
        if not valid_id:
            print("ID of task does not exist!")
            return
        for task in self.database.tasks:
            if task["id"] == ID:
                if status == "mark-in-progress":
                    task["status"] = "in-progress"
                else:
                    task["status"] = "done"
        print(f"Task marked successfully (ID:{ID})")
        return self.database.save_task()
    
    def list_task(self, status=None):
        print(f"{'ID':<3} {'Task':<20} {'Status':<12}")
        print("-"*35)
        if status == None:
            for task in self.database.tasks:
                print(f"{task['id']:<3} {task['task']:<20} {task['status']:<12}")
        else:
            for task in self.database.tasks:
                if task['status'] == status:
                    print(f"{task['id']:<3} {task['task']:<20} {task['status']:<12}")

    
                


