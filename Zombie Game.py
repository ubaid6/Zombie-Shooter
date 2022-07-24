# None of the images and graphics used are copyrighted.
# Images and graphics from opengameart.org
# Font for images and title generated using font-generator.com

from tkinter import *
import time
import os
import random
import sys

# Lists and variables used in the game.
zombieList = []
bulletList = []
zombieDead = []
zombieHouse = []
global wave
wave = 1

# Game is running.
global paused
paused = False
global gameOver
gameOver = False

# This function defines the main menu and adds all the buttons to it.


def mainMenu():
    global menuBg
    menuBg = canvas.create_rectangle(0, 0, 1920, 1080, fill="black")
    global titleimage
    titleimage = canvas.create_image(960, 200, image=titlefile)
    global playButton
    playButton = Button(game, bd=0, bg="black",
                        image=playimage, command=gamePlaying)
    playButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    global settingsButton
    settingsButton = Button(game, bd=0, bg="black",
                            image=settingsimage, command=settingsMenu)
    settingsButton.place(relx=0.5, rely=0.5, anchor=CENTER)
    global loadButton
    loadButton = Button(game, bd=0, bg="black",
                        image=loadimage, command=loadGame)
    loadButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    global leaderBoardButton
    leaderBoardButton = Button(
        game,
        bd=0,
        bg="black",
        image=leaderboardimage,
        command=leaderBoardMenu)
    leaderBoardButton.place(relx=0.5, rely=0.7, anchor=CENTER)
    global quit
    quit = Button(game, image=quitImage, bd=0, bg="black", command=quitGame)
    quit.place(relx=0.5, rely=0.9, anchor=CENTER)
    global HowToPlayButton
    HowToPlayButton = Button(game, image=howtoplayimage, bd=0, bg="black",
                             command=HowToPlay)
    HowToPlayButton.place(relx=0.5, rely=0.8, anchor=CENTER)
    controlLoad()
    fullScreenLoad()

# Displays the text showing you how to play.


def HowToPlay():
    canvas.delete(titleimage)
    quit.destroy()
    playButton.destroy()
    settingsButton.destroy()
    leaderBoardButton.destroy()
    loadButton.destroy()
    HowToPlayButton.destroy()
    HowToPlayFile = open("howtoplay.txt", "r")
    HowToPlayFile = HowToPlayFile.read()
    global HowToPlayText
    HowToPlayText = canvas.create_text(960, 540, text=HowToPlayFile,
                                       font="Arial, 25", fill="white")
    backHowToPlayButton = Button(game, bd=0, bg="black",
                                 image=backimage, command=backHowToPlay)
    backHowToPlayButton.place(x=100, y=900)


def backHowToPlay():
    reset()


# This is the leaderboard function which destroys the previous menu.
# It reads from the leaderboard.txt file and displays it using canvas text.


def leaderBoardMenu():
    HowToPlayButton.destroy()
    canvas.delete(titleimage)
    quit.destroy()
    playButton.destroy()
    settingsButton.destroy()
    leaderBoardButton.destroy()
    loadButton.destroy()
    highscore = canvas.create_image(960, 300, image=highscoreimage)
    stats = []
    leaderBoardFile = open("leaderboard.txt", "r")
    read = leaderBoardFile.read()
    read = read.split('\n')
    for x in read:
        stats.append(x.strip().split(","))
    stats.sort(key=lambda x: int(x[1]), reverse=True)

    first = ("{: <10} {:>10}".format(*stats[0]))
    second = ("{: <10} {:>10}".format(*stats[1]))
    third = ("{: <10} {: >10}".format(*stats[2]))
    fourth = ("{: <10} {: >10}".format(*stats[3]))
    fifth = ("{: <10} {: >10}".format(*stats[4]))
    global statText
    statText = canvas.create_text(
        960,
        700,
        text=first +
        '\n' +
        second +
        '\n' +
        third +
        '\n' +
        fourth +
        '\n' +
        fifth,
        fill="red",
        font="Courier, 50",
        anchor=CENTER)
    leaderBoardFile.close()
    global backLeaderBoardButton
    backLeaderBoardButton = Button(
        game, bd=0, bg="black", image=backimage, command=backLeaderBoard)
    backLeaderBoardButton.place(x=100, y=900)

# The back menu from leaderboard, resets the program.


def backLeaderBoard():
    reset()

# This gets the name from the entry when the game ends.


def leaderBoardConfirm():
    global endEntry
    leaderBoardEntry = endEntry.get()
    leaderBoardFile = open("leaderboard.txt", "a")
    leaderBoardAppend = leaderBoardFile.write(
        '\n' + leaderBoardEntry + "," + str(score))
    leaderBoardFile.close()

# This function loads the necessary data from the load file.
# It reads the data and starts the game with the saved stats.


def loadGame():
    HowToPlayButton.destroy()
    canvas.delete(titleimage)
    loadFile = open("saveFile.txt", "r")
    loadFile = loadFile.read()
    loadFile = loadFile.split('\n')
    for x in loadFile:
        x.strip()
    quit.destroy()
    canvas.delete(menuBg)
    playButton.destroy()
    settingsButton.destroy()
    loadButton.destroy()
    leaderBoardButton.destroy()
    global initialText
    initialText = canvas.create_image(1000, 500, image=initText)
    game.after(1000, Playing(int(loadFile[0]), int(
        loadFile[1]), int(loadFile[2])))

# This function destroys the main menu and calls another function
# startGame() to start the game.


def gamePlaying():
    HowToPlayButton.destroy()
    canvas.delete(titleimage)
    quit.destroy()
    leaderBoardButton.destroy()
    canvas.delete(menuBg)
    playButton.destroy()
    settingsButton.destroy()
    loadButton.destroy()
    global initialText
    initialText = canvas.create_image(1000, 500, image=initText)
    game.after(3000, startGame)

# This starts the game and is called by gamePlaying().


def startGame():
    Playing(0, 0, 0)

# This is the settings menu which can be accessed from
# the main menu. It contains the fullscreen option and the
# Controls menu option.


def settingsMenu():
    HowToPlayButton.destroy()
    canvas.delete(titleimage)
    quit.destroy()
    playButton.destroy()
    settingsButton.destroy()
    loadButton.destroy()
    leaderBoardButton.destroy()
    global fScreen
    fScreen = canvas.create_image(850, 200, image=fullscreenimage)
    global fullScreenButtonOn
    fullScreenButtonOn = Button(
        game, bd=0, bg="black", image=on, command=fullScreenOn)
    fullScreenButtonOn.place(x=1150, y=150)
    global fullScreenButtonOff
    fullScreenButtonOff = Button(
        game, bd=0, bg="black", image=off, command=fullScreenOff)
    fullScreenButtonOff.place(x=1350, y=150)
    global backButtonFullScreen
    backButtonFullScreen = Button(
        game, bd=0, bg="black", image=backimage, command=backFullScreen)
    backButtonFullScreen.place(x=100, y=900)
    global controlScreen
    controlScreen = Button(game, bd=0, bg="black",
                           image=controlimage, command=Controls)
    controlScreen.place(x=600, y=250)

# This function creates the pause menu with 3 options:
# main menu, save and quit. It is called by the pause key event.


def pauseMenu():
    global pauseMenuBg
    pauseMenuBg = canvas.create_rectangle(0, 0, 1920, 1080, fill="black")
    global mainMenuButton
    mainMenuButton = Button(game, bd=0, bg="black",
                            image=mainmenuimage, command=reset)
    mainMenuButton.place(relx=0.5, rely=0.3, anchor=CENTER)
    global quitButton
    quitButton = Button(game, bd=0, bg="black",
                        image=quitImage, command=quitGame)
    quitButton.place(relx=0.5, rely=0.5, anchor=CENTER)
    global saveButton
    saveButton = Button(game, bd=0, bg="black",
                        image=saveimage, command=saveGame)
    saveButton.place(relx=0.5, rely=0.4, anchor=CENTER)

# This is the fuction that saves the game and is called
# by the save button in the pause menu.


def saveGame():
    saveFile = open("saveFile.txt", "w")
    saveFile.write(str(score) + '\n' + str(zombiesInHouse) +
                   '\n' + str(zombiesKilled))
    saveFile.close()

# This function destroys the pause menu and is called by
# the pause event key.


def unpause():
    canvas.delete(pauseMenuBg)
    mainMenuButton.destroy()
    quitButton.destroy()
    saveButton.destroy()

# This loads the fullscreen setting from the fullscreen.txt
# file and determines whether fullscreen is true or false.


def fullScreenLoad():
    fullscreen = open("fullscreen.txt", "r")
    fullscreen = fullscreen.read()
    if fullscreen == '1':
        game.attributes('-fullscreen', True)

# This function loads the controls from the relevant files.


def controlLoad():
    leftOpen = open("leftcontrol.txt", "r")
    leftOpen = leftOpen.read()
    game.bind('<' + leftOpen + '>', move_left)
    rightOpen = open("rightcontrol.txt", "r")
    rightOpen = rightOpen.read()
    game.bind('<' + rightOpen + '>', move_right)
    upOpen = open("upcontrol.txt", "r")
    upOpen = upOpen.read()
    game.bind('<' + upOpen + '>', move_up)
    downOpen = open("downcontrol.txt", "r")
    downOpen = downOpen.read()
    game.bind('<' + downOpen + '>', move_down)
    shootOpen = open("shootcontrol.txt", "r")
    shootOpen = shootOpen.read()
    game.bind('<' + shootOpen + '>', bullet)

# This function creates the control menu which can be accessed
# via the settings menu.


def Controls():
    quit.destroy()
    canvas.delete(fScreen)
    fullScreenButtonOn.destroy()
    fullScreenButtonOff.destroy()
    controlScreen.destroy()
    controlFile = open("controltext.txt", "r")
    controlFileRead = controlFile.read()
    global controlText
    controlText = canvas.create_text(
        500, 500, text=controlFileRead, font=("Arial, 16"), fill="white")
    controlFile.close()
    global text1
    text1 = canvas.create_text(
        1000, 400, text="Strafe Left", font=("Arial, 16"), fill="white")
    global text2
    text2 = canvas.create_text(
        1000, 500, text="Strafe Right", font=("Arial, 16"), fill="white")
    global text3
    text3 = canvas.create_text(
        1000, 600, text="Move Up", font=("Arial, 16"), fill="white")
    global text4
    text4 = canvas.create_text(
        1000, 700, text="Move Down", font=("Arial, 16"), fill="white")
    global text5
    text5 = canvas.create_text(
        1000, 800, text="Shoot", font=("Arial, 16"), fill="white")
    global entry1
    entry1 = Entry(game)
    global entryOne
    entryOne = canvas.create_window(1200, 400, window=entry1)
    global entry2
    entry2 = Entry(game)
    global entryTwo
    entryTwo = canvas.create_window(1200, 500, window=entry2)
    global entry3
    entry3 = Entry(game)
    global entryThree
    entryThree = canvas.create_window(1200, 600, window=entry3)
    global entry4
    entry4 = Entry(game)
    global entryFour
    entryFour = canvas.create_window(1200, 700, window=entry4)
    global entry5
    entry5 = Entry(game)
    global entryFive
    entryFive = canvas.create_window(1200, 800, window=entry5)
    global leftcon
    leftcon = Button(game, bd=0, bg="white",
                     text="Confirm", command=leftConfirm)
    leftcon.place(x=1300, y=390)
    global rightcon
    rightcon = Button(game, bd=0, bg="white",
                      text="Confirm", command=rightConfirm)
    rightcon.place(x=1300, y=490)
    global upcon
    upcon = Button(game, bd=0, bg="white", text="Confirm", command=upConfirm)
    upcon.place(x=1300, y=590)
    global downcon
    downcon = Button(game, bd=0, bg="white",
                     text="Confirm", command=downConfirm)
    downcon.place(x=1300, y=690)
    global shootcon
    shootcon = Button(game, bd=0, bg="white",
                      text="Confirm", command=shootConfirm)
    shootcon.place(x=1300, y=790)
    global defaultButton
    defaultButton = Button(game, bd=0, bg="black",
                           image=defaultimage, command=defaultControls)
    defaultButton.place(x=1500, y=900)
    global backButtonControlScreen
    backButtonControlScreen = Button(
        game, bd=0, bg="black", image=backimage, command=backControls)
    backButtonControlScreen.place(x=100, y=900)
    backButtonFullScreen.destroy()

# This function is called by the 'default' button and
# resets the controls to default, and writes them to the
# relevant files


def defaultControls():
    left = open("leftcontrol.txt", "w")
    left.write("Left")
    left.close()
    right = open("rightcontrol.txt", "w")
    right.write("Right")
    right.close()
    up = open("upcontrol.txt", "w")
    up.write("Up")
    up.close()
    down = open("downcontrol.txt", "w")
    down.write("Down")
    down.close()
    shoot = open("shootcontrol.txt", "w")
    shoot.write("space")
    shoot.close()
    game.bind('<Up>', move_up)
    game.bind('<Down>', move_down)
    game.bind('<Left>', move_left)
    game.bind('<Right>', move_right)
    game.bind('<space>', bullet)

# The following 5 are the functions of each confirm button
# in the controls menu.


def leftConfirm():
    game.unbind(move_left)
    one = entry1.get()
    game.bind('<' + one + '>', move_left)
    write = open("leftcontrol.txt", "w")
    write.write(one)
    write.close()


def rightConfirm():
    one = entry2.get()
    game.bind('<' + one + '>', move_right)
    write = open("rightcontrol.txt", "w")
    write.write(one)
    write.close()


def upConfirm():
    one = entry3.get()
    game.bind('<' + one + '>', move_up)
    write = open("upcontrol.txt", "w")
    write.write(one)
    write.close()


def downConfirm():
    one = entry4.get()
    game.bind('<' + one + '>', move_down)
    write = open("downcontrol.txt", "w")
    write.write(one)
    write.close()


def shootConfirm():
    one = entry5.get()
    game.bind('<' + one + '>', bullet)
    write = open("shootcontrol.txt", "w")
    write.write(one)
    write.close()

# This function takes the user back to the main menu
# from the settings menu


def backFullScreen():
    backButtonFullScreen.destroy()
    fullScreenButtonOn.destroy()
    fullScreenButtonOff.destroy()
    canvas.delete(fScreen)
    canvas.delete(menuBg)
    controlScreen.destroy()
    mainMenu()

# This function takes the user back from the controls menu.


def backControls():
    reset()

# This function activates fullscreen and saves the setting
# to the fullscreen file.


def fullScreenOn():
    game.attributes('-fullscreen', True)
    fullscreen = open("fullscreen.txt", "w")
    fullscreen.write("1")

# This function deactivates fullscreen and again writes to the file.


def fullScreenOff():
    game.attributes('-fullscreen', False)
    fullscreen = open("fullscreen.txt", "w")
    fullscreen.write("0")

# This function resets the program and is called by several buttons.


def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)

# Quits the game and is called by several buttons.


def quitGame():
    game.destroy()

# Cheat code, is called by 'c'.


def Cheat(event):
    global paused
    if paused:
        paused = False
    else:
        paused = True

# Pauses and unpauses the game with 'p'.


def pause(event):
    global paused
    if paused:
        paused = False
        unpause()
    else:
        paused = True
        pauseMenu()

# Creates bullet.


def bullet(event):
    playerCoords = canvas.coords(player)
    bullet = canvas.create_oval(
        playerCoords[0] + 22,
        playerCoords[1] - 40,
        playerCoords[0] + 27,
        playerCoords[1] - 35)
    canvas.itemconfig(bullet, fill="red", outline="yellow")
    bulletList.append(bullet)

# Spawns zombies.


def zombieSpawn(numZombies):
    zombies = 0
    while zombies < numZombies:
        zombieXcoord = random.randint(100, 1800)
        frame = canvas.create_image(zombieXcoord, 0, image=zombie)
        game.update()
        zombieList.append(frame)
        zombies += 1

# The following 4 are movement events.


def move_up(event):
    x = 0
    y = -30

    canvas.move(player, x, y)


def move_down(event):
    x = 0
    y = +30

    canvas.move(player, x, y)


def move_left(event):
    x = -30
    y = 0

    canvas.move(player, x, y)


def move_right(event):
    x = +30
    y = 0

    canvas.move(player, x, y)

# Boss key, is called by 'Esc'.


def bossKey(event):
    global paused
    global boss
    if paused:
        canvas.delete(boss)
        paused = False
    else:
        boss = canvas.create_image(960, 540, image=bossImage)
        paused = True


game = Tk()

# Creation of window and background using canvas function.
# ALl the images are loaded here to be used in functions.
canvas = Canvas(game, width=1920, height=1080, bd=0)
canvas.pack()
grass = PhotoImage(file="Grass.png")
canvas.create_image(960, 540, image=grass)

highscoreimage = PhotoImage(file="highestscorers.png")
titlefile = PhotoImage(file="main.png")
leaderboardimage = PhotoImage(file="leaderboardimage.png")
loadimage = PhotoImage(file="loadimage.png")
saveimage = PhotoImage(file="save.png")
mainmenuimage = PhotoImage(file="mainmenu.png")
bossImage = PhotoImage(file="bossimage.png")
defaultimage = PhotoImage(file="default.png")
controlimage = PhotoImage(file="controls.png")
backimage = PhotoImage(file="back.png")
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")
fullscreenimage = PhotoImage(file="fullscreen.png")
settingsimage = PhotoImage(file="settings.png")
quitImage = PhotoImage(file="quit.png")
playimage = PhotoImage(file="playimage.png")
zombie = PhotoImage(file="frame72.png")
playerimage = PhotoImage(file="player.png")
player = canvas.create_image(900, 900, image=playerimage)
initText = PhotoImage(file="initialtext.png")
endGame = PhotoImage(file="gameover.png")
houseimage = PhotoImage(file="house1.png")
howtoplayimage = PhotoImage(file="howtoplay.png")
house = canvas.create_image(960, 1300, image=houseimage)

# Pause, Boss key, and cheat bindings.
game.bind('<p>', pause)
game.bind('<Escape>', bossKey)
game.bind('<c>', Cheat)

# The main function that runs the game.
# It defines the conditions which makes the zombies spawn.
# Increases difficulty as the player progresses.
# Defines the conditions when the zombies are killed.
# Defines the conditions for when the player loses.


def Playing(currentScore, zombieHouseNumber, zombieKilledNumber):
    global initialText
    canvas.delete(initialText)
    global score
    score = currentScore
    global wave
    global gameOver
    global scoreLabel
    global zombiesInHouse
    global zombiesKilled
    zombiesInHouse = zombieHouseNumber
    zombiesKilled = zombieKilledNumber
    scoreLabel = Label(game, text="Score: " + str(score),
                       font="Arial, 20", bg="red")
    scoreLabel.place(x=1200, y=4)
    global waveLabel
    waveLabel = Label(game, text="Wave: " + str(wave),
                      font="Arial, 20", bg="red")
    waveLabel.place(x=1400, y=4)
    global zombieLabel
    zombieLabel = Label(game, text="Zombies in House: " +
                        str(zombiesInHouse), font="Arial, 20", bg="red")
    zombieLabel.place(x=1600, y=4)
    zombiesInHouse = zombieHouseNumber
    zombiesKilled = zombieKilledNumber

    x = 0
    y = 1
    while True:
        game.update()
        if not paused:
            if zombiesKilled in range(10, 19):
                wave = 2
                waveLabel.config(text="Wave: " + str(wave))
                y = 1.2
            if zombiesKilled in range(20, 29):
                wave = 3
                waveLabel.config(text="Wave: " + str(wave))
                y = 1.4
            if zombiesKilled in range(30, 39):
                wave = 4
                waveLabel.config(text="Wave: " + str(wave))
                y = 1.6
            if zombiesKilled in range(40, 49):
                wave = 5
                waveLabel.config(text="Wave: " + str(wave))
                y = 1.8
            if zombiesKilled in range(50, 59):
                wave = 6
                waveLabel.config(text="Wave: " + str(wave))
                y = 2
            if zombiesKilled in range(60, 69):
                wave = 7
                waveLabel.config(text="Wave: " + str(wave))
                y = 2.2
            if zombiesKilled in range(70, 79):
                wave = 8
                waveLabel.config(text="Wave: " + str(wave))
                y = 2.4
            if zombiesKilled in range(80, 89):
                wave = 9
                waveLabel.config(text="Wave: " + str(wave))
                y = 2.6
            if zombiesKilled in range(90, 99):
                wave = 10
                waveLabel.config(text="Wave: " + str(wave))
                y = 2.8
            if zombiesKilled in range(100, 109):
                wave = 11
                waveLabel.config(text="Wave: " + str(wave))
                y = 3.0
            if zombiesKilled in range(110, 119):
                wave = 12
                waveLabel.config(text="Wave: " + str(wave))
                y = 3.2
            if zombiesKilled in range(120, 129):
                wave = 13
                waveLabel.config(text="Wave: " + str(wave))
                y = 3.4
            if zombiesKilled >= 129:
                wave = 14
                waveLabel.config(text="Wave: " + str(wave))
                y = 3.6
            if len(zombieList) == 0:
                zombieSpawn(random.randint(3, 5))
            if len(zombieList) == 2:
                zombieSpawn(random.randint(3, 5))
            for i in zombieList:
                canvas.move(i, x, y)
            game.update()
            time.sleep(0.010)
            for bullets in bulletList:
                canvas.move(bullets, 0, -20)
                game.update()
                bulletCoords = canvas.coords(bullets)
                for zombies in zombieList:
                    zombieCoords = canvas.coords(zombies)
                    bulletX1 = zombieCoords[0] - 40
                    bulletX2 = zombieCoords[0] + 40
                    bulletY1 = zombieCoords[1] - 10
                    bulletY2 = zombieCoords[1] + 10

                    if bulletCoords[0] in range(
                            int(bulletX1),
                            int(bulletX2)) and bulletCoords[1] in range(
                            int(bulletY1),
                            int(bulletY2)):
                        zombieDead.append(zombies)
                        zombiesKilled += 1
                        canvas.delete(zombies)
                        canvas.delete(zombies)
                        canvas.delete(zombies)
                        canvas.delete(bullets)
                        score += 10
                        scoreLabel.config(text="Score: " + str(score))
                        try:
                            bulletList.remove(bullets)
                        except BaseException:
                            ValueError
                        zombieList.remove(zombies)
                        game.update()

            for zombies in zombieList:
                zombieCoords = canvas.coords(zombies)
                playerCoords = canvas.coords(player)
                playerX1 = zombieCoords[0] - 50
                playerX2 = zombieCoords[0] + 50
                playerY1 = zombieCoords[1] - 20
                playerY2 = zombieCoords[1] + 20
                if zombieCoords[1] > 1080:
                    canvas.delete(zombies)
                    zombieList.remove(zombies)
                    zombieHouse.append(zombies)
                    zombiesInHouse += 1
                    zombieLabel.config(
                        text="Zombies in House: " + str(zombiesInHouse))
                    game.update()

                if playerCoords[0] in range(
                        int(playerX1),
                        int(playerX2)) and playerCoords[1] in range(
                        int(playerY1),
                        int(playerY2)):
                    canvas.create_image(900, 500, image=endGame)
                    returnToMainMenu = Button(
                        game, image=mainmenuimage,
                        bd=0, bg="black", command=reset)
                    returnToMainMenu.place(x=200, y=850)
                    quit = Button(game, image=quitImage, bd=0,
                                  bg="black", command=quitGame)
                    quit.place(x=1520, y=850)
                    global endEntry
                    endEntry = Entry(game)
                    canvas.create_window(960, 800, window=endEntry)
                    endConfirmButton = Button(
                        game,
                        text="Add to Leaderboard",
                        font="Arial, 20",
                        command=leaderBoardConfirm)
                    endConfirmButton.place(x=830, y=820)
                    gameOver = True
                    return
                if zombiesInHouse == 15:
                    canvas.create_image(900, 500, image=endGame)
                    returnToMainMenu = Button(
                        game, image=mainmenuimage,
                        bd=0, bg="black", command=reset)
                    returnToMainMenu.place(x=200, y=850)
                    quit = Button(game, image=quitImage, bd=0,
                                  bg="black", command=quitGame)
                    quit.place(x=1520, y=850)
                    endEntry = Entry(game)
                    canvas.create_window(960, 800, window=endEntry)
                    endConfirmButton = Button(
                        game,
                        text="Add to Leaderboard",
                        font="Arial, 20",
                        command=leaderBoardConfirm)
                    endConfirmButton.place(x=830, y=820)
                    gameOver = True
                    return


# Main menu is called as the program starts.
game.after(1, mainMenu)

game.update()

game.title("Backyard Zombie Slayer")

game.mainloop()
