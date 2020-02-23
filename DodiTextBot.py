"""
Author: Shannon Hobby

Date: 2/17/2020

Description: Dodi is meant to aid the user in time management planning.
The idea is to be able to input how much time you have, along with what tasks you
want to accomplish and how much time you expect them to take.

Version 1.0.0 goals:
x-Be able to input total time you have, tasks, how much time for each task
x-have Dodi warn the user if they have put too much on their plate
x-display every task in a nice manner
x-be able to update tasks as you complete them


Stretch:
x-potentially be able to automatically count down the time
-Look into if notifications are feasible and how they could be used
-rate task by importance
-Dodi can use priorities to suggest either adding or subtracting things you would like to get done
-Have a separate overall todo list that Dodi can take suggestions from
-add GUI



    """
from Handlers.inputTask import *
from Handlers.showList import *
from Handlers.updateList import *
from models.task import *
from models.timeRep import *


def home():
    close = False
    taskList = []
    print("Hello! How much time do we have today?: ")
    totalTime = input()
    done = False
    while(not done):
        if(totalTime.isdigit() and int(totalTime) < 24):
            totalTime = int(totalTime)
            done = True

        else:
            print("That's not a valid time :( try again")
            totalTime = input()

    timeFinish = timeRep(int(time.strftime("%I")) +
                         totalTime, int(time.strftime("%M")))
    print("You have until " + str(timeFinish.hour) +
          ":" + str(timeFinish.minutes) + time.strftime("%p"))
    timeLeft = timeFinish - \
        timeRep(int(time.strftime("%I")), int(time.strftime("%M")))

    print("What would you like to get done today?")
    newTask = inputTask(timeLeft, timeFinish)
    taskList += [newTask]
    timeLeft = timeRep(
        timeLeft.hour - newTask.finishTime, timeLeft.minutes)

    while(not close):
        timeLeft = timeFinish - \
            timeRep(int(time.strftime("%I")), int(time.strftime("%M")))
        showList(taskList, timeLeft, totalTime)
        taskList = updateList(taskList, timeLeft)


if __name__ == "__main__":
    home()
