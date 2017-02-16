import random

def shitty_task(command):
	if command == "below 7":
		members = ["Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
		print("Hello")
	elif command == "exclude jon":
		members =  ["Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
	else:
		members = ["Jon", "Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]

	return random.choice(members)