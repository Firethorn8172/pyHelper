import urllib.parse
import os

class HttpModule:
	
	#initialize the module as an object
	def __init__(this):
		None
	
	#run the module
	def run(this, prompt = ""):
		if "://" in prompt: #Detect http urls and run Lynx at given URL
			prompt = prompt.split(" ")
			for word in prompt:
				if word[0:4] == "http":
					prompt = word
					break
			
			os.system("lynx \"" + prompt + "\"")
		else:
			prompt = prompt.replace("ddg", "", 1).replace("duckduckgo", "", 1).replace("lx", "", 1).strip() #Filter to query
			if prompt == "" or ("lynx" in prompt and prompt != "lynx") or prompt == "browser" or prompt == "web browser": #If just asking for a browser
				os.system("lynx https://lite.duckduckgo.com/lite")
			else:
				prompt = urllib.parse.quote_plus(prompt) #Convert to search engine query format and open DDG
				os.system("lynx \"https://lite.duckduckgo.com/lite/?q=" + prompt + "\"")
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["http://", "https://", "lynx", "lx", "ddg", "duckduckgo", "browser", "web browser"]
	
	#return human-readable name of module
	def getName(this):
		return "Lynx Browser + DuckDuckGo"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return True
