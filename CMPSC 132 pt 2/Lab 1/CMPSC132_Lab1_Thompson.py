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

#print(login_list)



login = (str(input("Login or create a new user? Press 'L' to login, press 'C' to create a new user: ")))

if login == "l" or login == "L":
    login = login.upper()

    username_password = str(input("Enter your username and password (with a comma in between), then hit enter: "))
    
    entry = str(username_password)
    

    if entry in login_list:
        print("Welcome back.")

    if entry not in login_list:
        print("User not found.")
        
        
        
   
if login == 'c' or login == 'C':
    new_login = False
    login = login.upper()
    first_name = str(input("Please enter your first name: "))
    if first_name.isalpha() == False:
        print("Error. Please try again.")

    last_name = str(input("Please enter your last name: "))
    if last_name.isalpha() == False:
        print("Error. Please try again.")

    student_ID = str(input("Please enter your student ID number: "))
    if student_ID.isnumeric() == False:
        print("Error. Please try again.")

    userID = first_name[0] + last_name[:2] + str(student_ID[:3])

    new_password = input("Please enter a new password (no special characters): ")
    if new_password.isalnum() == False:
        print("Invalid password. Please try again.")
    
    else:
        verify = input("Please re-enter your password: ")
        if verify != new_password:
            print("Passwords do not match. Please try again.")
            
        else:
            print("New login created.")
            new_login = True
    
    if new_login == True:
        f.write((userID, str(verify)))
        f.close()
        print("Please login.")
    



    

