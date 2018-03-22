#######################################
# Instructions on how to use this app #
#######################################
print('ENTERED APP...')
print('Here is your shopping list.')
print('In order to add needed items, type them in one at a time.')
print('When you are finished, enter the word "nothing" to exit out of this app.')


###################################################
# The shopping list that will hold shopping items #
###################################################
shopping_list = []


####################################################################
# Type in shopping items here, and they will be added to the list. #
####################################################################
while True:
    shopping_item = input('What do you need?  ')
    # Type "NOTHING", and the app will finish with a display of the current list.
    if shopping_item.lower() == 'nothing':
        break
    # Type "SHOW" in order to see all shopping items added so far.
    elif shopping_item.lower() == 'show':
        print("Here's what's on the list so far:")
        for item in shopping_list:
            print('> ' + item)
    # Type "HELP" in order to see how to navigate through this app.
    elif shopping_item.lower() == 'help':
        print('Type "NOTHING" in order to exit this app.')
        print('Type "SHOW" in order to see all items on shopping list so far.')
        print('Type "HELP" if assistance is needed for using this app.')
    else:
        shopping_list.append(shopping_item)


###########################################
# Show full list of shopping items so far #
###########################################
print("Here's your updated list of shopping items:")
for item in shopping_list:
    print('> ' + item)
print('EXITED APP...')
