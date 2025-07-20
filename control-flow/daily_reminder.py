# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match case to determine base message based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Add urgency if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the customized reminder
print(message)
