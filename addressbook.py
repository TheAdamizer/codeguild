__author__ = 'Adam and Billy'




# Here we are initializing the storage dictionaries, the key list, and the global
# variable currentKey.  currentKey is iterated every time the program creates a new entry
# in the storage dictionaries, so that way we always know that the key is unique.
# When these entries are created, the keys are stored into the list keyList.
firstNameDict = {}
lastNameDict = {}
phoneDict = {}
phone2Dict = {}
emailDict = {}
addressDict = {}
keyList = []
currentKey = 0

# This method is called whenever the user wants to view the contents of the address
# book.  It iterates through every entry in the list keyList.  It then prints the
# corresponding value for the key in every one of the storage dictionaries.
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

# This method is called when the user wants to create a new entry.  It needs
# to be passed a key at which the new entry needs to be created.  We will
# pass it the global variable currentKey whenever we need a new entry created.
# Notice this method calls the editContact method, which also needs a key
# and is used to let the user modify the entry.  The rest of the addContact
# method simply adds the new key to the keyList, iterates the currentKey
# (so the key stays unique), and returns the currentKey.
def addContact(currentKey):
    editContact(currentKey)
    keyList.append(currentKey)
# This method is used to completely remove an entry from the the address book.
# This is done by, first, popping the entries out of every storage dictionary,
# by passing the key for the entry we'd like to remove.  Then, the key is removed from
# the keyList.
def deleteContact(currentKey):
    firstNameDict.pop(currentKey)
    lastNameDict.pop(currentKey)
    phoneDict.pop(currentKey)
    phone2Dict.pop(currentKey)
    emailDict.pop(currentKey)
    addressDict.pop(currentKey)
    keyList.remove(currentKey)
    print "------------------------------------------------------"

# This method is used for editing the data in the storage dictionaries. It needs
# to be passed the key at which the entry is being edited/created (this method works for
# both) It creates some
# local variables, and initially makes them all blank.  Later on, the program asks the user
# for an entry for each of these.  These raw_input requests all happen within while loops that
# continue looping until their values are not empty (meaning the user put something in).  The
# exception to this is the phone2 value, letting the user keep that blank if they would like.
# After all the values (other than phone2) have non-blank values, it enters them into the
# storage dictionaries, using the key that was passed into the method. This method doesn't
# need to edit the keyList, because it only enters into the dictionaries, which could be used
# for editing the entry in place as well.
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

    # Notice phone2 is not contained within the while loop, so the program will accept
    # a blank value.
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

    print "---------------------------------"

# This loops forever until a break is encountered (meaning the user has chosen to quit with option 5)
while True:
    # This is for interfacing with the hooman allowing them to choose which of the program's
    # features they would like to use.  A menu is printed and the user's choice is stored into
    # the variable choice, presumably an integer, though no error checking is done.
    print "Hey there, this is an address book!"
    print "What do you want to do?"
    print "1 = Show contacts"
    print "2 = Add Contact"
    print "3 = Edit Contact"
    print "4 = Delete Contact"
    print "5 = quit"
    print "--------------------------------"
    choice = raw_input("Pick one, dummy!  ")
    print "--------------------------------"
    print ""

    # This is the decision tree we use to comply with the user's wishes.  The user has chosen what the
    # would like to do, so we uses a series of ifs and elifs to perform those commands that the user has
    # chosen.  If the user chooses to add a contact, the program incrememnts the global variable currentKey,
    # to make sure the currentKey stays unique no matter what.  If the user doesn't choose a given choice,
    # (not 1 through 5), then the program taunts them and repeats the menu.
    if choice == '1':
        showContacts()
    elif choice == '2':
        addContact(currentKey)
        currentKey = currentKey + 1
    elif choice == '3':
        keyToEdit = int(raw_input("Which key do you want to edit?  "))
        editContact(keyToEdit)
    elif choice == '4':
        keyToDelete = int(raw_input("Which key do you want to delete?  "))
        deleteContact(keyToDelete)
    elif choice == '5':
        break
    else:
        print "You messed, dude.  Try again (at life)."





# This is commented out code that is used for testing the functionality of the program.
# The program currently lacks any way for the user to choose how it functions, so this bit
# can be uncommented to ensure that the methods are working so far.
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



# This is printing the choice the user made at the start of the program, though we're
# not actually using it for anything yet, it is just being printed for debug purposes.
# print choice

# This is here to make sure the program closes when the user is good and ready
# for it to close, dammit!
# wait = raw_input("You've chosen to quit.  Bye!")
