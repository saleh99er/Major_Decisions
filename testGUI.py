from appJar import gui

global currentPage
currentPage = 0

def press(button): #Change this function later, bugs present, can't access the variable in line 3 which I'm trying to use on line 11,12,16,17 and 19
    if button == "Quit":
        print "Exiting"
        app.stop()
    elif button == "Start":
        currentPage = currentPage + 1
        print currentPage
        app.stop()
        firstPage()
    elif button == "Next":
        currentPage = currentPage + 1
        print currentPage
        app.stop()
        selectPage(currentPage)



def selectPage(pageNo):
    if (pageNo == 2):
        secondPage()
    elif (pageNo == 3):
        thirdPage()
    else:
        print 'ERROR'


def firstPage():
    app = gui()
    app.startLabelFrame("First Question")
    app.setFont(20)
    app.addLabel('q1', '1. What is your intended major?')
    app.addEntry('e1')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()
    app.go()

def secondPage():
    app = gui()
    app.startLabelFrame("Second Question")
    app.setFont(20)
    app.addLabel('q2', '2. What state or country did you reside in?')
    app.addEntry('e2')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()
    app.go()


    entry1 = app.getEntry('e1')
    print "DEBUG: entry1 is " + entry1 #current issue entry1 is returned as an empty string
    print entry1                        #FIX LATER


app = gui()
app.startLabelFrame("Welcome Menu")
app.setFont(20)
app.addLabel("t1","Welcome to...\n Major Decisions", 0, 0)
app.addButtons(["Start","Quit"],press)
app.stopLabelFrame()

#runs the app
app.go()