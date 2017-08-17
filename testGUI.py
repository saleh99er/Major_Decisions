from appJar import gui
class Pages(object):
    def __init__(self):
        self.currentPage = 0

    def nextPage(self):
        self.currentPage = self.currentPage + 1

    def reset(self):
        #not neccessary, optional
        self.currentPage = 0

class App(Pages):
    def __init__(self):
        Pages.__init__(self)
        self.data = []
        self.gui = gui()

    def openWindow(self):
        if(self.currentPage == 0):
            welcomeMenu()
        elif(self.currentPage == 1):
            firstPage()
        elif(self.currentPage == 2):
            secondPage()
        else:
            print "ERROR"
            self.currentPage = self.currentPage -1
        #now adds a page
        self.nextPage()

def press(button): #Change this function later, bugs present, can't access the variable in line 3 which I'm trying to use on line 11,12,16,17 and 19
    if button == "Quit":
        print "Exiting"
        majorDecisions.gui.stop()
    elif button == "Start":
        majorDecisions.gui.stop()
        majorDecisions.nextPage()
        majorDecisions.openWindow()
    elif button == "Next":
        majorDecisions.gui.stop()
        majorDecisions.nextPage()
        majorDecisions.openWindow()



def firstPage():
    majorDecisions.gui = gui()
    majorDecisions.gui.startLabelFrame("First Question")
    majorDecisions.gui.setFont(20)
    majorDecisions.gui.addLabel('q1', '1. What is your intended major?')
    majorDecisions.gui.addEntry('e1')
    majorDecisions.gui.addButtons(['Quit','Next'],press)
    majorDecisions.gui.stopLabelFrame()
    majorDecisions.gui.go()

def secondPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
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

def welcomeMenu():
    app = gui()
    app.startLabelFrame("Welcome Menu")
    app.setFont(20)
    app.addLabel("t1","Welcome to...\n Major Decisions", 0, 0)
    app.addButtons(["Start","Quit"],press)
    app.stopLabelFrame()
    #runs the app
    app.go()

majorDecisions = App()
majorDecisions.openWindow()
# app = gui()
# app.startLabelFrame("Welcome Menu")
# app.setFont(20)
# app.addLabel("t1","Welcome to...\n Major Decisions", 0, 0)
# app.addButtons(["Start","Quit"],press)
# app.stopLabelFrame()
#
# #runs the app
# app.go()