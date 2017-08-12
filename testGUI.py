from appJar import gui

def press(button):
    if button == "Quit":
        app.stop()
    elif button == "Start":
        firstPage()

def firstPage():
    app.startLabelFrame("First Question")
    app.setFont(20)
    app.addLabel('q1', '1. What is your intended major?')
    app.addEntry('e1')
    entry1 = app.getEntry('e1')
    print "DEBUG: entry1 is " + entry1 #current issue entry1 is returned as an empty string
    print entry1                        #FIX LATER
    app.stopLabelFrame()


app = gui()
app.startLabelFrame("Welcome Menu")
app.setFont(20)
app.addLabel("t1","Welcome to...\n Major Decisions", 0, 0)
app.addButtons(["Start","Quit"],press)
app.stopLabelFrame()

#runs the app
app.go()