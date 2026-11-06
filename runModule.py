import fileFinder
import getpass
import re
import subprocess
import time

class RunModule:
	
	#initialize the module as an object
	def __init__(this):
		this.ff = fileFinder.FileFinder("/usr/share/applications/")
		this.ff.setBoostedFormats(["desktop"])
		this.ff2 = fileFinder.FileFinder("/home/" + getpass.getuser() + "/.local/share/applications/")
		this.ff2.setBoostedFormats(["desktop"])
	
	#run the module
	def run(this, prompt = ""):
		prompt = re.sub("[^a-zA-Z0-9 ]", "", prompt).lower().replace("run", "", 1).strip() #Filter to query
		path = this.ff.compareMatches(prompt, [this.ff.findFile(prompt), this.ff2.findFile(prompt)]) #Search start launchers
		cmd = ""
		with open(path) as file: #Open launcher config and read command
			content = file.readlines()
			for line in content:
				if "Exec=" in line:
					cmd = re.sub("[^/]*(/.*)", "\\1", line.replace("Exec=", "", 1)).replace("Try", "", 1).strip()
		print(cmd)
		subprocess.Popen(cmd.split(" "), close_fds=True) #Run command
		time.sleep(1) #Delay hopefully puts new pyHelper prompt after any CLI output from the above
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["run"]
	
	#return human-readable name of module
	def getName(this):
		return "Run Program"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
