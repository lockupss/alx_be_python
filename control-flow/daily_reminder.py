task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Complete it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but it is time-bound. Try to do it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level.")
