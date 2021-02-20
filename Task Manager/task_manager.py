#This is a copy of the task 20 task_manager.py

user_file = open("user.txt", "r+")                                         # we open the text document
login = False

while login == False:
  username = input("Enter your username: ")								#We ask the user to enter the username and password  
  password = input("Enter your password: ") 							#that is in the text file, if the username and password
																		#don't match to the ones in the text file it will give an error
																		#and will keep ask the user to the correct username and password.
  
  
  for line in user_file:
    valid_user, valid_password = line.strip("\n").split(", ")
    
    if username == valid_user and password == valid_password:
      login = True
      
    if username != valid_user or password != valid_password:
        
      print("Access Denied! password or username is incorrect, try again: ")
  user_file.seek(0)


print("Please select one of the following options: ")					#Here we ask the user to select one of the following options in the menu.
print("r\t    -  register user\n")
print("a\t    -  add task\n")
print("va\t   -  view all tasks\n")
print("vm\t   -  view my tasks\n")
if username == "admin" and password == "adm1n":
  print("ds\t   - display statistics\n")

print("e\t    -  exit")
  
choice = input("Enter your selected choice: ")

credentials = False
if choice == "r" and username == "admin":                           #If the user is the adm1n they are able to register the user.
  while credentials == False:
    write_file = open("user.txt", "a+")
    new_user = input("Enter your created username: ")
    new_password = input("Enter your created password: ")
    confirm_password = input("Re-enter your created password: ")

    if new_password != confirm_password:						#If the passwords don't match it will give an error message, but if they do match
      credentials = False										#the username and the password and the username will be stored in the user text file 
      print("passwords don't match")
    write_file.seek(0)

    if new_password == confirm_password:
      credentials = True
      write_file.write(f"\n{new_user}, {new_password}")
      print("Your username and password have been updated")
      write_file.close()
if choice == "r" and username != "admin":					#If the user isn't the admin it will give an error to say that only the admin can
  print("only administrators can register users")			#register the user 

elif choice == "a":											#if the user selects 'a' they are able to add another task into the text document.
   tasks_file = open("tasks.txt", "a+")
   user = input("Enter the username of the person the task is assigned to: ")
   task = input("Enter the title of the task: ")
   description = input("Enter the description of the task: ")
   assigned_date = input("Enter the date the task was assigned: ")
   due_date = input("Enter the due date of the task: ")
   is_completed = input("Is the todo completed: ")

   tasks_file.write(f"\n{user}, {task}, {description}, {assigned_date}, {due_date}, {is_completed}")
   tasks_file.close()

elif choice == "va":										#If the user selects 'va' they will be able to view all of the tasks in read mode.
   with open("tasks.txt","r") as read_file:
     read_file_contents = read_file.readlines()
     print(read_file_contents)
   
elif choice == "vm":                                       #if the user select vm, it will open the text document of the task assigned to the user.
  mytasks_file = open("tasks.txt","r")

  for line in mytasks_file:
    user, task, description, assigned_date, due_date, is_completed = line.split(", ")
    if username == user:                                   #If the username matches the name of the user in the text file it will display the assignments
														   #assigned to the user.
      print(f'''										   
    User                  : {user}											
    Task title            : {task}
    Task description      : {description}
    Assigned date         : {assigned_date}
    Due date              : {due_date}
    Completion status     : {is_completed}
    ''')
  mytasks_file.close()  

elif choice == "ds":                                        #This will display the total number of tasks and the total number of users
    statistics = input("Do you want to see the statistics? (Yes/No): ")
    if statistics =="Yes" or statistics == "YES":
      number_of_lines = len(open("tasks.txt").readlines())
      number_of_users = len(open("user.txt").readlines())
      print("There are"+" "+str(number_of_lines)+" "+"tasks and"+" "+str(number_of_users)+" "+"users.")

elif choice == "e":										    #If the user select 'e' the program will be terminated.
  print("Programme terminated")

elif choice !="e" and choice !="vm" and choice !="va" and choice !="a" and choice != "r": #if they didn't enter any of the letters displayed
  print("Your selection is invalid")													  #in the menu option it will give an error
elif choice == "yes":
  print("statics")

elif choice == "no":
  print("Programme terminated")
  


  