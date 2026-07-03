import TrainSchedules as ts 
#from TrainSchedules import TrainScheduleManager

manager = ts.TrainScheduleManager()
#t1 = Train(1, 'T10', 'Bahnof', 'Airport','7:00AM', '7:45AM')
print("1. Add a new train schedule")
print("2. Display all train schedules")
print("3. Search for a train using its train number")
print("4. Search trains based on source and destination stations")
print("5. Update the departure and arrival time of a train")
print("6. Delete a train schedule using the train number")
print("7. Exit")
cont = 'Yes'
while(cont.lower() == 'yes'):
    choice = int(input("Enter your choice:"))
    
    match choice:
        case 1:
            tNum = input('Enter train number: ')
            tName = input('Enter train name: ')
            tStart = input('Enter train source location: ')
            tDest = input('Enter train destination location: ')
            tDep = input('Enter train departure time: ')
            tArr = input('Enter train arrival time: ')
            t = ts.Train(tNum,tName, tStart, tDest, tDep, tArr)
            manager.add_train_schedule(t)
    
        case 2:
            manager.disp_train_schedule()
    
        case 3:
            num = input("Enter train number: ")
            manager.search_trainSchedule(num)
    
        case 4:
            source = input("Enter source of the train: ")
            destination = input("Enter destination of the train: ")
            manager.search_trainWithSrcDest(source, destination)
    
        case 5:
            num = input("Enter train number to be updated: ")
            manager.update_trainSchedule(num)
    
        case 6:
            num = input("Enter train number to be deleted: ")
            manager.delete_trainSchedule(num)

        case 7:
            break
            
        case _:
            print("Invalid choice")
    cont = input('Do you want to continue?(Enter Yes/No):\n')
print('Thank you!')