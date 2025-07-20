while True:
    task = input("Enter your task: ").strip()
    if task:  # Ensure task isn't empty
        break
    print("Task cannot be empty. Please enter a valid task.")

# Get valid priority input
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid priority. Please enter high, medium, or low.")

# Get valid time-bound input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print('Please answer "yes" or "no".')

# Process and generate reminder
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". It's important but not time-bound. Plan accordingly."
    
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that needs completion today!"
        else:
            reminder += ". Schedule it when convenient."
    
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but has a deadline. Complete when possible."
        else:
            reminder += ". Consider completing it when you have free time."

print("\n" + reminder)