# display for tasks
def showList(taskList, timeLeft, totalTime):
    count = 1
    print("=====================TASK LIST================")
    print("TIME LEFT: " + str(timeLeft.hour) + " hours and " +
          str(timeLeft.minutes) + " minutes OUT OF: " + str(totalTime) + " hours.")
    taskTime = 0
    for task in taskList:
        taskTime += task.finishTime
    if(totalTime >= taskTime):
        print("You have " + str(timeLeft.hour-taskTime) + " hours of free time")
    else:
        print("Oh no! It looks like you can't get all of this done in the allotted time. \
         \n !I would suggest removing an item or updating the amount of time it will take.")
    if len(taskList) == 0:
        print("NO MORE TASKS! GREAT JOB :)")
        print("if you would like to add another... type add task")
    else:
        for task in taskList:
            print(str(count) + ": " + str(task.description) +
                  " will take " + str(task.finishTime) + " hours")
            count += 1
