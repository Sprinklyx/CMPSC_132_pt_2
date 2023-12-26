class UserData:
  def __init__(self):
    self.__First = ""
    self.__Last = ""
    self.__User = ""
    self.__Pass = ""

  def getLast(self):
    return self.__Last
  
  def setLast(self, Last):
    self.__Last = Last

  def getUser(self):
    return self.__User

  def setUser(self, Username):
    self.__User = Username

  def getFirst(self):
    return self.__First

  def setFirst(self, First):
    self.__First = First

  def getPass(self):
    return self.__Pass
  
  def setPass(self, Password):
    self.__Pass = Password
  
  def getPrint(self):
    return self.__Print

  def setPrint(self, logins):
    self.__Print = logins

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



admin_portal = (str(input("Press A, B, C, E: ")))


user = UserData()

if admin_portal == "a" or admin_portal == "A":
    admin_portal = admin_portal.upper()
    
    last = str(input("Enter your last name: "))
    
    
    user.setLast(last)

    
    x = 0
    if last in login_list2[x]:
        user.setPass((login_list2[x][-1]))
                
        print(user.getPass())
      

    while x < len(login_list2):

        if last not in login_list2[x]:
            x += 1
        
            if last in login_list2[x]:
              user.setPass((login_list2[x][-1]))
                
              print(user.getPass())

            if last not in login_list2:
                print("User not found.")
            

if admin_portal == "b" or admin_portal == "B": 
    admin_portal = admin_portal.upper()

    username = str(input("Enter your username: "))

    user.setUser(username)

    
    z = 0
    if username in login_list2[z]:
        user.setPass((login_list2[z][-1]))
                
        print(user.getPass())

    while z < len(login_list2):
        

        if username not in login_list2[z]:
            z += 1
            
            if username in login_list2[z]:
              user.setPass((login_list2[z][-1]))
                
              print(user.getPass())

            if username not in login_list2:
                print("User not found.")


if admin_portal == "c" or admin_portal == "C":
    admin_portal = admin_portal.upper()

    new_user = str(input("Enter first name, last name, username, and password: "))

    f.write((new_user))
    f.close()


if admin_portal == "e" or admin_portal == "E":
    admin_portal = admin_portal.upper()

    user.setPrint(login_list2)
    print(user.getPrint())