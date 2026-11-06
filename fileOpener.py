import fileFinder
import getpass
import re
import subprocess
import time

class FileOpenerModule:
	
	#initialize the module as an object
	def __init__(this):
		this.ff = fileFinder.FileFinder("/home/" + getpass.getuser() + "/")
		this.ff.setBoostedFormats(["doc","docx","odt","rtf","txt","tex","wpd","ppt","pptx","bmp","gif","heic","jpg","jpeg","png","psd","tif","ai","svg","pdf","epub","pub","ods","xls","xlsx","dgn","dwg","dxf","step","stl","stp","html","php","zip","7z","tar","gz"])
	
	#run the module
	def run(this, prompt = ""):
		prompt = re.sub("[^a-zA-Z0-9 ]", "", prompt).lower().replace("open", "", 1).strip() #Filter prompt to filename query
		path = this.ff.findFile(prompt) #Find file
		subprocess.Popen(["xdg-open", path], close_fds=True) #Use xdg-open to open with defualt app
		time.sleep(1) #Delay hopefully puts new pyHelper prompt after any CLI output from the above
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["open"]
	
	#return human-readable name of module
	def getName(this):
		return "File Opener"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
