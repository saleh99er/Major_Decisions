import intendedMajorQ
from appJar import gui


#backbone of app
print "WIP"



#start page "Major Decisions" with two buttons to start and quit it
#throughout the program their needs to be an option to quit


#Operation of all buttons
def press(button):
    if button == "Quit":
        print "DEBUG: Quit was pressed"
        endIt(button)
    elif button == "Start":
        print "DEBUG: Start was pressed"
        firstQ()


#first question: What is their intended major then calculates with this
# and moves on to next one if answer is valid otherwise requires a new response
# Info extracted from this, length of the string they gave ranging from 3 to 16
def firstQ():
    #How do I Make the first question start at the top instead of in the middle
    app.removeAllWidgets()
    app.setSticky("ew")
    app.startLabelFrame("First Question")
    app.addLabel("debug statement","I can edit the app from here",0,0)





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
global app
app = gui()

app.startPagedWindow("Main Menu")
app.startPage()
#app.setSticky("ew")
app.setFont(20)
app.addLabel("welcome", "Welcome to... \n Major Decisions!", 0, 0)
app.addButtons(["Start", "Quit"], press)
app.stopPage()

#run the app
app.go()