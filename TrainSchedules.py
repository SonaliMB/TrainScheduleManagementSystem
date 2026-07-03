class Train:
    def __init__(self, number, name, source, dest, depTime, arrTime):
        self.num = number
        self.n = name
        self.src = source
        self.destn = dest
        self.depT = depTime
        self.arrT = arrTime

    def __str__(self):
        return (f'{self.num},{self.n},{self.src},{self.destn},{self.depT},{self.arrT}')
    

class TrainScheduleManager:
    def __init__(self, filename="trains.txt"):
        self.filename = filename
    
    def add_train_schedule(self,train):
        with open(self.filename,'a') as file:
            file.write(str(train))
        print("Train schedule added successfully.")
            
    def disp_train_schedule(self):
        try:
            with open(self.filename, 'r') as file:
                contents = file.readlines()        
            for content in contents:
                print(content)
        except FileNotFoundError:
            print('File does not exist! First add train schedule using option 1.')
    def search_trainSchedule(self,num):
        found = False
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    content = line.strip().split(',')
                    if content[0] == num:
                        found = True
                        print(f"Train number: {content[0]}")
                        print(f"Train name: {content[1]}")
                        print(f"Train source: {content[2]}")
                        print(f"Train destination: {content[3]}")
                        print(f"Train departure time: {content[4]}")
                        print(f"Train arrival time: {content[5]}")
                if found != True:
                    print('Train schedule not found for the entered number!')
        except FileNotFoundError:
            print('File does not exist! First add train schedule using option 1.jhn')

    def search_trainWithSrcDest(self,src, dest):
        found = False
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    content = line.strip().split(',')
                    if ((content[2] == src) and (content[3] == dest)):
                        found = True
                        print(f"Train number: {content[0]}")
                        print(f"Train name: {content[1]}")
                        print(f"Train source: {content[2]}")
                        print(f"Train destination: {content[3]}")
                        print(f"Train departure time: {content[4]}")
                        print(f"Train arrival time: {content[5]}")
                if found != True:
                    print('Train schedule not found for the entered source and destination!')
        except FileNotFoundError:
            print('File does not exist! First add train schedule using option 1.jhn')

    def update_trainSchedule(self,num):
        self.depT = input("Enter updated departure time: ")
        self.arrT = input("Enter updated arrival time: ")
        found = False
        updatedLine = []
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    content = line.strip().split(',')
                    if (content[0] == num):
                        found = True
                        content[4] = self.depT
                        content[5] = self.arrT
                    updatedLine.append(f'{content[0]},{content[1]},{content[2]},{content[3]},{content[4]},{content[5]}\n')
                if found != True:
                    print('Train schedule not found for the entered train number!')        
            with open(self.filename, 'w') as file:
                file.writelines(updatedLine)
        except FileNotFoundError:
            print('File does not exist! First add train schedule using option 1.jhn')

    def delete_trainSchedule(self,num):
        found = None
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            with open(self.filename, 'w') as file:
                for line in lines:
                    content = line.strip().split(',')                
                    if (content[0] != num):
                        file.writelines(line)
                    else:
                        found = True
                        continue
                if found == None:
                    print('Train schedule not found for the entered number!')
                else:
                    print('Mentioned train details deleted!')
        except FileNotFoundError:
            print('File does not exist! First add train schedule using option 1.jhn')