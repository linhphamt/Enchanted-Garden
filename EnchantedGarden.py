from tkinter import *
from EnchantedMushroom import EnchantedMushroom
from EnchantedLog import EnchantedLog


# main function; require no parameter
def main():

    # set up the Tkinter window 
    window:Tk = Tk()

    # set the title
    window.title("Enchanted Garden")
    
    # set the background color to navy
    window.configure(background='navy')

    # set dimensions to 800 x 600
    window.geometry("800x600")


    # Initializes the art assets:
    # use for loops to create the PhotoImage elements that the EnchantedMushroom 
    # and EnchantedLog classes each share.

    for i in range(4):
        EnchantedMushroom.displayImages.append(PhotoImage(file = f"mushroom{i}.png"))

    for i in range(2):
        EnchantedLog.displayImages.append(PhotoImage(file = f"log{i}.png"))


    # Create and add two logs by invoking the addLogWithMushrooms (described next):
    # One log should be at coordinates (0,100) with 3 mushrooms
    # The other log should be at coordinates (300,350) with 4 mushrooms
    addLogwithMushroom(window,0,100,3)
    addLogwithMushroom(window,300,350,4)

    #Launch the Tkinter window
    window.mainloop()


# Requires 4 parameters: the Tkinter window,2 int for x and y coordinate, 1 int for the number of mushrooms
def addLogwithMushroom(window:Tk, poSx:int, poSy:int, mushroomNum:int):

    # create a Tkinter Label instance to display the log
    logDisplay:Label = Label(window, bg="navy")

    # ask the created Label instance to place itself on the window at the specified x and y coordinates
    logDisplay.place(x=poSx,y=poSy)

    # create the EnchantedLog instance and pass it the GUI label for displaying
    # excuting the EnchantedLog Class
    log:EnchantedLog = EnchantedLog(logDisplay)

    # create the mushrooms using the createMushroom function (described next)
    for i in range (mushroomNum):
        Mushroom: EnchantedMushroom=createMushroom(window, (poSx + 40 + i*100), (poSy-100))
    
        # add them to the log using the log's instance method addMushroom
        log.addMushroom(Mushroom)


# Requires 3 parameters: the Tkinter window, 2 int for x and y coordinate
def createMushroom(window:Tk,posx:int,posy:int):

    # create a Tkinter Label instance to display the mushroom
    mushroomDisplay:Label = Label(window, bg="navy")

    # ask the created Label instance to place itself on the window at the specified x and y coordinates
    mushroomDisplay.place(x=posx,y=posy)

    # create the EnchantedMushroom instance and pass it the GUI label for displaying
    # executing the EnchantedMushroom Class
    mushroom:EnchantedMushroom = EnchantedMushroom(mushroomDisplay)

    #return the variable with the EnchantedMushroom instance (so the log can add it)
    return mushroom


main()
