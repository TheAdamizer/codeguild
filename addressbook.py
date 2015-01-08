__author__ = 'Adam and Billy'

print "Hey there, this is an address book!"
print "What do you want to do?"
print "1 = Show contacts"
print "2 = Add Contact"
print "3 = Edit Contact"
print "4 = Delete Contact"
print "5 = quit"
print "--------------------------------"
choice = raw_input("Pick one, dummy!")

firstNameDict = {}
lastNameDict = {}
phoneDict = {}
phone2Dict = {}
emailDict = {}
addressDict = {}
keyList = []
currentKey = 0

def showContacts():
    for i in keyList:
        print "This is key: %d" % i
        print (firstNameDict[i])
        print (lastNameDict[i])
        print (phoneDict[i])
        print (phone2Dict[i])
        print (emailDict[i])
        print (addressDict[i])
        print "--------------------"
        print ""

def addContact(currentKey):
    editContact(currentKey)
    keyList.append(currentKey)
    currentKey = currentKey + 1
    return currentKey

def deleteContact(currentKey):
    firstNameDict.pop(currentKey)
    lastNameDict.pop(currentKey)
    phoneDict.pop(currentKey)
    phone2Dict.pop(currentKey)
    emailDict.pop(currentKey)
    addressDict.pop(currentKey)
    keyList.remove(currentKey)

def editContact(currentKey):
    firstName = ""
    lastName = ""
    phone = ""
    phone2 = ""
    email = ""
    address = ""
    while firstName == "":
        firstName = raw_input("Whats the first name of your contact? ")
    while lastName == "":
        lastName = raw_input("Whats the last name of your contact? ")
    while phone == "":
        phone = raw_input("Whats the phone of your contact? ")
    phone2 = raw_input("What is the second phone number of your contact?")
    while email == "":
        email = raw_input("Whats the email of your contact? ")
    while address == "":
        address = raw_input("Whats the address of your contact? ")

    firstNameDict[currentKey] = firstName
    lastNameDict[currentKey] = lastName
    phoneDict[currentKey] = phone
    emailDict[currentKey] = email
    addressDict[currentKey] = address
    phone2Dict[currentKey] = phone2

"""  #This is for testing stuff!!!
showContacts()
currentKey = addContact(currentKey)
currentKey = addContact(currentKey)
showContacts()
editContact(1)
showContacts()
deleteContact(1)
showContacts()
"""




print choice

wait = raw_input("You've chosen to quit.  Bye!")
