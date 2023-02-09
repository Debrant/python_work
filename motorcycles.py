motorcycles = [	'honda', 'yamaha', 'suzuki']
#print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('kawasaki')
first_owned = motorcycles.pop(4)
too_expensive = motorcycles.pop(3)
#print(motorcycles)

print('The first motorcycle I owned was a ' + first_owned.title() + '. \nI would like to buy a ' + too_expensive.title() + ', but I cannot afford one.')