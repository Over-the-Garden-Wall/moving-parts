# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from math import *
from Tkinter import *
from ttk import *




class Application(Frame):
    """ A GUI app! """
    #cards = []    
    max_rows = 5;
    
    def __init__(self, master):
        #initialize the framezor
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks =0 #click counter!
        self.create_widgets()
        self.cards = []
        
    def create_widgets(self):
        #make the three buttons
    
        self.button1 = Button(self)
        self.button1["text"] = "Click me!"        
        self.button1["command"] = self.add_card        
        self.button1.grid() 
        

        
    def add_card(self):
        #increase the click count and display the new total
    
        self.cards.append(Card("./samp_im.gif"))
        r = self.button_clicks % 5
        c = 1 + int(self.button_clicks/5)
                
        
        self.cards[self.button_clicks].grid(row=r, column=c)
        self.button_clicks += 1
        
    def nonsense_click(self):
        
        self.button_clicks += 1
        self.button1["text"] = "card #" + str(self.button_clicks)
        #self.add_card()
        
        

class Card(Canvas):
    #A card object
    
    def __init__(self, img_fn):
        Canvas.__init__(self)
        self.configure(width = 50)
        self.configure(height = 50)
        self.img = PhotoImage(file = img_fn)
        self.create_image(25,25, image=self.img)
        self.bind("<Button-3>", self.right_click)
        self.bind("<Button-1>", self.left_click)
        
        #Canvas.__init__(self, *args, **kwargs)
        #super(Card, self).__init__(*args, **kwargs)
        
    def right_click(self, event):
        self.img = PhotoImage(file = "./samp3.gif")
        self.create_image(25,25, image=self.img)
        

    def left_click(self, event):
        self.img = PhotoImage(file = "./samp2.gif")
        self.create_image(25,25, image=self.img)
        
        
        


#create window
root = Tk()

#modify root window
root.title("main window")
root.geometry("800x800")

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
