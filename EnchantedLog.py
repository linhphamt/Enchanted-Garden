from tkinter import *
from EnchantedMushroom import EnchantedMushroom

class EnchantedLog (object):

    #empty list to hold 2 images
    displayImages:list=[]

    #constructor; requires a single argument when invoked for the Label instance used as a display
    def __init__(self, logDisplay:Label):

        # initialize 3 instance properties:

        #1 a boolean to track whether the log is enchanted (True) or not (False); it should initially not be enchanted
        self.__enchantment:bool=False

        #2 a list to track the EnchantedMushroom instances associated to the log; it should be initialized to the empty list
        self.__mushroom:list=[]

        #3  Label to maintain the display for the log (much like the EnchantedMushroom class)
        self.__logDisplay:Label=logDisplay
        
        # set up the display to show the image at index 0 of displayImages
        self.__logDisplay["image"] = EnchantedLog.displayImages[0]

        # "bind" mouse click events to the instance method processClick
        self.__logDisplay.bind( "<Button>", self.processClick )

   
    # getter for the enchantment level instance property; return a bool
    def isEnchanted(self):
        return self.__enchantment

    # instance method; return a type of None
    def enchant(self)->None:
        
        # check if all the mushrooms associated to this log have some level of enchantment (>0). 
        # if so, update the instance property to set the enchanted state to True and refresh the display.  
        notEnchanted:bool=False
        
        for mushroom in self.__mushroom: 
            if mushroom.getEnchantment()==0:
                notEnchanted=True
                
        if not notEnchanted:
            self.__enchantment=True

            #refresh the display
            self.refreshDisplay()

    # instance method; requires a single argument of type EnchantedMushroom; returns a type of None
    def addMushroom (self, displayMushroom:EnchantedMushroom):
        
        # add the passed mushroom to the list of mushrooms (maintained as an instance property)
        self.__mushroom.append(displayMushroom)

    # instance method for handling click events
    def processClick (self, event):
        print( f"Clicking: {self}" )
        self.enchant()
        print(f"...and now {self}")

    # instance method for refreshing the display
    # update the displayed image to be the corresponding image in the displayImages list
    def refreshDisplay(self)->None:
        
        # if the log is enchanted, display the image at index 0
        if self.isEnchanted():
            self.__logDisplay["image"]=EnchantedLog.displayImages[1]
            
        # Otherwise, display the image at index 1
        else:
            self.__logDisplay["image"]=EnchantedLog.displayImages[0]

    # instance method; return a string representation of the log 
    def __str__(self)->str:

        # "A log that is not enchanted with 3 mushrooms." or "A log that is enchanted with 4 mushrooms."
        result:str = "A log that is "
        
        if not self.isEnchanted():
            result += "not "
            
        result += f"enchanted with {len(self.__mushroomList)} mushrooms."
        return result
