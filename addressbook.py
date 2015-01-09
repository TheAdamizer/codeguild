__author__ = 'Adam and Billy'


# Here we are initializing the storage dictionaries, and the key list.
first_name_dict = {}
last_name_dict = {}
phone_dict = {}
phone_2_dict = {}
email_dict = {}
address_dict = {}
key_list = []


# I added an optional argument to this method now, so if you call the method and pass it a list (of keys)
# it will now print the contacts with keys in that list.  Otherwise, it will print all the entries.
def show_contacts(list = key_list):
    for i in list:
        show_contact(i)


# This method actually prints the contents of a contact entry.
def show_contact(i):
    print "This is key: %d" % i
    print (first_name_dict[i])
    print (last_name_dict[i])
    print (phone_dict[i])
    print (phone_2_dict[i])
    print (email_dict[i])
    print (address_dict[i])
    print "--------------------"
    print ""


# This method is called when the user wants to create a new entry.  It needs
# to be passed a key at which the new entry needs to be created.  We will
# pass it the global variable currentKey whenever we need a new entry created.
# Notice this method calls the editContact method, which also needs a key
# and is used to let the user modify the entry.  The rest of the addContact
# method simply adds the new key to the keyList, iterates the currentKey
# (so the key stays unique), and returns the currentKey.
def add_contact(current_key):
    edit_contact(current_key)
    key_list.append(current_key)


# This method is used to completely remove an entry from the the address book.
# This is done by, first, popping the entries out of every storage dictionary,
# by passing the key for the entry we'd like to remove.  Then, the key is removed from
# the keyList.
def delete_contact(current_key):
    first_name_dict.pop(current_key)
    last_name_dict.pop(current_key)
    phone_dict.pop(current_key)
    phone_2_dict.pop(current_key)
    email_dict.pop(current_key)
    address_dict.pop(current_key)
    key_list.remove(current_key)
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
def edit_contact(key_to_edit):
    first_name = ""
    last_name = ""
    phone = ""
    phone2 = ""
    email = ""
    address = ""
    while first_name == "":
        first_name = raw_input("What is the first name of your contact? ")
    while last_name == "":
        last_name = raw_input("What is the last name of your contact? ")
    while phone == "":
        phone = raw_input("What is the phone of your contact? ")

    # Notice phone2 is not contained within the while loop, so the program will accept
    # a blank value.
    phone2 = raw_input("What is the second phone number of your contact? ")
    while email == "":
        email = raw_input("What is the email of your contact? ")
    while address == "":
        address = raw_input("What is the address of your contact? ")

    first_name_dict[key_to_edit] = first_name
    last_name_dict[key_to_edit] = last_name
    phone_dict[key_to_edit] = phone
    email_dict[key_to_edit] = email
    address_dict[key_to_edit] = address
    phone_2_dict[key_to_edit] = phone2

    print "---------------------------------"


# This method, when given a string, searches the entries in all the databases for that string.
# It will return a list of all of the keys for entries that contain that string.
def phrase_search(phrase):
    search_results = []
    for i in key_list:
        if first_name_dict[i].__contains__(phrase) or last_name_dict[i].__contains__(phrase) or phone_dict[i].__contains__(phrase) or email_dict[i].__contains__(phrase) or address_dict[i].__contains__(phrase) or phone_2_dict[i].__contains__(phrase):
            search_results.append(i)
    return search_results


# This method manages the user's search. It initially asks for a phrase and keeps searching
# until the search yields results or the user decides to stop trying.
def search():
    search_phrase = raw_input("Enter a phrase to search. ")
    success = 0                                  # This variable is used to keep track of when the program should stop trying to search.
    while success == 0:                          # As long as no success is seen, the search continues...
        results = phrase_search(search_phrase)   # Calling the phrase_search method defined above.
        if results:
            show_contacts(results)
            success = 1
        else:
            choice = raw_input("No results... enter y to search again, and anything else otherwise. ")
            if choice == 'y':                    # If user decides to search again, new input is taken.
                search_phrase = raw_input("Enter a phrase to search. ")
            else:
                success = 1                      # Otherwise 1 is assigned to success and this ends the search loop.


# This method is used to take one line, read from the storage file, and parse it into a list
# of values for the dictionary.  It uses multiple try blocks to insure that the information is valid,
# and will not write to the dictionaries if it is not.
def read_line_to_dicts(line,key_so_far):
    items = line.split('|')
    print "Opening line..."
    try:                 # Making sure the key is a valid integer.
        key = int(items[0])
    except:              # If not, return the key given and report the error.
        print "Not a valid line: No valid Key. Nothing imported."
        return key_so_far
    print "Valid key number %d" % key
    try:                        # Making sure the item list is at least 6 long (contains all but a phone2)
        address_dict[key] = items[5].rstrip('\n')
        first_name_dict[key] = items[1]
        last_name_dict[key] = items[2]
        phone_dict[key] = items[3]
        email_dict[key] = items[4]
    except:                      # If the line doesn't have enough parameters, report error. Nothing will be imported.
        print "Not a valid line: Not enough parameters/Not formatted correctly. Nothing imported."
        return key_so_far
    try:                         # If the last entry (for phone2) is empty....
        phone_2_dict[key] = items[6].rstrip('\n')
    except:                      # Don't worry about it, and fill with a blank. Keep going.
        phone_2_dict[key] = ''
        pass
    print "Line is a valid entry! Entry %d successfully imported" % key
    key_list.append(key)         # Add the key to the keylist
    new_current_key = key + 1    # Increment the key to make sure it stays unique.
    return new_current_key


# This method tries to open the given file, manages all exceptions, and parses
# the file into lines.  It sends each line to the read_line_to_dicts method.  It
# closes the file when it is done, and it keeps track of the next usable key, by
# setting it to 1 plus the highest key read from a file. It returns this key when it
# is done to be stored into the current_key variable.
def read_lines_from_file(filename):
    highest_key = 0
    try:
        file_to_open = open(filename, 'r')
        print "File %s successfully opened!" % filename
    except:
        print "No valid file! Nothing imported. Sad day..."
        print "The current usable key after importing is %d." % highest_key
        wait = raw_input("Press enter to continue.")
        return highest_key
    for l in file_to_open:
        highest_key = read_line_to_dicts(l, highest_key)
    file_to_open.close()
    print "The current usable key after importing is %d." % highest_key
    wait = raw_input("Press enter to continue.")
    return highest_key


# This function reads through the entire key list and writes all of the values associated
# with that key into a line of a file that is defined in the argument.
# The values are seperated by a | character, and they are put in in an order that allows
# us to reliably retrieve them the next time the program is run.
def write_dicts_to_file(filename):
    file_to_write = open(filename, 'w')
    for key in key_list:
        file_to_write.write(str(key) + '|')
        file_to_write.write(first_name_dict[key] + '|')
        file_to_write.write(last_name_dict[key] + '|')
        file_to_write.write(phone_dict[key] + '|')
        file_to_write.write(email_dict[key] + '|')
        file_to_write.write(address_dict[key] + '|')
        file_to_write.write(phone_2_dict[key] + '|\n')
    file_to_write.close()


current_key = read_lines_from_file('book_file')
print "\nprint Hey there, this is an address book!\n\n"


# This loops forever until a break is encountered (meaning the user has chosen to quit with option 5)
# This way the user will always be presented with the menu after the program is done completing a request.
while True:
    # This is for interfacing with the hooman allowing them to choose which of the program's
    # features they would like to use.  A menu is printed and the user's choice is stored into
    # the variable choice, presumably an integer, though no error checking is done.
    print "What do you want to do?"
    print "1 = Show contacts"
    print "2 = Add Contact"
    print "3 = Edit Contact"
    print "4 = Delete Contact"
    print "5 = Search for contact"
    print "6 = Quit"
    print "--------------------------------"
    choice = raw_input("Pick one, dummy!  ")
    print "--------------------------------"
    print ""

    # This is the decision tree we use to comply with the user's wishes.  The user has chosen what the
    # would like to do, so we uses a series of ifs and elifs to perform those commands that the user has
    # chosen.  If the user chooses to add a contact, the program increments the global variable currentKey,
    # to make sure the currentKey stays unique no matter what.  If the user doesn't choose a given choice,
    # (not 1 through 5), then the program taunts them and repeats the menu.
    if choice == '1':
        show_contacts()
    elif choice == '2':
        add_contact(current_key)
        current_key = current_key + 1
    elif choice == '3':
		success = 0			 # Here I am making a sub-loop that continues asking the user for a key to edit
		while success == 0 : # Until the user gives a valid key that is used in the first_name_dict
			key_to_edit = int(raw_input("Which key do you want to edit?  "))
			if first_name_dict.has_key(key_to_edit):
				edit_contact(key_to_edit)
				success = 1
			else:			 # Otherwise it prints an error and repeats the loop.
				print "This isn't a valid key, m8.  Please try again."
    elif choice == '4':
		success = 0
		while success == 0:	 # Using the same technique as above
			key_to_delete = int(raw_input("Which key do you want to delete?  "))
			if first_name_dict.has_key(key_to_delete):
				delete_contact(key_to_delete)
				success = 1
			else:
				print "This isn't a valid key, m8.  Please try again."
        
    elif choice == '5':
	    search()
    elif choice == '6':
        write_dicts_to_file('book_file')
        break
    else:
        print "You messed, dude.  Try again (at life).\n"





# This is commented out code that is used for testing the functionality of the program.
# The program currently lacks any way for the user to choose how it functions, so this bit
# can be uncommented to ensure that the methods are working so far.
"""  #This is for testing stuff!!!
show_contacts()
current_key = add_contact(currentKey)
current_key = add_contact(currentKey)
show_contacts()
edit_contact(1)
show_contacts()
delete_contact(1)
show_contacts()
"""



# This is printing the choice the user made at the start of the program, though we're
# not actually using it for anything yet, it is just being printed for debug purposes.
# print choice

# This is here to make sure the program closes when the user is good and ready
# for it to close, dammit!
# wait = raw_input("You've chosen to quit.  Bye!")
