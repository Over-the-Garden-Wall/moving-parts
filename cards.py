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

    def refresh():
        pass

    def buy_card(self):
        config.active_player.buy_card(self)
    
    def sell_card(self):
        config.active_player.sell_card(self)
                    
        
class Creature(Card):
    
    combat_state = 0
    power = 0
    health = 0
    card_id = 0    
    #0 = null, 1 = attack, 2 = block low, 3 = block high
    
    def __init__(self, master):
        
        #print master
            
        
        Card.__init__(self, master)
        
        self.birth()
        self.refresh()
        
        
    def right_click(self, event):
        self.combat_state = self.combat_state+1        
        if self.combat_state == 4:
            self.combat_state = 0
        
        self.refresh()
            
    def birth(self):
        pass
    
    def death(self):
        pass
                
    def refresh(self):
        self.delete("all")
        self.create_image(25,25, image = self.img)
        self.create_image(15,40, image = config.numbers[self.power])
        self.create_image(35,40, image = config.numbers[self.health])
        if self.owner != -1:
            self.create_image(40, 10, image = config.combat_icons[self.combat_state])
            
        

class Suika1(Creature):
    
    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika1.gif")            
        self.cost_money = 200
        self.power = 2
        self.health = 1
        
        Creature.__init__(self, master)
        
    
class Suika2(Creature):

    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika2.gif")            
        self.cost_money = 300
        self.power = 1
        self.health = 3
    
        Creature.__init__(self, master)


class Suika3(Creature):
    
    def __init__(self, master):
        self.img = PhotoImage(file = "./images/suika3.gif")            
        self.cost_money = 400
        self.power = 0
        self.health = 1
 
        Creature.__init__(self, master)
         
 
    def birth(self):
        config.active_player.money_inc += 200
        
    def death(self):
        config.active_player.money_inc -= 200        
