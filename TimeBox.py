import datetime

# ask user for beginning and end of day
beginning_of_day = input("Enter the beginning of the day (format: HH:MM AM/PM): ")
end_of_day = input("Enter the end of the day (format: HH:MM AM/PM): ")

# create datetime objects for the beginning and end of the day
beginning_of_day = datetime.datetime.strptime(beginning_of_day, '%I:%M %p')
end_of_day = datetime.datetime.strptime(end_of_day, '%I:%M %p')

# calculate the total available time for the day
total_time = (end_of_day - beginning_of_day).total_seconds() / 60

# ask user for tasks and their details
tasks = []
while True:
    task = input("Enter task name (or 'done' to finish): ")
    if task.lower() == 'done':
        break
    duration = int(input("Enter task duration in minutes: "))
    severity = input("Enter task severity level ('high', 'medium', 'low'): ")
    tasks.append((task, duration, severity))

# sort tasks by severity level (high > medium > low)
tasks.sort(key=lambda x: {'high': 3, 'medium': 2, 'low': 1}[x[2]])

# allocate time for each task
time_allocated = 0
for task in tasks:
    task_name, duration, severity = task
    allocated_time = duration
    if severity == 'high':
        allocated_time = duration * 1.5
    if time_allocated + allocated_time > total_time:
        break
    time_allocated += allocated_time
    start_time = beginning_of_day + datetime.timedelta(minutes=time_allocated - allocated_time)
    end_time = beginning_of_day + datetime.timedelta(minutes=time_allocated)
    print(f"{task_name}: {start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}")

# print remaining time in the day
remaining_time = total_time - time_allocated
print(f"Remaining time: {remaining_time} minutes")
