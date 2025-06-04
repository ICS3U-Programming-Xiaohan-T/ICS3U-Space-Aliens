#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 30, 2025
# This program added the ship to the game scene

import ugame
import stage


def game_scene():
    # This function is the main game scene
    # Insert the background and ship sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # The size of the backgound is 10 by 8 tiles, each tile is 16x16 pixels
    background = stage.Grid(image_bank_background, 10, 8)
    # Place the sprite under the location (75, 66) on the screen
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, 66
    )  # Assuming sprite index 5 is the ship
    # Refresh the display
    game = stage.Stage(ugame.display, 60)
    # The layers are the background and the ship
    game.layers = [ship] + [background]
    game.render_block()

    while True:
        # This section is the loop
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
