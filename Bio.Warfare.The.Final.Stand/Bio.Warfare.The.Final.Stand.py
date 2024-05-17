#create characters

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
class Hero(Character):
    def __init__(self,name,health =40, power =5):
        super().__init__(self,name,health,power)

class Villain(Character):
    def __init__(self, name, health = 30, power = 10):
        super().__init__(self,name,health,power)
        
class Scientist (Character):
    
class Detective(Character):





#define colors
white = (255, 255, 255)
black = (0,0,0)
darkgrey =(40,40,40)
lightgrey = (100,100,100)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)

#define grid parameters 
def draw_grid(self):
    for x in range(0, width, tilesize):
        pg.draw.line(self.screen, lightgrey, (x,0), (x, heigh))
    for y in range(0, heigh, tilesize):
        pg.draw.line(self.screen, lightgrey, (0,y), (width,y))

        
def draw(self):
    self.screen.fill(bgcolor)
    self.draw_grid()
    self.all_sprites.draw(self.screen)
    pg.display.flip()
    
def draw(self):
    self.screen.fil

#game settings
width = 1024 #how many squares fit on screen
heigh = 768
fps = 60
title = "Bio-Warfare: The Final Stand"
bgcolor = darkgrey

tilesize = 32
gridwidth = width / tilesize
gridheigh = heigh / tilesize