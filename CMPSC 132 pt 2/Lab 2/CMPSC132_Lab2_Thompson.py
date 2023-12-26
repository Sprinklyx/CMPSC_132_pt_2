f = open("UD.txt","r+") #opening the file

if f.mode == 'r+': 
    contents = f.readlines()
    
login_list = []
for line in contents:
    if line[0:5] == "FIRST":
        continue
    login_list.append(line)
    n = 0
    while n < len(login_list):
        if "\n" in login_list[n]:
            login_list[n] = (login_list[n]).strip()
        n += 1
    

login_list2 = []
for string in login_list:
    login_list2.append((string.split(",")))
print(login_list2)


admin_portal = (str(input("Press A, B, C, D, E, or F: ")))


if admin_portal == "a" or admin_portal == "A":
    admin_portal = admin_portal.upper()
    
    last = str(input("Enter your last name: "))
    
    x = 0
    if last in login_list2[x]:
            print(login_list2[x])

    while x < len(login_list2):

        if last not in login_list2[x]:
            x += 1
        
            if last in login_list2[x]:
                print(login_list2[x])

            if last not in login_list2:
                print("User not found.")


if admin_portal == "b" or admin_portal == "B":
    admin_portal = admin_portal.upper()

    first = str(input("Enter your first name: ")) 
    
    y = 0
    if first in login_list2[y]:
            print(login_list2[y])

    while y < len(login_list2):

        if first not in login_list2[y]:
            y += 1
            
            if first in login_list2[y]:
                print(login_list2[y])

            if first not in login_list2:
                print("User not found.")


if admin_portal == "c" or admin_portal == "C": 
    admin_portal = admin_portal.upper()

    username = str(input("Enter your username: "))

    z = 0
    if username in login_list2[z]:
            print(login_list2[z])

    while z < len(login_list2):
        

        if username not in login_list2[z]:
            z += 1
            
            if username in login_list2[z]:
                print(login_list2[z])

            if username not in login_list2:
                print("User not found.")


if admin_portal == "d" or admin_portal == "D":
    admin_portal = admin_portal.upper()

    def output():
        login_list2.sort()
        print(login_list2)
        
    output()


if admin_portal == "e" or admin_portal == "E":
        admin_portal = admin_portal.upper()

        def output():          

            def takeSecond(elem):
                return elem[1]
            login_list2.sort(key=takeSecond)
            print(login_list2)

                
        output()


if admin_portal == "f" or admin_portal == "F":  
    admin_portal = admin_portal.upper()
    
    new_user = str(input("Enter first name, last name, username, and password: "))

    f.write((new_user)) 
    f.close()
  