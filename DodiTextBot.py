"""
Author: Shannon Hobby

Date: 2/17/2020

Description: Dodi is meant to aid the user in time management planning.
The idea is to be able to input how much time you have, along with what tasks you
want to accomplish and how much time you expect them to take.

Version 1.0.0 goals:
-Be able to input total time you have, tasks, how much time for each task
-have Dodi warn the user if they have put too much on their plate
-display every task in a nice manner
-be able to update tasks as you complete them


Stretch:
-potentially be able to automatically count down the time
-Look into if notifications are feasible and how they could be used
-rate task by importance
-Dodi can use priorities to suggest either adding or sbtracting things you would like to get done
-Have a separate overall todo list that Dodi can take suggestions from



    """
class task:
    def __init__(task, description, finishTime):
        task.description = description
        task.finishTime = finishTime




def home():
    taskInputDone= False
    taskInput=False
    taskList = []
    print("Hello! How much time do we have today?: ")
    totalTime= input()
    done = False
    while(not done):
        if(totalTime.isdigit() and int(totalTime) < 24):
           totalTime = int(totalTime)
           done = True
            
        else:
            print("That's not a valid time :( try again")
            totalTime = input()
        
    timeLeft = totalTime
    while(taskInputDone != True):
        if(taskInput != True) :
            print("What would you like to get done today?")
            taskInput=True
        else:
            newTask = inputTask(timeLeft)
            taskList += [newTask]
            timeLeft -= newTask.finishTime
            taskInput= False
            if(timeLeft<=0):
                print("Looks like we're out of time! Let's get started :)")
                taskInputDone = True
            else:
                print("Would you like to input another task? Y/N")
                cont = input()
                no = ["n","N", "NO", "No" , "no", "nO"]
                if (cont in no):
                    if(timeLeft > 0):
                        print("and you still have " + str(timeLeft) + " hours of free time!")
                    taskInputDone = True

   # showList(taskList, timeLeft, totalTime)
                
        
            

#Allows the user to input a new task description and time
def inputTask(totalTime):
    newTaskDescription = input()
    print("How long do you expect this to take?")
    newTime = input()
    done = False

    while(not done):
        if(not newTime.isdigit() or int(newTime) > totalTime):
            print("Oh no! That's an invalid time. Try again. You have " + str(totalTime) + " hours left")
            newTime = input()
        else:
            newTime = int(newTime)
            done = True
    newTask = task(newTaskDescription, newTime)
    print("Great! This task has been added to your list. You now have " + str(totalTime - newTime) + " hours left")
    return newTask


#display for tasks
def showLIst(taskList, timeLeft, totalTime):
    pass
    


if __name__ == "__main__":
    home()
