class ExampleModule:
	
	#initialize the module as an object
	def __init__(this):
		this.text = "Hello World!"
	
	#run the module
	def run(this, prompt = ""):
		print(this.text)
		print("run() called with prompt: " + prompt)
	
	#return keywords relevant to the module, used to figure out which module to run
	def getKeywords(this):
		return ["example module", "test", "text module", "example", "hi", "hello", "hello world"]
	
	#return human-readable name of module
	def getName(this):
		return "Example Module"
	
	#whether this module is appropriate for any prompt (ex. search engine)
	def isGeneric(this):
		return False
