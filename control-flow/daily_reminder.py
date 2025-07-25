# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Prepare the priority-specific message using match-case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Append time-sensitivity info
if time_bound == "yes":
    final_message = f"{base_message} that requires immediate attention today!"
else:
    final_message = f"{base_message}. Consider completing it when you have free time."

# ✅ This line matches what the test expects exactly
print(f"Reminder: {final_message}")
