import fileFinder
import getpass
import subprocess
import re
import time

class MusicModule:
	
	#initialize the module as an object
	def __init__(this):
		this.ffMusic = fileFinder.FileFinder("/home/" + getpass.getuser() + "/Music")
		this.ffMusic.setBoostedFormats(["mp3","aif","m3u","m4a","wma","wav","ogg","flac","mp4","3gp","asf","avi","flv","m4v","mov","mpg","swf","ts","vob","wmv","mkv","mpeg"])
		this.ffVideo = fileFinder.FileFinder("/home/" + getpass.getuser() + "/Videos")
		this.ffVideo.setBoostedFormats(["mp3","aif","m3u","m4a","wma","wav","ogg","flac","mp4","3gp","asf","avi","flv","m4v","mov","mpg","swf","ts","vob","wmv","mkv","mpeg"])
	
	#run the module
	def run(this, prompt = ""):
		if prompt.strip() == "music": #If just "music", ask for the song
			print("Song Name: ", end="")
			prompt = str(input())
		else: #Else, filter to just name query
			prompt = prompt.replace("play the song", "", 1).replace("play", "", 1).replace("music", "", 1)
		prompt = re.sub("[^a-zA-Z0-9 ]", "", prompt).lower().strip() #Lowercase alphanumericization for easy comparison
		path = this.ffMusic.compareMatches(prompt, [this.ffMusic.findFile(prompt), this.ffVideo.findFile(prompt)]) #Find best file between Music/ and Videos/
		subprocess.Popen(["/bin/vlc", path], close_fds=True) #Open in VLC
		time.sleep(1) #Delay hopefully puts new pyHelper prompt after any CLI output from the above
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["play", "play the song", "music"]
	
	#return human-readable name of module
	def getName(this):
		return "Music (via VLC)"

	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
