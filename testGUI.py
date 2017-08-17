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
        self.answer = None

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
    elif button == "Try Again?":
        majorDecisions.gui.stop()
        majorDecisions.reset()
        majorDecisions.openWindow()

    #Just for question 2
    elif button == "Yes":
        secondPageUS()
    elif button == "No":
        secondPageCountry()

def welcomeMenu():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
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
    app.stopLabelFrame()
    app.go()


def secondPageUS():
    app = majorDecisions.gui
    app.startLabelFrame("Second Question cont. (State)")
    app.addLabel("stateQ","Which state are you from?")
    app.addEntry('e2a')
    app.addButtons(['Quit','Next'],press)
    app.stopLabelFrame()


def secondPageCountry():
    app = majorDecisions.gui
    app.startLabelFrame("Second Question cont. (Country)")
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
    app.go()

def fourthPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("Calculating")
    app.addLabel('calc','Calculating...\nplease wait')
    print "DEBUG: Calculating..."
    app.stopLabelFrame()
    app.go()    #BUG currently show above until waitTime below is done, then show bottom portion for a second and move on to the final page
                #WILL FIX TOMORROW

    waitTime = random.randint(3,15)
    print "DEBUG: waiting " + str(waitTime) + " seconds"
    time.sleep(waitTime)

    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.addLabel('done','Calculation done')
    app.go()

    time.sleep(1)
    #onto the final page
    majorDecisions.nextPage()
    majorDecisions.openWindow()

def fifthPage():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("Results")
    app.addLabel("suspension",'The major decided by our patented algorithm is...')
    app.go()
    time.sleep(5)
    app.addLabel('answer',majorDecisions.answer)
    app.addButtons(["Try Again?","Quit"],press)
    app.go()
    # entry1 = app.getEntry('e1')
    # print "DEBUG: entry1 is " + entry1 #current issue entry1 is returned as an empty string
    # print entry1                        #FIX LATER


#SCRIPT CODE -
majorDecisions = App()
majorDecisions.openWindow()
