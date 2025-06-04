#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 30, 2025
# This program

import ugame
import stage


def game_scene():
    # This function is the main game scene

    # Insert the file that is for the background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Set the background image
    # The background is a grid of 10 columns and 8 rows
    background = stage.Grid(image_bank_background, 10, 8)

    # The rate is a 60
    game = stage.Stage(ugame.display, 60)
    # Set the background to the game
    game.layers = [background]
    game.render_block()

    while True:
        pass


if __name__ == "__main__":
    game_scene()
