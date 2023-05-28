# this program is used to keep track of tasks I need to complete
from tasks import Task
from emailer import Emailer
# TODO implement argparse

# function used to check the response from the user to make sure it is a valid response
def check_response(response):
    iter = True
    response_list = ['Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no']
    while iter:
        for i in response_list:
            if response == i:   # if valid response, ends loop and returns response
                iter = False
                return response
        response = input("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response
        
# function used to check if user wants to email task list to themselves or other people
def email_list(response, task):
    check_response(response)    # checks the response to make sure it is valid
    if response == 'Y' or response == 'y' or response == 'Yes' or response == 'yes':
        sender_email = input("\nPlease provide the sender gmail address ( ex. sender@gmail.com ): ") # take the users email address
        app_password = input("Please provide your gmail app password: ")    # take the users gmail app password
        reciever_email = input("Please provide the recievers email address ( ex. reciever@mail.com ): ") # take the email they wish to send the task to
        Emailer(sender_email, app_password, reciever_email, task)   # pass the variables into the Emailer class
    else:
       print("Task list will not be emailed")   # if the user picks No, tell the user the list will not be emailed

# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
    # empty list for task info
    task_info = []
      
    task_name = input("\nEnter the task name: ") # get task name from user
    task_info.append(task_name) # append task name to task_info list

    task_completion_status = input("Enter the task completion status ( Y | N ): ") # get task completion status from user
    checked_completion_status = check_response(task_completion_status)  # check for valid response
    task_info.append(checked_completion_status) # append response to task_info list

    task_reminder_status = input("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    checked_reminder_status = check_response(task_reminder_status)  # check for valid response
    task_info.append(checked_reminder_status)   # append response to task_info list

    task_priority = input("Enter the priority of this task ( 0, 1, 2 ): ")  # get task priority from the user
    task_info.append(task_priority) # append the task priority to task_info list

    task_comment = input ("Enter a comment for this task: ") # get task comment from user
    task_info.append(task_comment)  # append task comment to task_info list

    return task_info    # return task_info

# passes task_info list variables into the Task class, then returns the task object
def set_task(task_info):
    task = Task(task_info[0], task_info[1], task_info[2], int(task_info[3]), task_info[4]) # split task_info list into multiple variables and insert into Task class

    return task # return the task object

def print_task(tasks):
    print('\n')
    for i in tasks:
        print(i)
    

def main():
    tasks = [] # empty list for task objects to be appended to
    iter = True
    while iter:

        task_info = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        task = set_task(task_info) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable

        tasks.append(task) # appending the task object with the user provided data

        print_task(tasks) # prints the tasks

        # Ask user if they would like to add another task, if not ask if they would like to email the list
        answer = input("\nWould you like to enter another task ( Y | N ): ")
        check_response(answer) # check for valid response
        
        # checks user response to if they wish to continue, if yes loop will continue otherwise user will be asked if they would like to email their list
        # and loop will end
        if answer == 'Y' or answer == 'y' or answer == 'Yes' or answer == 'yes':
            continue
        else:
            iter = False
            response = input("\nWould you like to email your task list ( Y | N ): ") # prompts user asking if they would like to email their task list
            email_list(response, task) # checks response and sends on doesn't send email based on the response
 

# TODO list of tasks, save user infomation on cloud or locale?, allow user to send task list to email or export as txt
if __name__ == '__main__':
    main()