class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority

#creating an empty array
tasks = []

while True:
    title = input("Enter task title or q to quit:  ")

    if(title =="q"):
        break

    priority = input("Enter priority: ")


    task = Task(title,priority)

#add task object to the tasks array
    tasks.append(task)
    print(len(tasks))

#print everything in the tasks array
for task in tasks:
    print(task.title)
    print(task.priority)
print("Thank you for using the App!")

# print(task.title)
# print(task.priority)
