import random

def shitty_task(command):
	if command[9:16] == "below 7":
		members = ["@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@rossk", "@sam_lindsay"]
	elif command[9:20] == "exclude jon":
		members =  ["@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@olivia_lewis", "@rossk", "@sam_lindsay"]
	else:
		members = ["@jonroberts", "@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@olivia_lewis", "@rossk", "@sam_lindsay"]


	return "The winner is <" + random.choice(members) + ">"