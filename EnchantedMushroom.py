from tkinter import Label


class EnchantedMushroom  (object):

    # initialize an empty list to hold 4 images. 
    displayImages:list=[]

       
    # constructor;
    def __init__(self, mushroomDisplay:Label):

        # initialize 2 instance properties

        #1 an int to track the enchantment level of the mushroom, with 0 indicating no enchantment
        self.__level:int=0

        #2 a Label to maintain the display for the mushroom (much like the LightBulb class)
        self.__mushroomDisplay:Label=mushroomDisplay

        # set up the display to show the image at index 0 of displayImages
        self.__mushroomDisplay["image"] = EnchantedMushroom.displayImages[0]

        # "bind" mouse click events to the instance method processClick
        self.__mushroomDisplay.bind( "<Button>", self.processClick )

    
    #getter for the enchantment level instance property
    def getEnchantment (self)->int:

        #Should return an int that is 0 for the initial enchantment level (not enchanted)
        #1 for the next level of enchantment, etc.
        return self.__level

    
    # setter to change changing the level of enchantment
    def setEnchantment (self,level:int):
        
        #Checks if the given value is valid (between 0 and the # of levels)
        #if self.__levelTracking>=0:
        #If an invalid value is passed, it should assign the closest valid value
        
        # For a value < 0, set the enchantment to the initial level. 
        if level<0:
            self.__level=0
            
        # For a value > the final level value, set the enchantment to the final level.
        elif level>=len(EnchantedMushroom.displayImages):
            self.__level=len(EnchantedMushroom.displayImages)-1

        
        else:
            self.__level=level
        
        self.refreshDisplay()

    # instance method to "advance" the level of enchantment by invoking the getEnchantment and setEnchantment methods
    def enchant (self):
        self.setEnchantment(self.getEnchantment()+1)

    # instance method for handling click events
    #(we'll skip the type for this as it would require a little more GUI explanation than is within the scope of this course).
    def processClick(self, event):
        print( f"Clicking: {self}" )
        self.enchant()
        print(f"...and now {self}")


    # instance method for refreshing the display to update the displayed image to be the corresponding image in the displayImages list.
    def refreshDisplay(self):
        self.__mushroomDisplay["image"]=EnchantedMushroom.displayImages[self.getEnchantment()]


    # instance method to return a string representation of the mushroom
    def __str__(self)->str:
        # If the mushroom is enchanted at level 0, 
        # for example, it should return 
        #"A mushroom enchanted at level 0."

        mushroomStr:str=f"A mushroom enchanted at level {self.getEnchantment()}."
        return mushroomStr

