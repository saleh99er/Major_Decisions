import appJar
def myLoop():
    print("Looping")
    app = appJar.gui()
    app.after(100, myLoop)

app = appJar.gui()
app.after(0, myLoop)

#I don't know why the after function is not working, will come back to this later