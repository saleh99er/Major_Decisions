import intendedMajorQ
from appJar import gui


#backbone of app
print "WIP"



#start page "Major Decisions" with two buttons to start and quit it
#throughout the program their needs to be an option to quit


#Operation of all buttons
def press(button):
    if button == "Quit":
        app.stopLabelFrame
    elif button == "Start":
        firstQ()

#first question: What is their intended major then calculates with this
# and moves on to next one if answer is valid otherwise requires a new response
# Info extracted from this, length of the string they gave ranging from 3 to 16
def firstQ():
    app.stopLabelFrame()
    input = "TEMP"
    valReceived.append(questions.intendedMajorQ(input))


#second question: What state do they live in
# Info extracted from this, whether or not an "a" is present in the state name or abbrev they give




#third question: Blah Blah Blah




#select a random value



#third question: blah blah blah



#end the app
def endIt(button):
    if button == "Quit":
        del app

#initializes Major Decisions
valReceived = []
app = gui()
app.addLabel("welcome","Welcome to... \n Major Decisions!")
app.addButton("Start", firstQ)
app.addButton("Quit", endIt)

#run the app
app.go()