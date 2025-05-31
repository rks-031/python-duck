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
        while user_choice == 'Y' or user_choice == 'y':
            user_task = input("Enter your todo task: ")
            user_deadline = int(input("Enter the deadline in minutes: "))
            self.add_todo(user_deadline, user_task)
            print("Do you wish to continue adding todos? (Y/N)")
            user_choice = input().strip()

    def show_priority_wise_todos(self):
        print("Here are your todos based on deadline priority:")
        for deadline in sorted(self.todo_map.keys()):
            print(f"Deadline: {deadline} minutes, Task: {self.todo_map[deadline]}")

# Example usage
agent1 = Agent("Toby", "I am a todo sorter agent. I sort users todo based on priroity")
agent1.about_agent()
agent1.ask_user()
agent1.show_priority_wise_todos()