import re
def InputCycle():
  global memberID
  global name
  global email
  global monthjoined
  memberID = input("Enter MEMBERID ")
  try:
    val = int(memberID)
  except ValueError:
    memberID = input("Invalid entry, enter MEMBERID again")
  name = input("Enter your Name ")
  x = any(char.isdigit() for char in name)
  if x == True:
    name = input("Re-enter name")
  email = input("Enter your email ")
  if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
      email = input("Enter your email again ")
  monthjoined = input("Enter the month joined in digits ")
  try:
    monthjoined < "13" 
  except ValueError:
    monthjoined = input("Invalid entry, enter month joined again")
  currentmonth = input("Enter the current month ")
  try:
    currentmonth < "13" 
  except ValueError:
    currentmonth = input("Invalid entry, enter current month again")
  if(monthjoined < currentmonth):
    return "TRUE"
  else:
    return "FALSE"
def looper():
  x = input("Enter EXIT to quit program, enter any other key to continue")
  if x == "EXIT":
    return
  else:
    InputCycle()
    FileEntry()
    looper()
membershipactive = InputCycle()    
def FileEntry():
 f = open("test.txt", 'a+')
 string = memberID + "," + name + "," + email + "," + monthjoined + "," + membershipactive
 f.write(string + "\n")
 f.close()
 print (string + " WAS WRITTEN") 
FileEntry()
looper()
