import pyowm

key = pyowm.OWM('95783b76084ec822fe88a2c6bf49e22f')  # API token

# Search for current weather in London (UK)
observation = key.weather_at_place('London')
current_weather = observation.get_weather().get_status()

#print(current_weather)

weather_emojis = {'Clouds' : ':cloud:',
                  'Clear' : ':sun_with_face:',
                  'Rain' : ':rain_cloud:'}

def weather_emoji(command):
	command_array = str.lower(command).split(' ')

	if len(command_array) == 1:
		observation = key.weather_at_place('London')
		current_weather = observation.get_weather().get_status()
	else:
		command_array.pop(0)
		location = ' '.join(command_array)
		try:
			observation = key.weather_at_place(location)
			current_weather = observation.get_weather().get_status()
			response = weather_emojis[current_weather]
		except:
			response = "That's not a real place."

	return response