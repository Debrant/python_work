def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know aboaut a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last


	for key, value in user_info.items():
		profile[key] = value
		print(value)
	return profile

#user_profile = build_profile('albert', 'einstien', location= 'princeton', field = 'physics')
user_profile = build_profile('Nathan', 'Bryant', location= 'North West US', field = 'physics', occupation = 'engineer')

print(user_profile )