f = open("UD.txt","r+") #opening the file

if f.mode == 'r+': 
    contents = f.readlines()
    
login_list = []
for line in contents:
    if line[0:4] == "USER":
        continue
    login_list.append(line)
    n = 0
    while n < len(login_list):
        if "\n" in login_list[n]:
            login_list[n] = (login_list[n]).strip()
        n += 1
print(login_list)

login_list2 = []
for entry in login_list:
    login_list2.append((entry.split(",")))

for x in range(len(login_list2)):
    print(login_list2[x], end = "\n")



class Student:
    def __init__(self):
        self.__Username = ""
        self.__Courses = []
    def addCourse(self, CourseName):
        self.add = CourseName
        self.__Courses.append(self.add)
    def dropCourse(self, CourseName):
        self.drop = CourseName
        self.__Courses.remove(self.drop)
    def getCourse(self):
        return self.__Courses
  



class Course:
    def __init__(self):
        self.__courseName = ""
        self.__students = []
    def addStudent(self, logged):
        self.addS = logged
        self.__students.append(self.addS)
    def dropStudent(self, logged):
        self.dropS = logged
        self.__students.remove(self.dropS)
    def getStudents(self):
        return self.__students
    def getNumber_of_students(self):
        return len(self.__students)



CS131 = Course()
CS132 = Course()
EE210 = Course()
EE310 = Course()
Math320 = Course()
Math220 = Course()

login_portal = True
logging_in = True
wrong_input = True
while login_portal == True:
    
    while logging_in == True:
        admin_portal = str(input("Press L to login or C to create a new user: "))
        admin_portal = admin_portal.upper()

    
        if admin_portal == "L":
            
            while wrong_input == True:
                decision = str(input("Did you mean to choose this? Yes or No? "))
                decision = decision.capitalize()
      
                if decision == "Yes":
                    wrong_input = False
                    pass
                elif decision == "No":
                    break
                else:
                    print("Please choose yes or no.")
                    break
        
            if wrong_input == False:
                username = str(input(("Please enter your username and hit enter: ")))

                z = 0
                if username in login_list2[z]:
                    password = str(input("Please enter your password and hit enter: "))
                    if password in login_list2[z]:
                        logging_in = False
                        logged = login_list2[z]
                        verified = print("You are logged in.")
                        break
                        
                        
                    else:
                        print("Wrong password.")
                        break
            
                while z < len(login_list2):
                    if username in login_list2[z]:
                        password = str(input("Please enter your password and hit enter: "))
                        if password in login_list2[z]:
                            logging_in = False
                            logged = login_list2[z]
                            verified = print("You are logged in.")
                            break
                            
                            
                        else:
                            print("Wrong password.")
                            break
                    else:
                        print("Searching...")
                        z += 1
                        if z == len(login_list2):
                            print("User not found.")
                            break
            
    
    
        if admin_portal == "C":
            wrong_input = True
            while wrong_input == True:
                decision = str(input("Did you mean to choose this? Yes or No? "))
                decision = decision.capitalize()
      
                if decision == "Yes":
                    wrong_input = False
                    pass
                elif decision == "No":
                    break
                else:
                    print("Please choose yes or no.")
                    break

            if wrong_input == False: 
                creating = True
                while creating == True:

                    identity = str(input("Please enter your first name, last name, and student ID number, with each followed by a space: "))

                    identity = identity.split(" ")
               
                    userID = []
                    userID.append(identity[0][0])
                    userID.append(identity[1][0:2])
                    userID.append(identity[2][0:3])
                    userID = ''.join(userID)
        
                    new_password = str(input("Please enter a password: "))
                    check = str(input("Please reenter your password: "))
                    if new_password != check:
                        print("Passwords did not match.")
                        break
                    else:
                        newUser = str(userID + "," + check)
                        f.mode = "a"
                        f.write("\n")
                        f.write(newUser)
                        f.close()
                        break
        
          
    person = Student()
    while logging_in == False:
        
        f2 = open("SI.txt", "a+")
        f2.read()
        f3 = open("CI.txt", "a+")
        f3.read()
        options = str(input(("Choose A, B, C, D, or E: ")))
        options = options.upper()

        if options == "A":
            check_size = True
            while check_size == True:
                
                print("The number of students in CS131: ", CS131.getNumber_of_students())
                print("The number of students in CS132: ", CS132.getNumber_of_students())
                print("The number of students in EE210: ", EE210.getNumber_of_students())
                print("The number of students in EE310: ", EE310.getNumber_of_students())
                print("The number of students in Math320: ", Math320.getNumber_of_students())
                print("The number of students in Math220: ", Math220.getNumber_of_students())
                break

        if options == "B":
            choosing = True
            while choosing == True:
                choice = input("Which course would you like to add? CS131, CS132, EE210, EE310, Math220, or Math320?: ")
                if choice == "CS131":
                    print("You have been added to CS131.")
                    person.addCourse(choice)
                    CS131.addStudent(logged)
                if choice == "CS132":
                    print("You have been added to CS132.")
                    person.addCourse(choice)
                    CS132.addStudent(logged)
                if choice == "EE210":
                    print("You have been added to EE210.")
                    person.addCourse(choice)
                    EE210.addStudent(logged)
                if choice == "EE310":
                    print("You have been added to EE310.")
                    person.addCourse(choice)
                    EE310.addStudent(logged)
                if choice == "Math320":
                    print("You have been added to Math320.")
                    person.addCourse(choice)
                    Math320.addStudent(logged)
                if choice == "Math220":
                    print("You have been added to Math220.")
                    person.addCourse(choice)
                    Math220.addStudent(logged)

                complete = input("Is this all you want to add? Yes or no: ")
                complete = complete.capitalize()
                if complete == "Yes":
                    choosing = False
                    break
                if complete == "No":
                    pass
                else:
                    print("Please choose yes or no.")
                    break

        if options == "C":
            dropping = True
            while dropping == True:
                drop_choice = input("Which course would you like to drop? CS131, CS132, EE210, EE310, Math220, or Math320?: ")
                if drop_choice == "CS131":
                    print("You dropped CS131.")
                    person.dropCourse(drop_choice)
                    CS131.dropStudent(logged)
                if drop_choice == "CS132":
                    print("You dropped CS132.")
                    person.dropCourse(drop_choice)
                    CS132.dropStudent(logged)
                if drop_choice == "EE210":
                    print("You dropped EE210.")
                    person.dropCourse(drop_choice)
                    EE210.dropStudent(logged)
                if drop_choice == "EE310":
                    print("You dropped EE310.")
                    person.dropCourse(drop_choice)
                    EE310.dropStudent(logged)
                if drop_choice == "Math320":
                    print("You dropped Math320.")
                    person.dropCourse(drop_choice)
                    Math320.dropStudent(logged)
                if drop_choice == "Math220":
                    print("You dropped Math220.")
                    person.dropCourse(drop_choice)
                    Math220.dropStudent(logged)

                complete = input("Is this all you want to drop? Yes or no: ")
                complete = complete.capitalize()
                if complete == "Yes":
                    choosing = False
                    break
                if complete == "No":
                    pass
                else:
                  print("Please choose yes or no.")
                  break

        if options == "D":
            
            print("You are in ", person.getCourse())
            
            
        if options == "E":
            
            print("Saving info...")
            f2.mode = "r+"
            f2.readlines()
            f2.write(str(person.getCourse()))
            f2.write("\n")
            f3.mode = "r+"
            
            f3.write(str(CS131.getStudents()))
            f3.write(str(CS132.getStudents()))
            f3.write(str(EE210.getStudents()))
            f3.write(str(EE310.getStudents()))
            f3.write(str(Math320.getStudents()))
            f3.write(str(Math220.getStudents()))
            f2.close()
            f3.close()
            print("Exiting.")
            break
    break