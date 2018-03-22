##############################################
# The list that will hold the shopping items #
##############################################
shopping_list = []




################
# App Commands #
################

# Display the current list of shopping items by typing "SHOW" #
def show_current_list():
    for item in shopping_list:
        print('> ' + item)

# Show the HELP menu by typing "HELP" #
def show_help_menu():
    print('Type "SHOW" in order to see all items on your shopping list so far.')
    print('Type "HELP" if assistance is needed for using this app.')
    print('Type "NOTHING" in order to exit this app.')




##########################
# The actual app process #
##########################

# Starting up the app #
print('STARTING SHOPPING LIST...\n')
print('Here is your shopping list.  In order to add needed items, type them in one at a time.\n')
print('If you need help, you can type in the following commands:\n')
show_help_menu()
print('\n')

# Type in shopping items here, and they will be added to the list. #
while True:
    shopping_item = input('What do you need?  ')
    print('\n')
    if shopping_item.lower() == 'show':
        print("Here's what's on the list so far:")
        print('\n')
        show_current_list()
        print('\n')
    elif shopping_item.lower() == 'help':
        show_help_menu()
        print('\n')
    elif shopping_item.lower() == 'nothing':
        break
    else:
        shopping_list.append(shopping_item)

# Exiting out of the app will show the full list of shopping items #
print("Here's your final list of shopping items:\n")
show_current_list()
print('\n')
print('SHOPPING LIST COMPLETED...')
