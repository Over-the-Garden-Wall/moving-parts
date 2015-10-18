# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from math import *
from Tkinter import *
from ttk import *
import config
from cards import *
#import copy


class Application(Frame):
    """ A GUI app! """
    #cards = []    
    max_rows = 5;
    player = []
    
    def __init__(self, master):
        #initialize the framezor
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks =0 #click counter!
        self.create_players()
        config.active_player = self.player[0]                

        for n in range(10):
            config.numbers[n] = PhotoImage(file = "./images/number" + str(n) + ".gif")
        
        config.combat_icons[0] = PhotoImage(file = "./images/null.gif")
        config.combat_icons[1] = PhotoImage(file = "./images/combat_attack.gif")
        config.combat_icons[2] = PhotoImage(file = "./images/combat_block_low.gif")
        config.combat_icons[3] = PhotoImage(file = "./images/combat_block_high.gif")
        
        
        self.create_widgets()
        self.cards = []
        
        
        
    def create_players(self):
        for n in range(2):
            self.player.append(Player(self, n, 2*n))
        
        
    
    def create_widgets(self):
        #make the three buttons
        
        self.columnconfigure(0, minsize = 200)
        self.columnconfigure(1, minsize = 600)
        self.rowconfigure(0, minsize = 300)
        self.rowconfigure(1, minsize = 100)
        self.rowconfigure(2, minsize = 300)
        self.rowconfigure(3, minsize = 100)
        
        
        
        self.shopFrame = Shop(self)   
               
        
        self.shopFrame.grid(row =0, column =0, rowspan=4)
        
                

        self.shopFrame.add_card(Suika1(self.shopFrame))
        self.shopFrame.add_card(Suika2(self.shopFrame))
        self.shopFrame.add_card(Suika3(self.shopFrame))                
                
        self.button2 = Button(self.shopFrame)
        self.button2["text"] = "switch player!"        
        self.button2["command"] = self.switch_player
        self.button2.grid()
        

    def switch_player(self):
        player_no = config.active_player.player_no         
        if player_no == 0:
            player_no = 1
        else:
            player_no = 0
            
        config.active_player = self.player[player_no]   
        config.active_player.earn_income()


        
class Player(object):
    player_no = 0
    board = 0
    
    #currency
    money = 1000
    white = 0
    blue = 0
    green = 0
    
    money_inc = 400    
    white_inc = 0
    blue_inc = 0
    green_inc = 0
    
    def __init__(self, master, player_no, board_row):
        self.player_no = player_no
        self.board = Gameboard(master)
        self.board.grid(row = board_row, column =1)
        self.info = Player_info(master)      
        self.info.update_money_labels(self.money, self.blue, self.white, self.green)
        self.info.grid(row = board_row+1, column =1)
        
    
    def buy_card(self, shop_card):
        if self.money >= shop_card.cost_money and self.blue >= shop_card.cost_blue and self.white >= shop_card.cost_white and self.green >= shop_card.cost_green:
            self.blue -= shop_card.cost_blue
            self.green -= shop_card.cost_green
            self.white -= shop_card.cost_white
            self.money -= shop_card.cost_money
            self.board.add_card(shop_card)
            self.info.update_money_labels(self.money, self.blue, self.white, self.green)
            
    def earn_income(self):
        self.money += self.money_inc
        self.white += self.white_inc
        self.blue += self.blue_inc
        self.green += self.green_inc
        self.info.update_money_labels(self.money, self.blue, self.white, self.green)
                
    def sell_card(self, card):
        self.blue += card.cost_blue
        self.green += card.cost_green
        self.white += card.cost_white
        self.money += card.cost_money
        self.board.delete_card(card.card_id)
        self.info.update_money_labels(self.money, self.blue, self.white, self.green)
        
class Gameboard(Frame):
    num_cards = 0
        
    def __init__(self, master, **kwargs):    
        Frame.__init__(self, master)
        self.cards = []
        #print self        
            
        
    def add_card(self, card):  
        
        class_type = card.__class__
        self.cards.append(class_type(self))
        self.cards[self.num_cards].card_id = self.num_cards
        
        self.cards[self.num_cards].owner = config.active_player.player_no
        self.num_cards += 1                
        
        self.refresh()
        
        
    def delete_card(self, card_id):
        for n in range(card_id+1, self.num_cards):
            self.cards[n].card_id -= 1
        
        self.cards[card_id].destroy()
        self.cards.pop(card_id)
        self.num_cards -= 1        
        self.refresh()
        
    def refresh(self):

        #self.grid_forget()
            
        for n in range(self.num_cards):
            c = n % config.cards_per_row
            r = int(n/config.cards_per_row)
            
            self.cards[n].grid(row=r, column=c)
            self.cards[n].refresh()
            
            
        
class Player_info(Frame):
    def __init__(self, master, **kwargs):    
        Frame.__init__(self, master)
        self.label1 = Label(self)
        self.label1.grid()
        self.label2 = Label(self)
        self.label2.grid()
        self.label3 = Label(self)
        self.label3.grid()
        self.label4 = Label(self)
        self.label4.grid()
        
    def update_money_labels(self, money, blue, white, green):
        self.label1["text"] = "gold: " + str(money)
        self.label2["text"] = "stars: " + str(blue)
        self.label3["text"] = "cross: " + str(white)
        self.label4["text"] = "gear: " + str(green)    
    

class Shop(Frame):
    
    num_cards = 0
    
    def __init__(self, master, **kwargs):    
        Frame.__init__(self, master)
        self.cards = []
        
        
    def add_card(self, card):
        #self.cards.append(Card(self, card_name))
        self.cards.append(card)
        
        self.cards[self.num_cards].grid()
        self.num_cards += 1


        
        
        


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
