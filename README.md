# pyHelper

An attempt at making a modular terminal voice assistant

pyHelper is a program that runs much like traditional voice assistants, only using Python's STDIN and STDOUT instead of audio. It has a few basic operations built-in, but most of its functionality comes from modules, which are simply Python classes with a few specific functions. These modules are ideally independent of each other, but they're still supposed to work together under pyHelper.py to form a versatile program.

Language input is designed to feel somewhat natural, so commands like "play Bad Apple" or "open helloWorld.py" are possible. Using a generic module (a module designed to handle arbitrary string inputs), you can even ask pyHelper things like "What is the average air speed velocity of an unladened swallow?" or "How many figs to one Newton?"

pyHelper is also designed to not use AI by default. This means that none of the code I wrote is AI-generated, and pyHelper and its premade modules don't use AI. This is not to say AI usage is forbidden - it's perfectly possible, even despite my personal hatred of AI - but the spirit of the project is to avoid using it and rely instead on coding your own functionality.

## Base Functionality
Without calling a module, pyHelper can:
- Display help with "help" or "?"
- Clear the screen with "clear", "c", or "cls"
- Forward commands to a shell by preceeding them with "!"
- Exit with "exit", "quit", "bye", "x", or "q"

## Module Structure
All modules are Python classes, generally named after the function of the module (ex. WeatherModule, WhereIsModule). They contain the following functions:
- \_\_init\_\_: Handles initialization of the module, ex. instance variables, caching a data set, etc.
- run: Runs the module. The full prompt as inputted by the user will also be forwarded to this function.
- getKeywords: Returns an array containing string keywords related to the module, ex. "play" for a music module.
- getName: Returns a human-readable name for the module. This will be printed in the help menu.
- isGeneric: Returns whether the module is designed to handle arbitrary input (True) or just input related to the keywords (False)

## Premade Modules
- Example: Says "Hello World!" and echoes your prompt.
- Weather: Curls the weather from wttr.in.
- FileOpener: Opens the file in your home directory that best matches a query.
- Music: Plays media from ~/Music and ~/Videos in VLC.
- Http: Uses Lynx with DuckDuckGo for web browsing. Will take generic input as a search query.
- Gemini: Uses Amfora to access gemspace. Will take generic input as a search query.
- Sandwich: References XKCD 149.
- WhereIs: Prints where that file you lost is.
- Run: Runs a program in /usr/share/applications or ~/.local/share/applications. May crash if the "Exec=" line is weirdly formatted, but I tried to prevent that.

## Installing Modules
All modules should be located in the same directory as pyHelper.py, but as long as you can import the module, you can place it wherever. As an example, you could place the source code in /bin/pyHelper/ and use a bash script at /bin/pyhelper running "python3 /bin/pyHelper/pyHelper.py" to launch the program.

To install a module, you'll need to import the module at the top of pyHelper.py (ex. "import exampleModule") and add an instance of the module in the modules array (ex. modules = \[exampleModule.ExampleModule(), ...\]). After that, you're ready to go! Just keep in mind that modules at the beginning of the list have priority over later ones, and only the first generic module will be used if no keywords match the prompt.

Modules may be removed by removing them from the list and unimporting them.
