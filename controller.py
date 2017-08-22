from flask import Flask

app = Flask(__name__)

class User:
	username = ""
	password = ""
	points = ""

userOne = User()
userOne.username = "Shafiq"
userOne.password = "Bleh"
userOne.points = 100

userTwo = User()
userTwo.username = "Sheeni"
userTwo.password = "Kitty"
userTwo.points = 1000

myuser = ""

hardCodedDB = [userOne, userTwo]

@app.route('/')
def start():
	return "Welcome to my website! To search for a user, type in their name above after the /"

@app.route('/<name>')
def returnUser(name=""):
	for user in hardCodedDB:
		if user.username == name:
			myuser = user

	return "The user that you picked is {} and has {} points".format(name, myuser.points)

@app.route('/login/<username>/<password>')
def authenticate(username="", password=""):
	for user in hardCodedDB:
		if user.username == username and user.password == password:
			return "{} has successfully logged in!".format(username)
	return "Invalid credentials."

app.run(debug=True, port=8001, host='0.0.0.0')
