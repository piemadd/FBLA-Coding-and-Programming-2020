import json


def userIndex(data):  # returns an array of all user IDs
	ids = []
	profiles = data['profiles']
	x = 0
	while x < len(profiles):
		profile = profiles[x]
		ids.append(profile['id'])
		x = x + 1
	return ids

def hoursIndex_ids(data):  # returns the IDs of all of the hours
	ids = []
	hours = data['hours']
	x = 0
	while x < len(hours):
		hour = hours[x]
		ids.append(hour['hourId'])
		x = x + 1
	return ids

def hoursIndex(data):  # returns an array of all hours
	ids = []
	profiles = data['profiles']
	x = 0
	while x < len(profiles):
		profile = profiles[x]
		ids.append(profile['id'])
		x = x + 1
	return ids


def loadDatabase(fileName): # loads the database file when a valid filename is passed
	with open(fileName, "r") as read_file:
		data = json.load(read_file)
	return data

def saveDatabase(data, filename):
	f = open(filename, "w+")
	json.dump(data, f)
	#f.write(str(data))
	#f.close()

def findUser(data, userID): # returns the user profile when the user ID is passed
	profiles = data['profiles']
	x = 0
	while x < len(profiles):
		tempProfile = profiles[x]
		if tempProfile['id'] == userID:
			return profiles[x]
		else:
			x = x + 1
	if x <= len(profiles):
		return Exception

def findUserLocation(data, userID):
	profiles = data['profiles']
	x = 0
	while x < len(profiles):
		tempProfile = profiles[x]
		if tempProfile['id'] == userID:
			return x
		else:
			x = x + 1
	if (x <= len(profiles)):
		return Exception

def findHourLocation(data, hourID):
	hours = data['hours']
	x = 0
	while x < len(hours):
		tempHour = hours[x]
		if tempHour['hourId'] == hourID:
			return x
		else:
			x = x + 1
	if (x <= len(hours)):
		return Exception

def findHourIds(data, userID): # returns all of the hour ids worked by a user when the user ID is passed
	user = findUser(data, userID)
	return user['hourIds']

def findHour(data, hourID): # returns the data about the hour worked when the hour ID is passed
	hourID = int(hourID)
	hours = data['hours']
	return hours[hourID]

def findHours(data, userID): # returns all of the hours worked by a user, including the data
	hours = findHourIds(data, userID)
	x = 0
	fullHours = []
	while x < len(hours):
		fullHours.append(findHour(data, hours[x]))
		x = x + 1
	return fullHours

def deleteHours(data, userID, hourID): # deletes an hour entry from user
	while len(hourID) < 6:
		hourID = '0' + hourID
	user = findUser(data, userID)
	hours = user['hourIds']
	hours.remove(hourID)
	user['hourIds'] = hours
	users = data['profiles']
	x = findUserLocation(data, userID)
	users[x] = user
	data['profiles'] = users
	return data

def addHours(data, userID, date, numofHours):
	hoursIndex = data['hours']
	tempHourEntry = {}
	hourID = str(len(hoursIndex))
	while len(hourID) < 6:
		hourID = '0' + hourID
	tempHourEntry['hourID'] = hourID
	tempHourEntry['studentNumber'] = userID
	tempHourEntry['date'] = date
	tempHourEntry['hours'] = numofHours
	hoursIndex.append(tempHourEntry)
	data['hours'] = hoursIndex
	user = findUser(data, userID)
	hours = user['hourIds']
	hours.append(hourID)
	user['hourIds'] = hours
	users = data['profiles']
	x = findUserLocation(data, userID)
	users[x] = user
	data['profiles'] = users
	return data

def editHours(data, userID, date, numofHours, hourID):
	hoursIndex = data['hours']
	tempHourEntry = {}
	while len(hourID) < 6:
		hourID = '0' + hourID
	tempHourEntry['hourID'] = hourID
	tempHourEntry['studentNumber'] = userID
	tempHourEntry['date'] = date
	tempHourEntry['hours'] = numofHours
	hoursIndex.append(tempHourEntry)
	data['hours'] = hoursIndex
	user = findUser(data, userID)
	hours = user['hourIds']
	hours.append(hourID)
	user['hourIds'] = hours
	users = data['profiles']
	x = findUserLocation(data, userID)
	users[x] = user
	data['profiles'] = users
	return data

def addUser(data, nameLast, nameFirst, gradeLevel, id):
	tempUser = {}
	tempUser['nameLast'] = nameLast
	tempUser['nameFirst'] = nameFirst
	tempUser['gradeLevel'] = gradeLevel
	tempUser['id'] = id
	profiles = data['profiles']
	profiles.append(tempUser)
	data['profiles'] = [profiles]

def editUser(data, nameLast, nameFirst, gradeLevel, id):
	tempUser = {}
	tempUser['nameLast'] = nameLast
	tempUser['nameFirst'] = nameFirst
	tempUser['gradeLevel'] = gradeLevel
	tempUser['id'] = id
	userLocation = findUserLocation(data, id)
	profiles = data['profiles']
	profiles[userLocation] = tempUser
	data['profiles'] = [profiles]

def deleteUser(data, id):
	profiles = data['profiles']
	profile = findUser(data, id)
	profiles.remove(profile)
	return True

#data = loadDatabase("data_file.json")