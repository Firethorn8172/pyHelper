import urllib.parse
import os

class GeminiModule:
	
	#initialize the module as an object
	def __init__(this):
		None
	
	#run the module
	def run(this, prompt = ""):
		if prompt.strip() in ["amfora", "gemini", "gemini browser", "browser"]: #If just asking for a gemini client
			os.system("amfora")
		else:
			prompt = prompt.replace("amfora", "", 1).strip() #If gemini URL, open
			for word in prompt.split(" "):
				if word[0:9] == "gemini://":
					prompt = word
					os.system("amfora \"" + prompt + "\"")
					return
			
			#If not, send to Kennedy
			prompt = prompt.replace("gemini browser", "", 1).replace("browser", "", 1).strip()
			if prompt.split(" ")[0] == "gemini": #remove "gemini" only if at beginning (assumes user is specifying module)
				prompt = prompt.replace("gemini", "", 1).strip()
			os.system("amfora \"gemini://kennedy.gemi.dev/search?" + prompt + "\"")
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["amfora", "gemini://", "gemini", "gemini browser", "browser"]
	
	#return human-readable name of module
	def getName(this):
		return "Amfora Gemini Client"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return True
