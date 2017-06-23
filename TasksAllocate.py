import random

def shitty_task(command):
	if command[9:16] == "below 7":
		members = ["@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@rossk", "@sam_lindsay", "@anthonycody", "@r_mccormack", "@jo", "@ruddy_duck", "@phil_dent", "@Ben Marshall"]
	elif command[9:20] == "exclude jon":
		members =  ["@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@olivia_lewis", "@rossk", "@sam_lindsay", "@anthonycody", "@r_mccormack", "@jo", "@ruddy_duck", "@phil_dent", "@Ben Marshall"]
	else:
		members = ["@jonroberts", "@samtazzyman", "@robin_linacre", "@ross_wyatt", "@danjones", "@daniel_hills", "@karik.isichei", "@gkelly", "@hayden_sansum", "@bfortescue", "@vickyhughes", "@apoulton", "@marwa_el1", "@olivia_lewis", "@rossk", "@sam_lindsay", "@anthonycody", "@r_mccormack", "@jo", "@ruddy_duck", "@phil_dent", "@john_osmond", "@Ben Marshall", "@Philip Howard"]


	return "The winner is <" + random.choice(members) + ">"