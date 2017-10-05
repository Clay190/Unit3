#Clay Kynor
#10/5/17
#dotDemo.py - loops and graphics - making some dots

from ggame import *

purple = Color(0xF000FF,1)

dot = CircleAsset(20,LineStyle(1,purple),purple)

for i in range(20):
    Sprite(dot,(20 + 40*i,20))
    

App().run()