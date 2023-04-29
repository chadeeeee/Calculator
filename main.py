try:
   import os, sys
      
   os.chdir(sys._MEIPASS)
except AttributeError:
   pass

import eel


eel.init("web")

eel.start("main.html", size=(354, 587))