

# Todo List

global_list=[]

def add_task(taskName):
    global_list.append(taskName)
    print(f"New task added:{taskName}")

def view_list():

    for i,item in enumerate(global_list,start=1):
        print(i,item)

def del_task(taskIndex):
    global_list.pop(taskIndex-1)
    print(f"{taskIndex} is deleted from list")


print("TODO List App")
print("1:Add Task")
print("2:View List")
print("3:Delete Task")


while(True):
    try:
        user_choice= int(input("Enter your choice (1:Add Task,2:View List, 3:Delete Task):"))

        if(user_choice==1):
            print("__________________________")
            addTaskInput=input("Enter name of task, Add to the list:")
            add_task(addTaskInput)


        elif(user_choice==2):
            view_list()

        elif(user_choice==3):
            
            print("__________________________")
            view_list()
            print("__________________________")



            deleteTaskInput= int(input("Enter the number of task, Delete from the list:"))
            del_task(deleteTaskInput)
            
            print("__________________________")
            view_list()
            print("__________________________")

        
        else:
            print("Thank you for using our app")
            break

    except:
        print("Please only enter number from list")
