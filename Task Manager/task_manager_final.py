# The program allows user to login if user is admin then the user can register other users 
# and generate reports and view the reports.
# Users can add tasks, view all tasks and tasks only assigned to them
import sys
import re
import datetime

#if the user selects 'a' they are able to add another task into the text document
def add_task():
    
        task_file = open("tasks.txt", "a+")

        user = input("Enter the username of the person the task is assigned to: ")
        task = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        assigned_date = input("Enter the date the task was assigned: ")
        due_date = input("Enter the due date of your task: ")
        is_completed = input("Is the task completed: ")

        task_file.write(f"\n{user}, {task}, {description}, {assigned_date}, {due_date}, {is_completed}")
        task_file.close()
        return None

#This function is used to register a new user
#if the user exists in the text file it will give an error
def reg_user():
        gredentials = False
    
        while gredentials == False:
            user_file = open("user.txt", "a+")
            new_user = input("Enter your created username: ")
            new_password = input("Enter your created password: ")
            confirm_password = input("Re-enter your created password: ")

            if new_password != confirm_password:
                gredentials = False
                print("Passwords don't match. Please try again: ")
            user_file.seek(0)
            
            for line in user_file:
                valid_user = line.split(',')
                if new_password == confirm_password and new_user != valid_user[0]:
                    gredentials = True
                    user_file.write(f"\n{new_user}, {new_password}")
                    print(f"{new_user} has been registered!")
                    return None
                    
            if new_user == valid_user[0]:
                print("This username already exists, please try again.")
                gredentials = False
                user_file.seek(0)

            
        user_file.close()

#If the user selects 'va' they will be able to view all of the tasks in read mode.
def view_all():
    

        task_file = open("tasks.txt", "r")
        task_file_contents = task_file.readlines()
        print(task_file_contents)

#if the user select vm, it will open the text document of the task assigned to the user.
def view_mine():
    task_number = 0

    while task_number != -1:
        mytasks_file = open("tasks.txt", "r")
        i = 0
        for line in mytasks_file:
            user, task_title, task_description, assigned_date, due_date, is_completed = line.split(", ")
            i += 1

            if username == user:                  #If the username matches the name of the user in the text file it will display the assignments
                                                  #assigned to the user.
                print(f"""
                {i})  User                : {user}
                    Task title          : {task_title}
                    Task description    : {task_description}
                    Assigned date       : {assigned_date}
                    Due date            : {due_date}
                    Completion status   : {is_completed}
                """)
        #Here the user can edit their task        
        task_number = int(input("Choose a task number to edit or type -1 to return to the menu: "))
        
        if task_number != -1:

            with open('tasks.txt', "r") as f:
                data = f.readlines()
                item = data[task_number - 1].split(',')

            complete = input("Do you want to mark the task as complete?(Yes/No): ")
            uppercase_complete = complete.upper()
            uppercase_Yes = item[5].upper()

            if uppercase_Yes == " YES" or uppercase_Yes == " YES\n":
                print("Selected option cannot be edited")
                return None

            if uppercase_complete != "YES" and (uppercase_Yes != " YES" or uppercase_Yes != " YES\n"):
                new_username = input("Please enter the new user to which the task will be assigned to: ")
                new_due_date = input("Please enter the new due date for task: ")
                items = data[task_number - 1].split(',')
                items[0] = new_username
                items[4] = new_due_date
                data[task_number - 1] = str(items)[1:-1].replace('\'', ' ')
                data[task_number - 1].strip('\n')
                print("Edit was successfull")
            
            if task_number == len(data) and uppercase_complete != "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}")
                return None

            if task_number != len(data) and uppercase_complete != "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}\n")
                return None

            if uppercase_complete == "YES":
                items = data[task_number - 1].split(',')
                items[5] = "Yes"
                data[task_number - 1] = str(items)[1:-1].replace('\'', ' ')
                data[task_number - 1].strip('\n')
                print("Edit was successfull")

            if task_number == len(data) and uppercase_complete == "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}")
                return None
            
            if task_number != len(data) and uppercase_complete == "YES":
                with open('tasks.txt', 'w') as f:
                    for line in data:
                        line.strip('\n') 
                        f.write(f"{line}\n")
                return None

        if task_number == -1:
            print("Please select one of the following options: ")					#Here we ask the user to select one of the following options in the menu.
        if username == "admin" and password == "adm1n":    
          print("r\t    -  register user\n")
        print("a\t    -  add task\n")
        print("va\t   -  view all tasks\n")
        print("vm\t   -  view my tasks\n")
        if username == "admin" and password == "adm1n":
          print("gr\t   - generate reports\n")
          print("ds\t   - display statistics\n")
        print("e\t    -  exit")
  
        choice = input("Enter your selected choice: ")
        if choice == "r":
            reg_user()

        elif choice == "a":
           add_task()

        elif choice == "va":
           view_all()

        elif choice == "vm":
           view_mine()

        elif choice == "gr":
           generate_reports()

        elif choice == "ds":
           display_statistics()

        elif choice == "e":
           print("Programme Terminated")
        elif choice != "e" and choice != "vm" and choice != "va" and choice != "a" and choice != "r" and choice != "e": 
         print("Your selection is invalid, please try again: ")
        mytasks_file.close()
        return None

def generate_reports():

    x = 0
    y = 0
    z = 0
    i = 0
    a = 0
    b = 0
    c = 0
    uppercase_username = username.upper()

    with open('tasks.txt') as f:
        tasks = f.readlines()
        num_tasks = len(tasks)

        for line in tasks:
            items = line.upper().split(',')
            if items[5] == " YES\n" or items[5] == " YES":
                i += 1 #completed tasks

            if items[5] == " NO\n" or items[5] == " NO":
                x += 1 #incompleted tasks

            date = datetime.datetime.strptime("10/12/2020", "%m/%d/%Y")
            date_now = datetime.datetime.today()
            if date_now >  date and (items[5] == " NO\n" or items[5] == " NO"):
                y += 1 #over due tasks
            
            if uppercase_username == items[0]:
                z += 1 #tasks assinged to user

            if uppercase_username == items[0] and (items[5] == " YES" or items[5] == " YES\n"):
                a += 1 #tasks assigned to user and completed

            if uppercase_username == items[0] and (items[5] == " NO" or items[5] == " NO\n"):
                b += 1 #tasks that are assigned to the user and are incomplete

            if uppercase_username == items[0] and (items[5] == " NO" or items[5] == " NO\n") and date_now >  date:
                c += 1 #tasks assigned to user are overdue
     
            percentage_incomplete = float((x/len(tasks))*100)
            percentage_overdue = float((y/len(tasks))*100)
            percentage_assigned = float((z/len(tasks))*100)
            percentage_assigned_complete = float((a/len(tasks))*100)
            percentage_assigned_incomplete = float((b/len(tasks))*100)
            percentage_assigned_incomplete_overdue = float((c/len(tasks))*100)

    f.close()

#This will open the task_overview text file if it doesn't exist, by using the 'w' it will be created.
    task_overview = open('task_overview.txt', 'w+')

    #We write everything to the task overview text file
    task_overview.write(f"""    Total number of tasks                           : {num_tasks}
    Total number of completed tasks                 : {i}
    Total number of uncompleted tasks               : {x}
    The total number of tasks that haven’t been completed and
that are overdue    : {y}
    The percentage of tasks that are incomplete                  : {percentage_incomplete}
    The percentage of tasks that are overdue     : {percentage_overdue}
                        """) 
    task_overview.close()
            

    with open('user.txt', 'r') as f:
        user = f.readlines()
        users = len(user)
    
    #This will open the user_overview text file if it doesn't exist, by using the 'w' it will be created.
    user_overview = open('user_overview.txt', 'w+')

    #We write everything to the user overview text file
    user_overview.write(f"""    Total number of users                       : {users}
    Total number of tasks                       : {num_tasks}
    Tatal tasks assgined to you                 : {z}
    Percentage of tasks assigned to you         : {percentage_assigned}
    Percentage of tasks you completed           : {percentage_assigned_complete}
    Percentage of tasks incomplete              : {percentage_assigned_incomplete}
    Percentage of tasks incomplete and overdue  : {percentage_assigned_incomplete_overdue}
                        """)
    user_overview.close()

    print("Reports successfully generated")
    return None

#This will display the admin's statistics
def display_statistics():
    
    display_user = open("user_overview.txt", "r") #The statistics for the users will be stored in the user_overview file.
    
    print('\nUSER OVERVIEW\n')
    for line in display_user:
        print(line)

    print('\nTASK OVERVIEW\n')
    display_task = open("task_overview.txt", "r") #The statistics for the tasks will be stored in the user_overview file.
    for line in display_task:
        print(line)
    

    return None

# we open the text document

user_file = open("user.txt", "r")
login = False

while login == False:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for line in user_file:
      valid_user, valid_password = line.strip("\n").split(", ")
      if username == valid_user or password == valid_password:
        login = True
      if username != valid_user or password != valid_password:
        print("Your password or username is incorrect")
        
        
    user_file.seek(0)    


print("Please select one of the following options: ")					#Here we ask the user to select one of the following options in the menu.
if username == "admin" and password == "adm1n":
  print("r\t    -  register user\n")
print("a\t    -  add task\n")
print("va\t   -  view all tasks\n")
print("vm\t   -  view my tasks\n")
if username == "admin" and password == "adm1n":
  print("gr\t   - generate reports\n")
  print("ds\t   - display statistics\n")

print("e\t    -  exit")
  
choice = input("Enter your selected choice: ")
if choice == "r":
    reg_user()

elif choice == "a":
    add_task()

elif choice == "va":
    view_all()

elif choice == "vm":
    view_mine()

elif choice == "gr":
    generate_reports()

elif choice == "ds":
    display_statistics()

elif choice == "e":
    print("Programme Terminated")
elif choice != "e" and choice != "vm" and choice != "va" and choice != "a" and choice != "r" and choice != "e": 
        print("Your selection is invalid, please try again: ")  #if they didn't enter any of the letters displayed
                                                                #in the menu option it will give an error