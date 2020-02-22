# display for tasks
def showList(taskList, timeLeft, totalTime):
    count = 1
    print("=====================TASK LIST================")
    print("TIME LEFT: " + str(timeLeft) +
          " hours OUT OF: " + str(totalTime) + " hours")
    if not taskList:
        print("NO MORE TASKS! GREAT JOB :)")
        print("if you would like to add another... type add task")
    else:
        for task in taskList:
            print(str(count) + ": " + str(task.description) +
                  " will take " + str(task.finishTime) + " hours")
            count += 1
