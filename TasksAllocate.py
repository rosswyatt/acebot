import random

def shitty_task(command):
	if command[10:17] == "below 7":
		members = ["Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
		print("Hello")
	elif command[10:21] == "exclude jon":
		members =  ["Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
	else:
		members = ["Jon", "Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]

	return random.choice(members)

