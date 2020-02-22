from models.task import task
from Handlers.inputTask import *


def updateList(taskList, timeLeft):
    "let me know when you've completed or worked on a task!"
    userInput = input()
    update = ["started", "start", "update", "updated"]
    finish = ["finish", "complete", "completed", "done"]
    remove = ["remove", "delete"]
    add = ["add task", "add"]
    if(userInput in update):
        print("please give the task number that you wish to update")
        taskNumber = input()
        for task in range(1, taskList.length):
            if taskNumber == task:
                taskNumber = taskList[task]
        print(str(taskNumber) + " how much time did you work on this task?")
        taskTime = input()
        done = False
        while(not done):
            if(taskTime.isDigit()):
                done = True
            else:
                print("That's not a valid time... Try again")
        if (taskTime < taskNumber.finishTime):
            taskNumber = taskNumber - taskTime
        else:
            userInput = "finish"
    elif(userInput in finish):
        print("Great job! Please give the number of the task you finished")
        taskNumber = input()
        print("im here")
        for task in range(0, len(taskList)-1):
            if int(taskNumber)-1 == task:
                print("taskList: " + str(taskList))
                taskList.pop(task)
                print("taskList: " + str(taskList))
                return taskList
    elif(userInput in add):
        print("Input your task description")
        taskList += inputTask(timeLeft)
        return taskList
    elif(userInput in remove):
        print("Please give the number of the task you want to remove")
        taskNumber = input()
        for task in range(0, len(taskList)-1):
            if taskNumber-1 == task:
                taskList.pop(task)
                return taskList
