import os
import re
from geopy.geocoders import Nominatim

class WeatherModule:
	
	#initialize the module as an object
	def __init__(this):
		None
	
	#run the module
	def run(this, prompt = ""):
		prompt = re.sub("[^a-zA-Z0-9 ]", "", prompt).lower().split(" ") #Split prompt
		city = ""
		for i in range(len(prompt)):
			if prompt[i] == "in" and i <= len(prompt) - 2: #If "in ___" detected, ___ is city name
				city = prompt[i + 1]
		
		if city == "": #If no city, curl plain site
			os.system("curl wttr.in/")
		else: #If city, curl with city name
			os.system("curl wttr.in/" + str(city))
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["weather", "wttr.in"]
	
	#return human-readable name of module
	def getName(this):
		return "Weather (wttr.in)"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
