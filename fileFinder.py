import os
import difflib
import re

class FileFinder:
	def __init__(this, startDir = "/home"):
		this.files = []
		this.filesRaw = []
		this.resetBoostedFormats()
		this.setDir(startDir)

	def hasGoodFormat(this, inputFileName): #Tests if the file's format is a preferred format
		if len(inputFileName) > this.formatLength:
			inputFileName = inputFileName[len(inputFileName) - this.formatLength:]
		for f in this.formats:
			if f in inputFileName:
				return True
		return False

	def findFileHelper(this, target): #Actually does the finding
		bestMatchScore = -1
		bestMatch = ""
		for i in range(len(this.files)): #For every lowercase alphanumericized filename
			ratio = difflib.SequenceMatcher(None, target, this.files[i]).ratio() #Start with just string similarity
			if this.hasGoodFormat(this.files[i]): #Boost for a desireable extension
				ratio *= 1.7
			if target in this.files[i]: #Boost for exact substring matches
				ratio *= 2.6 #This and the other boost multiplier were found by tweaking until results were good
			if ratio > bestMatchScore: #Compare scores and store best
				bestMatchScore = ratio
				bestMatch = this.filesRaw[i] #Store raw path
		return [bestMatch, bestMatchScore] #Return path and score

	def promptAndFind(this): #findFile but with input() instead of a parameter
		print("File to search for:")
		target = re.sub("[^a-zA-Z0-9]", "", str(input())).lower()
		res = this.findFileHelper(target)
		if "and" in target:
			res2 = this.findFileHelper(target.replace("and", ""))
			if res2[1] > res[1]:
				return res2[0]
		return res[0]
	
	def findFile(this, target): #Find a file
		target = re.sub("[^a-zA-Z0-9]", "", target).lower()
		res = this.findFileHelper(target)
		if "and" in target: #Test without "and" in case the file had "&", which is subbed out when making names alphanumeric
			res2 = this.findFileHelper(target.replace("and", ""))
			if res2[1] > res[1]:
				return res2[0]
		return res[0]

	def compareMatches(this, target, matches): #Similar to findFileHelper but for a custom list of files to search
		bestMatchScore = -1
		bestMatch = ""
		for i in range(len(matches)):
			item = re.sub("[^a-zA-Z0-9]", "", re.sub(".*/", "", matches[i])).lower()
			ratio = difflib.SequenceMatcher(None, target, item).ratio()
			if this.hasGoodFormat(item):
				ratio *= 1.7
			if target in item:
				ratio *= 2.6
			if ratio > bestMatchScore:
				bestMatchScore = ratio
				bestMatch = matches[i]
		return bestMatch

	def resetBoostedFormats(this): #Sets boosted formats to a default list of common files
		this.setBoostedFormats(["pdf","txt","mp3","mp4","png","jpg","jpeg","gif","wav","ogg","odt","webp","mkv","html","md","xlsx","ods","py","java","zip","tar","7z","gz"])

	def setBoostedFormats(this, extensionArr): #Sets boosted formats to a string array containing file extensions
		maxLen = -1
		for i in range(len(extensionArr)): #Lowercase and alphanumericize for easier comparisons
			extensionArr[i] = re.sub("[^a-zA-Z0-9]", "", str(extensionArr[i])).lower()
			if len(extensionArr[i]) > maxLen: #Also find longest length to avoid comparing too much or little text
				maxLen = len(extensionArr[i])	
		this.formatLength = maxLen + 2 #Make the allotted length for formats a bit longer just in case
		this.formats = extensionArr

	def setDir(this, dir): #Set directory to search
		this.filesRaw = os.popen("find " + dir + " -type f | grep -v \"/\\.\"").read().splitlines() #Run find for all non-hidden files and make into array
		while this.filesRaw.count("") > 0: #Remove blank lines if any
			this.filesRaw.remove("")
		this.files = []
		for item in this.filesRaw: #Make second array with only lowercase alphanumericized names (no paths) for easy comparisons
			this.files.append(re.sub("[^a-zA-Z0-9]", "", re.sub(".*/", "", item)).lower())

#Old algorithm used this disaster
#print(difflib.get_close_matches(target, files, cutoff=0, n=10))
