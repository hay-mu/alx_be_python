task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task priority '{priority}' is not recognized."


if priority in {"high", "medium", "low"}:
    if time_bound == "yes":
        
        if priority == "low":
            message += ". Consider completing it when you have free time."
        else:
            message += " that requires immediate attention today!"
    elif time_bound == "no":
        if priority == "low":
            message += ". Consider completing it when you have free time."
        else:
            message += ". You can plan it accordingly."
    else:
        message += ". Time-bound input not recognized."

print(message)