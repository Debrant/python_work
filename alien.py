# # set initial position and alien speed
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print("Original x-position: " + str(alien_0['x_position']))

# # move alien to the right
# # determine how far to move based on speed
# if alien_0['speed'] == 'slow':
    # x_increment = 1
# elif alien_0['speed'] == 'medium':
    # x_increment = 2
# else:
    # #this must be a fast alien
    # x_increment = 3

# # the new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position: " + str(alien_0['x_position']))

# container for sorting aliens and a counter to help randomize
aliens =[]
count = 1 
# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    if count%3 == 0:
        new_alien['color']= 'yellow'
        new_alien['speed'] = 'medium'
        count = count + 1
    elif count%3 == 1:
        new_alien['color']= 'red'
        new_alien['points'] = 10
        count = count + 1
    elif count%3 == 2:
        new_alien['color']= 'yellow'
        new_alien['speed'] = 'medium'
        count = count + 1
    aliens.append(new_alien)
 
# randomize some of the aliens
    
#show some aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show total
print("Total number of aliens: " + str(len(aliens)))
