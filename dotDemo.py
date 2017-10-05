#Clay Kynor
#10/5/17
#dotDemo.py - loops and graphics - making some dots

from ggame import *

purple = Color(0xF000FF,1)

dot = RectangleAsset(20,LineStyle(1,purple),purple)

for j in range(20): #prints the row 20 times
    for i in range(20): #prints one row of dots
        Sprite(dot,(20 + 40*i,20 + 40 * j)) 

App().run()