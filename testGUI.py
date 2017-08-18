from appJar import gui
import time
import random
import threading

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
        exit()
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

    else:
        print "ERROR with press function"


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
    a = threading.Thread(target=fourthPagePart1) #calculating...
    b = threading.Thread(target=fourthPagePart2) #calculation done
    a.start()
    waitTime = random.randint(3,15)
    print "DEBUG: waiting " + str(waitTime) + " seconds"
    time.sleep(waitTime)
    b.start()


def fourthPagePart1():
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("Calculating")
    app.addLabel('calc','Calculating...\nplease wait')
    print "DEBUG: Calculating..."
    app.stopLabelFrame()
    app.go()


def fourthPagePart2():
    app = majorDecisions.gui
    app.addLabel('done','\n\nCalculation done')
    print "DEBUG: closing fourth page"
    app.addButtons(['Quit','Next'],press) #APP STOPS RESPONDING HERE


def fifthPage():
    print 'DEBUG: made it to the fifth page'
    a = threading.Thread(target=fifthPagePartOne) #suspension
    b = threading.Thread(target=fifthPagePartTwo) #reveal answer
    print 'DEBUG: starting part one'
    a.start()
    time.sleep(5)
    print 'DEBUG: starting part two'
    b.start()


def fifthPagePartOne():
    time.sleep(1)
    majorDecisions.gui = gui()
    app = majorDecisions.gui
    app.startLabelFrame("(Drum roll please)")
    app.addLabel("suspension",'The major decided by our patented algorithm is...')
    app.stopLabelFrame()
    app.go()


def fifthPagePartTwo():
    app = majorDecisions.gui()
    app.addLabel('answer',majorDecisions.answer)
    app.addButtons(["Try Again?","Quit"],press)
    #app.go()
    # entry1 = app.getEntry('e1')
    # print "DEBUG: entry1 is " + entry1 #current issue entry1 is returned as an empty string
    # print entry1                        #FIX LATER


#SCRIPT CODE -
majorDecisions = App()
majorDecisions.openWindow()
