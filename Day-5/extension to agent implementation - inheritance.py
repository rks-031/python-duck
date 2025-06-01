class Agent:
    def __init__(self, agent_name, task):
        self.agent_name = agent_name
        self.task = task
        self.todo_map = {}

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


# 🔹 A ReminderAgent that reminds you about the most urgent task
class ReminderAgent(Agent):
    def remind_next(self):
        if not self.todo_map:
            print("No tasks to remind.")
            return
        earliest = min(self.todo_map)
        print(f"⏰ Reminder: Your next task is '{self.todo_map[earliest]}' due in {earliest} minutes!")


# 🔹 A CountAgent that tells how many tasks are due within the next X minutes
class CountAgent(Agent):
    def count_urgent_tasks(self, within_minutes):
        urgent_tasks = [d for d in self.todo_map if d <= within_minutes]
        print(f"You have {len(urgent_tasks)} task(s) due within the next {within_minutes} minutes.")


# 🔹 A ClearAgent that can clear all todos
class ClearAgent(Agent):
    def clear_all_todos(self):
        self.todo_map.clear()
        print("✅ All todos have been cleared.")


# Example usage
agent1 = ReminderAgent("Toby", "I remind users about their most urgent todo.")
agent1.about_agent()
agent1.ask_user()
agent1.show_priority_wise_todos()
agent1.remind_next()

