from tasktracker import TaskTracker

if __name__=='__main__':
    tt=TaskTracker()
    tt.load_from_file()

    while True:
        print(f'       Welcome to the TaskManager')
        print(f'1.Add Task \n2.Remove Task \n3.Mark done any task \n4.All Tasks\n5.To exit')
        command=int(input("Select the option : "))
        print()
        if command==1:
            title=input("Enter the Title of the Task : ")
            desc=input("Enter description for the Task(optional) : ")
            prio=input("Enter priority of the Task (high/medium/low) : ").lower()
            due_date=input("Enter due date of the task (format :(yyyy-mm-dd)) : ")
            result=tt.add_task(title,desc,prio,due_date)
            tt.save_to_file()
            if result is True:
                print(f"Task '{title}' added successfully!")


        elif command==2:
            tt.list_tasks()
            idx=int(input('Enter Task no to Remove it : '))
            result=tt.remove_task(idx)
            tt.save_to_file()
            if result is True:
                print("Removed Successfully")
            else:
                print(f"something went wrong.May be {idx} not in the tasks")

        elif command==3:
            tt.list_tasks()
            idx=int(input('Enter Task No to Mark as done : '))
            result=tt.mark_done(idx)
            tt.save_to_file()
            if result is True:
                print(f"Task {idx} is marked as done ")
            else:
                print(f'Task {idx} is not the tasks')

        elif command==4:
            sort_by=int(input("Do you want to sort by 1.priority or 2.due_date (default :'priority') : "))
            if sort_by not in [1,2]:
                print("Enter only 1 or 2 ")
                continue
            if sort_by==2:
                sort_by='due_date'
            tt.list_tasks(sort_by)

        elif command==5:
            print("Thanks for visiting ")
            break
