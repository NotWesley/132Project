from Tkinter import *

class Level(object):
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.solutions = {}
        self.hints = {}

    # accessors and mutators for Level
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def solutions(self):
        return self._solutions

    @solutions.setter
    def solutions(self, value):
        self._solutions = value

    @property
    def hints(self):
        return self._hints

    @hints.setter
    def hints(self, value):
        self._hints = value


    # helper functions

    def addSolution(self, solution, level):
        self._solutions[solution] = level

    def addHint(self, hint, level):
        self._hints[hint] = level

    # string representation of each level
    def __str__(self):
        # welcome and level number
        s = "Welcome to {}. \n".format(self.name)

        for hint in self.hints.keys():
            s += hint
            
        
        # s += "Solutions: "
        # for solution in self.solutions.keys():
          #  s += solution + " "
        return s

###############################################################################
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createLevels(self):

        # creates rooms and gives them names
        intro = Level("The Game", "images/intro.gif")
        l1 = Level("Level 1", "images/level1.gif")
        l2 = Level("Level 2", "images/level2.gif")
        l3 = Level("Level 3", "images/level3.gif")
        l4 = Level("Level 4", "images/level4.gif")
        outro = Level("The End", "images/outro.gif")
        
        # intro level attributes
        intro.addSolution("enter", l1)
        
        # level 1 attributes
        l1.addSolution("good luck", l2)
        l1.addHint("It's easy as cba", l1)

        # level 2 attributes
        l2.addSolution("it only gets harder", l3)
        l2.addHint("SOS", l2)

        # level 3 attributes
        l3.addSolution("pass", l4)
        l3.addHint("Three is the Biggest one", l3)

        # level 4 attributes
        l4.addSolution("finale", outro)
        l4.addHint("The grand", l4)

        # outro level attributes
        outro.addHint("Don't worry this is just the demo", outro)
                      
        
        # make global variable currentLevel and set it to intro
        global currentLevel
        Game.currentLevel = intro 
        
                
        
    def setUpGUI(self):
        self.pack(fill = BOTH, expand = 1)

        Game.player_input = Entry(self, bg = "white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side = BOTTOM, fill = X)
        Game.player_input.focus()

        # set up the image on the left
        img = None
        Game.image = Label(self, width = WIDTH / 2, image = img)
        Game.image.image = img
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False)

        # set up the text on the right
        text_frame = Frame(self, width = WIDTH / 2)
        Game.text = Text(text_frame, bg = "lightgrey", state=DISABLED)
        Game.text.pack(fill = Y, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)

    def setLevelImage(self):
        if(Game.currentLevel == None):
            Game.img = PhotoImage(file = "images/placeholder.gif")
        else:
            Game.img = PhotoImage(file = Game.currentLevel.image)

        Game.image.config(image = Game.img)
        Game.image.image = Game.img

    def setStatus(self, status):
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)

        if(Game.currentLevel == None):
            Game.text.insert(END, "You were killed and all proof of your existence destroyed")
        else:
            Game.text.insert(END, str(Game.currentLevel)) # here for other text

        Game.text.config(state = DISABLED)

    def play(self):
        # sets up the levels
        self.createLevels()

        # sets up the GUI
        self.setUpGUI()

        # sets up the image of the current Level
        self.setLevelImage()

        # sets up the status
        self.setStatus("")
    
    def process(self, event):
        chances = 3
        action = Game.player_input.get()
        action = action.lower()
        words = action

        if(action.strip() in ["quit", "bye", "exit"]):
            exit(0)

        if(Game.currentLevel == None):
            Game.player_input.delete(0, END)
            return

        if(words in Game.currentLevel.solutions):
            response = "Congrats, you made it to the next level"
            chances = 3
            Game.currentLevel = Game.currentLevel.solutions[words]
        else:
            response = "Incorrect"
            chances -= 1

        if(chances == 0):
            Game.currentLevel = None
        
        self.setStatus(response)
        self.setLevelImage()
        Game.player_input.delete(0, END)
        
###############################################################################
# screen defaults
WIDTH = 800
Height = 600

# create window
window = Tk()
window.title("Message from ")

# create the GUI as a canvas inside the window
g = Game(window)

# play the game
g.play()

# transfer contorl to the GUI indefinitely
window.mainloop()
