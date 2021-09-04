#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------
WIDTH = 200
HEIGHT = 200

gameState = ''


def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState
    
    if key == keys.A:
        gameState = 'initializeStartScreen'
    
    elif key == keys.B:
        gameState = 'initializeGameScreen'
        
        
def update():
    global gameState
    #music.play('handel_mp3')   #This is a bad idea!
    if gameState == 'initializeStartScreen':
        music.play('handel_mp3')    #Play the song over and over
        gameState = 'startScreen'
    if gameState == 'StartScreen':
        pass
    elif gameState == 'initializeGameScreen':
        music.play_once('birthday') #https://freemusicarchive.org/music/Monk_Turner__Fascinoma/The_New_Birthday_Song_Contest/Its_Your_Birthday_1839
        gameState = 'gameScreen'
        
def on_music_end():
    music.play_once('one') #You could make this pick a random song from a list for example
    #https://freemusicarchive.org/music/Doctor_Turtle/5f91e09024ca8/one-person-listening-now


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    if gameState == 'startScreen':
        screen.fill((255, 255, 255))
    #Draw the knight
    