
#define colors
white = (255, 255, 255)
black = (0,0,0)
darkgrey =(40,40,40)
lightgrey = (100,100,100)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)

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