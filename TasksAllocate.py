import random

def shitty_task(command):
	if command[9:16] == "below 7":
		members = ["Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
	elif command[9:20] == "exclude jon":
		members =  ["Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]
	else:
		members = ["Jon", "Sam", "Robin", "Ross", "Dan J", "Dan H", "Karik", "George", "Hayden", "Ben", "Vicky", "Andy"]

	return "The winner is " + random.choice(members)