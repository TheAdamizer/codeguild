__author__ = 'Adam and Billy'

import sys


'''
The structure of the address book is as follows:
Each of the parameter dictionaries (ex: first_name_dict, email_dict, etc) stores
one entry detail on a contact.  The keys in every one of these dictionaries
is the shared key for a unique contact entry, meaning that every entry into the
contact book gets a unique key, and that key can be used to access any of the
entry details in the parameter dictionaries.

Every one of these dictionaries is stored into a parent list.  There
are 3 entries into this list, and order is important because the first two elements of the list
determine the function of that entry in the address book.  The first index of the list is a
'binary' value indicating whether the program should let that entry be blank.  Normally, the
only entry that is allowed blank is "Phone 2", though user created entries can either be
allowed blank or not.  Entries that can be blank will be indicated with a 1 value.
The second entry, another binary value, determines whether the entry is user-created or not.  If it
is user created, the value will be 1.

These parameter lists are stored into a dictionary called called book_dict.
In this dictionary, the key for every parameter list is a textual
representation of that parameter list's contents.  For example,the list containing first_name_dict, as
it is originally instantiated, will be put in the the book_dict under the key 'First Name',
last_name_dict's parameter list will be stored as 'Last Name', email_dict's parameter list as
'Email Address', and so on.

In this new dictionary, book_dict, the entire address book has been packaged into one object
that can be passed around to different functions and accessed directly.  One would note that
creating dictionaries with the names first_name_dict, phone_dict, etc. is completely unnecessary,
and that I would only need one line to create the book_dict with its keyed parameter lists.
This project is being created as an educational experience, and as such the creation of the book_dict
object has been expanded to provide some insight into it's structure and how it will be used by methods
later on in the address book program.
'''


def create_book():
    first_name_dict = {}
    last_name_dict = {}
    phone_dict = {}
    phone_2_dict = {}
    email_dict = {}
    address_dict = {}
    book_dict = {'First Name': [0, 0, first_name_dict],
                 'Last Name': [0, 0, last_name_dict],
                 'Phone Number': [0, 0, phone_dict],
                 'Phone 2': [1, 0, phone_2_dict],
                 'Email Address': [0, 0, email_dict],
                 'Physical Address': [0, 0, address_dict]}
    return book_dict


'''
When adding a new entry into the list, the program needs a way to determine the next available key
to use for an entry.  Since the program supports deleting entries, those keys open up, and for the sake of
tidiness, this method will prefer lower entries.  It iterates from 0 and finds the next available key.
'''


def get_available_key(book_dict):
    for possible_key in range(book_dict['First Name'][2].__len__()):
        if possible_key not in book_dict['First Name'][2].keys():
            return possible_key
    return book_dict['First Name'][2].__len__()


# This simple function acts as an alias to retrieve the key list.  Cause I'm lazy.
def get_key_list(book_dict):
    return book_dict['First Name'][2].keys()


# I added an optional argument to this method now, so if you call the method and pass it a list (of keys)
# it will now print the contacts with keys in that list. Otherwise, it will print all the entries.
def show_contacts(book_dict, show_list='not a list'):
    if isinstance(show_list, list):
        for i in show_list:
            show_contact(book_dict, i)
    elif isinstance(show_list, str):
        for i in get_key_list(book_dict):
            show_contact(book_dict, i)
    else:
        print "I do not understand the input and I won't respond to it."


# This method actually prints the contents of a contact entry.
def show_contact(book_dict, i):
    print "This entry is key: %d" % i
    for column_name in book_dict.keys():
        print "%s: %s" % (column_name, book_dict[column_name][2][i])
    print "--------------------\n"


# This method is called when the user wants to create a new contact  It needs
# to be passed the book_dict in which the new entry needs to be created.
def add_contact(book_dict):
    key_to_add = get_available_key(book_dict)
    print "\nThis contact will have key number: %d\n" % key_to_add
    print "Please enter the requested information about your new contact."
    for column_name in book_dict.keys():
        print "%s: " % column_name
        user_input = raw_input("")
        if book_dict[column_name][0] == 0:
            while user_input == '':
                print 'This value cannot be blank. Please reenter.'
                print "%s: " % column_name
                user_input = raw_input("")
        book_dict[column_name][2][key_to_add] = user_input
    return book_dict


# This method is used to completely remove an entry from the the address book.
# This is done by, first, popping the entries out of every storage dictionary,
# by passing the key for the entry we'd like to remove.
def delete_contact(book_dict, delete_key):
    print "Contact has been marked for deletion!!!!!!"
    show_contact(book_dict, delete_key)
    user_input = raw_input("Type Y if you're sure you want to delete !!")
    if user_input == 'Y':
        for column_name in book_dict.keys():
            book_dict[column_name][2].pop(delete_key)
        return book_dict
    else:
        print "No changes made."
        return book_dict


# This method is used for editing the data in the storage dictionaries. It needs
# to be passed the key at which the entry is being edited.
# The program prints the current value at column_name for an entry, then asks the user for an entry.
# If the user doesn't want to change that part of the contact, they can simply hit enter and it will remain unchanged.
def edit_contact(book_dict, edit_key):
    print "Key you have chosen to edit: %d" % edit_key
    print "\nShowing current values, if you want to leave the entry, press enter.  Otherwise, the input will replace it"
    for column_name in book_dict.keys():
        print "%s: %s" % (column_name, book_dict[column_name][2][edit_key])
        user_input = raw_input("")
        if user_input != '':
            book_dict[column_name][2][edit_key] = user_input
            print "replaced with %s" % user_input
        else:
            print "nothing changed!"
    print "Done editing\n...................................."
    return book_dict


# This method, when given a string, searches the entries in all the databases for that string.
# It will return a list of all of the keys for entries that contain that string.
def phrase_search(book_dict, phrase):
    search_results = []
    for i in get_key_list(book_dict):
        for column_name in book_dict.keys():
            if book_dict[column_name][2][i].__contains__(phrase):
                search_results.append(i)
                break
    return search_results


# This method manages the user's search, given a book to search. It initially asks for a phrase and keeps searching
# until the search yields results or the user decides to stop trying.
# noinspection PyTypeChecker
def search(book_dict):
    search_phrase = raw_input("Enter a phrase to search. ")
    search_success = 0          # This variable is used to keep track of when the program should stop trying to search.
    while search_success == 0:                          # As long as no success is seen, the search continues...
        results = phrase_search(book_dict, search_phrase)   # Calling the phrase_search method defined above.
        if results:
            show_contacts(book_dict, results)
            search_success = 1
        else:
            user_choice = raw_input("No results... enter y to search again, and anything else otherwise. ")
            if user_choice == 'y':                    # If user decides to search again, new input is taken.
                search_phrase = raw_input("Enter a phrase to search. ")
            else:
                search_success = 1    # Otherwise 1 is assigned to success and this ends the search loop.


# This method is used to take one line, read from the storage file, and parses it into a list
# of values for the dictionary.  It uses multiple try blocks to insure that the information is valid,
# and will not write to the dictionaries if it is not.
def read_line_to_dicts(book_dict, column_list, line):
    items = line.split('|')
    try:                        # Making sure the key is a valid integer.
        key = int(items[0])
    except ValueError:          # If not, return the key given and report the error.
        print "Not valid Key. Nothing imported."
        return book_dict
    except:
        print "Unexpected Error: ", sys.exc_info()[0]
        raise
    print "Valid key number %d" % key
    try:                        # Making sure the item list is as long as the column_list's length.
        last_term = line[column_list.__len__()-1]
        term_to_read = 1
        for column_name in column_list:
            book_dict[column_name][2][key] = items[term_to_read].rstrip('\n')
            term_to_read += 1
    except IndexError:          # If the line doesn't have enough parameters, report error. Nothing will be imported.
        print "Not a valid line: Not enough parameters/Not formatted correctly. Nothing imported."
        return book_dict
    except:
        print "Unexpected Error: ", sys.exc_info()[0]
        raise
    print "Line is a valid entry! Entry %d successfully imported" % key
    return book_dict


# This method is used to read the first line of the file.  The first line is important because it defines
# the structure of the address book.
def read_first_line(first_line):
    broken_line = first_line.split('|')
    ordered_parameter_list = []
    new_book_dict = dict()
    try:
        for i in range(broken_line.__len__()):
            broken_column = broken_line[i].split(',')
            new_parameter_list = [int(broken_column[0]), int(broken_column[1]), dict()]
            ordered_parameter_list.append(broken_column[2].rstrip('\n'))
            new_book_dict[broken_column[2].rstrip('\n')] = new_parameter_list
        return [new_book_dict, ordered_parameter_list]
    except IndexError:
        print "File formatted incorrectly.  Creating blank database."
        return new_book_dict


# This method tries to open the given file, manages all exceptions, and parses
# the file into lines.  It sends each line to the read_line_to_dicts method.  It
# closes the file when it is done, and it keeps track of the next usable key, by
# setting it to 1 plus the highest key read from a file. It returns this key when it
# is done to be stored into the current_key variable.
# noinspection PyUnusedLocal
def read_lines_from_file(filename):
    try:
        file_to_open = open(filename, 'r')
        print "File %s successfully opened!" % filename
    except IOError:
        fresh_book = create_book()
        print "No valid file! Nothing imported. Sad day..."
        print "The current usable key after importing is %d." % get_available_key(new_book)
        wait = raw_input("Press enter to continue.")
        return fresh_book
    except:
        print "Unexpected Error: ", sys.exc_info()[0]
        raise
    current_line = 0
    book_dict = {}
    column_list = []
    for l in file_to_open:
        if current_line == 0:
            book_dict_and_parameter_list = read_first_line(l)
            book_dict = book_dict_and_parameter_list[0]
            if book_dict.__len__() == 0:
                break
            column_list = book_dict_and_parameter_list[1]
        else:
            book_dict = read_line_to_dicts(book_dict, column_list, l)
        current_line += 1
    file_to_open.close()
    if book_dict.__len__() == 0:
        book_dict = create_book()
    print "The current usable key after importing is %d." % get_available_key(book_dict)
    wait = raw_input("Press enter to continue.")
    return book_dict

new_book = read_lines_from_file('book_file')
search(new_book)

'''
# This function reads through the entire key list and writes all of the values associated
# with that key into a line of a file that is defined in the argument.
# The values are separated by a | character, and they are put in in an order that allows
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


# This loops forever until a break is encountered (meaning the user has chosen to quit with option 6)
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
        current_key += 1
    elif choice == '3':
        success = 0			 # Here I am making a sub-loop that continues asking the user for a key to edit
        while success == 0:  # Until the user gives a valid key that is used in the first_name_dict
            key_to_edit = int(raw_input("Which key do you want to edit?  "))
            if key_to_edit in first_name_dict:
                edit_contact(key_to_edit)
                success = 1
            else:			 # Otherwise it prints an error and repeats the loop.
                print "This isn't a valid key, m8.  Please try again."
    elif choice == '4':
        success = 0
        while success == 0:	 # Using the same technique as above
            key_to_delete = int(raw_input("Which key do you want to delete?  "))
            if key_to_delete in first_name_dict:
                delete_contact(key_to_delete)
                success = 1
            else:
                print "This isn't a valid key, m8.  Please try again."
        
    elif choice == '5':
        search()
    elif choice == '6':      # We need to make sure the file saves when the user exits the program.
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

'''