# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from Tkinter import *



class Application(Frame):
    """ A GUI app! """
    
    def __init__(self, master):
        #initialize the framezor
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks =0 #click counter!
        self.create_widgets()
        
    def create_widgets(self):
        #make the three buttons
    
        self.button1 = Button(self)
        self.button1["text"] = "Click me!"
        self.button1["command"] = self.update_count        
        self.button1.grid()
        
        
    def update_count(self):
        #increase the click count and display the new total
        self.button_clicks += 1
        self.button1["text"] = "Clicks: " + str(self.button_clicks)
        



#create window
root = Tk()

#modify root window
root.title("main window")
root.geometry("600x400")

app = Application(root)


"""

#create frame to hold widgets
app = Frame(root)
app.grid()

label = Label(app, text = "A Label")
label.grid()

button1 = Button(app, text = "This is a button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "button 2!")

button3 = Button(app)
button3.grid()
button3["text"] = "button 3"

"""

#kick off the event loop
root.mainloop()
