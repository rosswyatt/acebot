import random

def shitty_task(command):
	if command[9:16] == "below 7":
		members = ["@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton"]
	elif command[9:20] == "exclude jon":
		members =  ["@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton"]
	else:
		members = ["@jonroberts", "@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton"]

	return "The winner is " + random.choice(members)