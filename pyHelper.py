import re
import os

#place module imports here
import weather
import fileOpener
import music
import httpBrowser
import geminiBrowser
import sandwich
import whereIs
import runModule

def pyHelperMain():
	#type importName.moduleName() as an element in the array to be able to use the module
	modules = [weather.WeatherModule(), fileOpener.FileOpenerModule(), music.MusicModule(), httpBrowser.HttpModule(), geminiBrowser.GeminiModule(), sandwich.SandwichModule(), whereIs.WhereIsModule(), runModule.RunModule()]
	
	inp = ""
	while True:
		print("pyHelper ~ ", end="")
		inp = input()
		if inp.strip() == "": #Ignore blank lines
			continue
		if inp[0] == "!": #Forward !command to system shell
			os.system(inp[1:])
			continue
		inp = inp.lower()
		if inp in ["exit", "quit", "bye", "x", "q"]: #Exiting
			break;
		if inp in ["help", "?"]: #Help menu
			print("pyHelper: an attempt at making a modular terminal voice assistant")
			print("\nType exit, quit, bye, x, or q to exit\nType clear, c, or cls to clear screen\nStart prompt with ! to forward to shell")
			if len(modules) > 0:
				print("\nInstalled modules:")
				mods = ""
				for module in modules:
					mods += module.getName() + ", "
				mods = mods[0:len(mods) - 2]
				print(mods)
		elif inp in ["clear", "c", "cls"]: #Screen clearing
			os.system("clear")
		elif len(modules) == 0: #No modules error
			print("No modules installed.")
		else: #Calling modules based on input
			bestModule = None
			bestModuleScore = 0
			genericModuleFound = False
			genericModule = None
			
			for modObj in modules: #Look at all installed modules
				if modObj.isGeneric() and not genericModuleFound: #If generic module, remember that
					genericModule = modObj
					genericModuleFound = True;
				
				matchCount = 0
				for kw in modObj.getKeywords(): #Count matching keywords
					if re.sub("[^a-zA-Z0-9 ]", "", kw).lower() in re.sub("[^a-zA-Z0-9 ]", "", inp).lower():
						matchCount += 1
				if matchCount > bestModuleScore: #Maximize matching keywords and store best module
					bestModuleScore = matchCount
					bestModule = modObj
			
			if bestModuleScore > 0: #If a module is found, run it
				bestModule.run(inp)
			elif genericModuleFound == True: #Else, run a generic module if available
				genericModule.run(inp)
			else: #Else, complain to user
				print("No appropriate module found.")

if __name__ == "__main__":
	pyHelperMain()
