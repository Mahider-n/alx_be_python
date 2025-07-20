while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid priority. Please enter high, medium, or low.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print('Please answer "yes" or "no".')

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. It's important but not time-bound. Plan accordingly.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that needs completion today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule it when convenient.")
    
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a deadline. Complete when possible.")
        else:
            # This matches the exact example output for low priority non-time-bound tasks
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")