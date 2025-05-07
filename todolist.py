# CLASS DEFINITION

class ToDoCLI:

    def __init__(self):
        self.pending: list[str] = []
        self.completed: list[str] = []

    # MENU DISPLAY

    @staticmethod
    def show_menu() -> None:
        print("\n***** Users Menu *****")
        print("\n1. Create a task")
        print("2. Edit a task")
        print("3. Delete a task")
        print("4. Mark a task as complete")
        print("5. Exit")

    def create_task(self):
        
        while True:
            task = input("Add your task:").strip()
            
            if not task or task.isdigit():
                print("Enter a valid task:")
                continue
            self.pending.append(task)
            print(f"{task}, has been added")
            break

    def show_tasks(self, tasks: list[str], empty_msg: str) -> None:
        
        if not tasks:
            print(empty_msg)
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}: {task}")

    @staticmethod
    def ask_back_or_forward() -> bool:
        #Return True if user chooses 'f', False if 'b'.
        
        while True:
            choice = input("Press 'b' to go back or 'f' to move forward: ").lower()
            
            if choice in ("b", "f"):
                return choice == "f"
            print("Enter a valid option:")

    def edit_task(self):
        self.show_tasks(self.pending, "No pending tasks.")
        
        if not self.pending:
            return  # early‑exit if nothing to edit
        if not self.ask_back_or_forward():
            return
        
        while True:
            
            idx_txt = input("Which task do you want to edit? (number): ").strip()
            try:
                idx = int(idx_txt)
            except ValueError:
                print("Enter a numerical value:")
                continue
            
            if 1 <= idx <= len(self.pending):
                while True:
                    new_task = input("Enter your new task:").strip()
                    
                    if not new_task or new_task.isdigit():
                        print("Enter a valid task:")
                        continue
                    # store trimmed version to avoid stray spaces
                    self.pending[idx - 1] = new_task
                    print(f"Task updated to: {new_task}")
                    return  # finished editing
            
            print("Enter a number that matches a task:")

    def delete_task(self):
        self.show_tasks(self.pending, "No pending tasks.")
        
        if not self.pending:
            return
        
        if not self.ask_back_or_forward():
            return
        
        while True:
            idx_txt = input("Which task delete? (number): ").strip()
            
            try:
                idx = int(idx_txt)
            except ValueError:
                print("Enter a numerical value:")
                continue
            
            if 1 <= idx <= len(self.pending):
                deleted = self.pending.pop(idx - 1)
                print(f"Task: {deleted}, has been deleted")
                return
            
            print("Enter a number that matches a task:")

    def complete_task(self):
        self.show_tasks(self.pending, "No pending tasks.")
        
        if not self.pending:
            return
        
        if not self.ask_back_or_forward():
            return
        
        while True:
            idx_txt = input("Which task is completed? (number): ").strip()
            try:
                idx = int(idx_txt)
            except ValueError:
                print("Enter a numerical value:")
                continue
            
            if 1 <= idx <= len(self.pending):
                done = self.pending.pop(idx - 1)
                self.completed.append(done)
                print(f"Task: {done}, marked as complete ✅. Congratulations!")
                return
            
            print("Enter a number that matches a task:")

    # 4) MAIN LOOP

    def run(self):
        while True:
            self.show_menu()
            print("\nPending Tasks:")
            self.show_tasks(self.pending, "No pending tasks.")
            
            try:
                choice = int(input("\nEnter an option (1-5): "))
                if choice not in range(1, 6):
                    raise ValueError
            except ValueError:
                print("Enter a numerical value from 1 to 5.")
                continue

            if choice == 1:
                self.create_task()
            elif choice == 2:
                self.edit_task()
            elif choice == 3:
                self.delete_task()
            elif choice == 4:
                self.complete_task()
            else:
                print("\nPending tasks:")
                self.show_tasks(self.pending, "No pending tasks.")
                print("\nCompleted tasks:")
                self.show_tasks(self.completed, "No completed tasks.")
                break  # exit



if __name__ == "__main__":
    ToDoCLI().run()