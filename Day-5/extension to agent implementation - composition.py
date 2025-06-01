class Agent:
    def __init__(self, agent_name, task):
        self.agent_name = agent_name
        self.task = task
        self.todo_map = {}
        # Composed helpers
        self.reminder = Reminder(self)
        self.counter = TaskCounter(self)
        self.clearer = Clearer(self)

    def about_agent(self):
        print(f"Hi, I am {self.agent_name} and {self.task}")

    def add_todo(self, user_deadline, user_task):
        self.todo_map[user_deadline] = user_task

    def ask_user(self):
        print("Please tell about your immediate todo task and the deadline in minutes starting now.")
        user_choice = 'Y'
        while user_choice.lower() == 'y':
            user_task = input("Enter your todo task: ")
            user_deadline = int(input("Enter the deadline in minutes: "))
            self.add_todo(user_deadline, user_task)
            print("Do you wish to continue adding todos? (Y/N)")
            user_choice = input().strip()

    def show_priority_wise_todos(self):
        print("Here are your todos based on deadline priority:")
        for deadline in sorted(self.todo_map.keys()):
            print(f"Deadline: {deadline} minutes, Task: {self.todo_map[deadline]}")


# Helper class: Reminder
class Reminder:
    def __init__(self, agent):
        self.agent = agent

    def remind_next(self):
        if not self.agent.todo_map:
            print("No tasks to remind.")
            return
        earliest = min(self.agent.todo_map)
        print(f"Reminder: Your next task is '{self.agent.todo_map[earliest]}' due in {earliest} minutes!")

# Helper class: TaskCounter
class TaskCounter:
    def __init__(self, agent):
        self.agent = agent

    def count_urgent_tasks(self, within_minutes):
        urgent = [d for d in self.agent.todo_map if d <= within_minutes]
        print(f"You have {len(urgent)} task(s) due within the next {within_minutes} minutes.")


# Helper class: Clearer
class Clearer:
    def __init__(self, agent):
        self.agent = agent

    def clear_all_todos(self):
        self.agent.todo_map.clear()
        print("All todos have been cleared.")


# --- Example usage ---
agent = Agent("Toby", "I am a todo manager with modular skills.")
agent.about_agent()
agent.ask_user()
agent.show_priority_wise_todos()
agent.reminder.remind_next()
agent.counter.count_urgent_tasks(within_minutes=30)
agent.clearer.clear_all_todos()
