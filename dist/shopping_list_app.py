# Instructions on how to use this app
print('ENTERED APP...')
print('Here is your shopping list.')
print('In order to add needed items, type them in one at a time.')
print('When you are finished, enter the word "nothing" to exit out of this app.')


# The shopping list that will hold shopping items
shopping_list = []


# Type in shopping items here, and they will be added to the list.
# Type in "nothing", and the app will finish with a display of the current list.
while True:
    shopping_item = input('What do you need?  ')
    if shopping_item.lower() == 'nothing':
        break
    shopping_list.append(shopping_item)


# Show full list of shopping items so far
print("Here's what's on the list so far:")

for item in shopping_list:
    print('> ' + item)

print('EXITED APP...')
