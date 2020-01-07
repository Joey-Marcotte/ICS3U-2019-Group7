#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This file is the "Jungle Joe and Snakob" game
# for CircuitPython

import ugame
import stage
import board
# import neopixel
import time
import random

import constants


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    # pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    # pixels.deinit() # and turn them all off

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(1.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the game scene
    text = []
    sprites = []

    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")
    image_bank_4 = stage.Bank.from_bmp16("elemental_studios.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(13, 60)
    text_1.text("ELEMENTAL STUDIOS")
    text.append(text_1)

    fire_upper_right = stage.Sprite(image_bank_4, 0, 16, 0)
    sprites.append(fire_upper_right)
    fire_bottom_right = stage.Sprite(image_bank_4, 1, 16, 16)
    sprites.append(fire_bottom_right)
    fire_upper_left = stage.Sprite(image_bank_4, 2, 0, 0)
    sprites.append(fire_upper_left)
    fire_bottom_left = stage.Sprite(image_bank_4, 3, 0, 16)
    sprites.append(fire_bottom_left)

    water_upper_right = stage.Sprite(image_bank_4, 6, 144, 0)
    sprites.append(water_upper_right)
    water_bottom_right = stage.Sprite(image_bank_4, 7, 144, 16)
    sprites.append(water_bottom_right)
    water_upper_left = stage.Sprite(image_bank_4, 4, 128, 0)
    sprites.append(water_upper_left)
    water_bottom_left = stage.Sprite(image_bank_4, 5, 128, 16)
    sprites.append(water_bottom_left)

    earth_upper_right = stage.Sprite(image_bank_4, 10, 16, 98)
    sprites.append(earth_upper_right)
    earth_bottom_right = stage.Sprite(image_bank_4, 11, 16, 112)
    sprites.append(earth_bottom_right)
    earth_upper_left = stage.Sprite(image_bank_4, 8, 0, 98)
    sprites.append(earth_upper_left)
    earth_bottom_left = stage.Sprite(image_bank_4, 9, 0, 112)
    sprites.append(earth_bottom_left)

    wind_upper_right = stage.Sprite(image_bank_4, 14, 144, 98)
    sprites.append(wind_upper_right)
    wind_bottom_right = stage.Sprite(image_bank_4, 15, 144, 112)
    sprites.append(wind_bottom_right)
    wind_upper_left = stage.Sprite(image_bank_4, 12, 128, 98)
    sprites.append(wind_upper_left)
    wind_bottom_left = stage.Sprite(image_bank_4, 13, 128, 112)
    sprites.append(wind_bottom_left)

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        time.sleep(1.0)
        main_menu_scene()
        # redraw sprite list
        pass # just a placeholder until you write the code


def main_menu_scene():
    # this function is the main menu scene
    text = []

    image_bank_5 = stage.Bank.from_bmp16("Backgrounds.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    background.tile(2, 8, 1)
    background.tile(2, 8, 2)
    background.tile(2, 8, 3)
    background.tile(2, 8, 4)
    background.tile(2, 8, 5)
    background.tile(2, 8, 6)
    background.tile(2, 8, 7)
    background.tile(2, 8, 8)
    background.tile(2, 8, 9)
    background.tile(2, 8, 10)
    
    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(40, 35)
    text_1.text("JUNGLE JOE")
    text.append(text_1)

    text_2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_2.move(40, 45)
    text_2.text("& SNAKOB'S")
    text.append(text_2)

    text_3 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_3.move(25, 55)
    text_3.text("BONGO BANANZA!")
    text.append(text_3)
    
    text_4 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_4.move(35, 118)
    text_4.text("PRESS START!")
    text.append(text_4)

    clouds = []
    for cloud_number in range(constants.TOTAL_CLOUDS):
        a_single_cloud = stage.Sprite(image_bank_5, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        clouds.append(a_single_cloud)

    def Show_clouds():
        for cloud_number in range(len(clouds)):
            if clouds[cloud_number].x < 20:
                clouds[cloud_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_Y - constants.SPRITE_SIZE), constants.OFF_LEFT_SCREEN)
                break

    cloud_count = 6
    Show_clouds()
    Show_clouds()

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + clouds + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
    
        # update game logic
        for cloud_number in range (len(clouds)):
            if clouds[cloud_number].y > 0:
                clouds[cloud_number].move(clouds[cloud_number].x,
                                          + constants.CLOUD_SPEED,
                                          clouds[cloud_number].y)
                if clouds[cloud_number].x > constants.SCREEN_X:
                    clouds[cloud_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    Show_clouds()
                if clouds[cloud_number].x > constants.SCREEN_X/2:
                    Show_clouds()
        # redraw sprite list
        pass # just a placeholder until you write the code


def game_scene():
    # this function is the game scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":
    blank_white_reset_scene()
    # blank_white_reset_scene()
