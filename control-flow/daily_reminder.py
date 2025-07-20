# daily_reminder.py

def get_valid_input(prompt, valid_options):
    """Loop until user enters a valid response."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Please enter one of the following: {', '.join(valid_options)}")

def main():

    # Prompt for task, priority, and time-bound status
    task = input("Enter your task: ").strip()
    priority = get_valid_input("Priority (high/medium/low): ", ["high", "medium", "low"])
    time_bound = get_valid_input("Is it time-bound? (yes/no): ", ["yes", "no"])

    # Match-case based on priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has unknown priority"

    # Final output based on time-bound status
    if time_bound == "yes":
        print(f"\nReminder: {message} that requires immediate attention today!")
    else:
        print(f"\nNote: {message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()

