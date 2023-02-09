# Start with users that need to be verified
# Make an empty list to hold comfirmed users
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []


# Verify each user until there are none
# As confirmed, move each to the empty list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe folowing users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

