import fileFinder
import getpass
import re
import subprocess
import time

class WhereIsModule:
	
	#initialize the module as an object
	def __init__(this):
		this.ff = fileFinder.FileFinder("/home/" + getpass.getuser() + "/")
		this.ff.setBoostedFormats(["doc","docx","odt","rtf","txt","tex","wpd","ppt","pptx","bmp","gif","heic","jpg","jpeg","png","psd","tif","ai","svg","pdf","epub","pub","ods","xls","xlsx","dgn","dwg","dxf","step","stl","stp","html","php","zip","7z","tar","gz"])
	
	#run the module
	def run(this, prompt = ""):
		#Filter prompt to just query
		prompt = re.sub("[^a-zA-Z0-9 ]", "", prompt).lower().replace("where is", "", 1).replace("where did i put", "", 1).strip()
		path = this.ff.findFile(prompt) #Search
		print(path) #Print where the file is
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["where is", "where did i put"]
	
	#return human-readable name of module
	def getName(this):
		return "Where Is"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
