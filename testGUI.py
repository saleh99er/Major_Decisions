from appJar import gui
import time
import random


class Pages(object):
    def __init__(self):
        self.currentPage = 0

    def nextPage(self):
        self.currentPage = self.currentPage + 1

    def reset(self):
        #not neccessary, optional
        self.currentPage = 0


class App(Pages):
    QUESTIONS = ['Intended Major?', "they from the US?","Which country/state they from?","which dorm are they residing in right now?"]
    def __init__(self):
        Pages.__init__(self)
        self.data = ['ans1','ans2a','ans2b','ans3']
        self.gui = gui()

    def openWindow(self):
        if(self.currentPage == 0):
            welcomeMenu()
        elif(self.currentPage == 1):
            firstPage() #first question
        elif(self.currentPage == 2):
            secondPage() #second question
        elif(self.currentPage == 3):
            thirdPage() #third question
        elif(self.currentPage == 4):
            fourthPage() #"Calculating" page
        elif(self.currentPage == 5):
            fifthPage() #Results page
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

    #Just for question 2
    elif button == "Yes":
        secondPageUS()
    elif button == "No":
        secondPageCountry()

def welcomeMenu():
    app = gui()
    app.startLabelFrame("Welcome Menu")
    app.setFont(20)
    app.addLabel("t1","Welcome to...\n Major Decisions", 0, 0)
    app.addButtons(["Start","Quit"],press)
    app.stopLabelFrame()
    #runs the app
    app.go()

def firstPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("First Question")
    app.setFont(20)
    app.addLabel('q1', '1. What is your intended major?')
    app.addEntry('e1')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()
    app.go()

def secondPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("Second Question")
    app.setFont(20)
    app.addLabel('q2', '2. Do you reside in the US?')
    app.addButtons(['Yes','No'], press)
    app.go()


def secondPageUS():
    app = majorDecisions.gui
    app.addLabel("stateQ","Which state are you from?")
    app.addEntry('e2a')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()

def secondPageCountry():
    app = majorDecisions.gui
    app.addLabel('countryQ', "Which country are you from?")
    app.addEntry('e2b')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()

def thirdPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("Third Question")
    app.addLabel('q3','Where are you dorming Freshman year?')
    app.addEntry('e3')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()

def fourthPage():
    majorDecisions.gui = gui()
    app =  majorDecisions.gui
    app.startLabelFrame("Calculating")
    app.addLabel('calc','Calculating...\nplease wait')
    waitTime = random.randint(3,15)
    time.sleep(waitTime)
    app.addLabel('done','Calculation done')
    time.sleep(1)
    majorDecisions.nextPage()
    majorDecisions.openWindow()

def fifthPage():
    a

    # entry1 = app.getEntry('e1')
    # print "DEBUG: entry1 is " + entry1 #current issue entry1 is returned as an empty string
    # print entry1                        #FIX LATER


#SCRIPT CODE -
majorDecisions = App()
majorDecisions.openWindow()
