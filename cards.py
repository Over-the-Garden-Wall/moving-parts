# -*- coding: utf-8 -*-
"""
Individual cards live here

Created on Mon Oct 12 23:40:13 2015

@author: kagami
"""

from Tkinter import *
from ttk import *
import config

class Card(Canvas):
    #A card object
    owner = -1 #default to shop ownership    
    name = ""
    cost_money = 0    
    cost_white = 0    
    cost_blue = 0    
    cost_green = 0
    just_bought = 1    
    
    img = None    
    
    def __init__(self, master):
        
        Canvas.__init__(self, master)
        #print master
        self.configure(width = 50)
        self.configure(height = 50)
        self.bind("<Button-3>", self.right_click)
        self.bind("<Button-1>", self.left_click)
                  
        self.create_image(25,25, image = self.img)
        
        #Canvas.__init__(self, *args, **kwargs)
        #super(Card, self).__init__(*args, **kwargs)
        
    def right_click(self, event):
        pass
        

    def left_click(self, event):
        if self.owner == -1:
            self.buy_card()
        elif self.just_bought == 1:
            self.sell_card()            
        else:            
            self.activate()

    def activate():
        pass            

    def buy_card(self):
        config.active_player.buy_card(self)
    
    def sell_card(self):
        config.active_player.sell_card(self)
                    
        
class Creature(Card):
    
    combat_state = 0
    #0 = null, 1 = attack, 2 = block low, 3 = block high
    
    def __init__(self, master):
        
        #print master
            
        
        Card.__init__(self, master)
        
        self.birth()
        #print img_str
        #print self.img        
        
        #Canvas.__init__(self, *args, **kwargs)
        #super(Card, self).__init__(*args, **kwargs)
        
    def right_click(self, event):
        combat_state = combat_state+1        
        if combat_state == 4:
            combat_state = 0
            
    def birth(self):
        pass
    
    def death(self):
        pass
                

class Suika1(Creature):
    
    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika1.gif")            
        Creature.__init__(self, master)
        
        self.cost_money = 200    
    
    
class Suika2(Creature):

    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika2.gif")            
        Creature.__init__(self, master)
        
        self.cost_money = 300
    

class Suika3(Creature):
    
    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika3.gif")            
        Creature.__init__(self, master)
        
        self.cost_money = 400
 
    def birth(self):
        config.active_player.money_inc += 200
        
    def death(self):
        config.active_player.money_inc += 200        
