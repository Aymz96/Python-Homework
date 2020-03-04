# SIMPLEST - Restaurant Waiter Helper

# User Stories

menu = ['falafel', 'HuMMus', 'couscous', 'Bacalhau a Bras']
food_order = []

#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
firstname = input('What is you name? ')
print(f"{firstname} heres the menu: ")
print(menu[0].capitalize())
print(menu[1].capitalize())
print(menu[2].capitalize())
print(menu[3].capitalize())

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.
first_order = input('What would you like to order? ').capitalize()
food_order.append(first_order)

second_order = input('What else would you like to order? ').capitalize()
food_order.append(second_order)

third_order = input('lastly what would you like to order? ').capitalize()
food_order.append(third_order)

print(food_order)



# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything