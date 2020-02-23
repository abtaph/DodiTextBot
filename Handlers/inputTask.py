from models.task import task


# Allows the user to input a new task description and time
def inputTask(totalTime):

    newTaskDescription = input()
    print("How long do you expect this to take?")
    newTime = input()
    done = False

    while(not done):
        if(not newTime.isdigit() or int(newTime) > totalTime.hour):
            print("Oh no! That's an invalid time. Try again. You have " +
                  str(totalTime) + " hours left")
            newTime = input()
        else:
            newTime = int(newTime)
            done = True
    newTask = task(newTaskDescription, newTime)
    print("Great! This task has been added to your list.")
    return newTask
