#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 30, 2025
# This program

import ugame
import stage

import constants


def menu_scene():
    # This function is the main game scene
    # Insert the background and ship sprites
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # The size of the background is 10 by 8 tiles, each tile is 16x16 pixels
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    game = stage.Stage(ugame.display, constants.FPS)
    # The layers are the background and the ship
    game.layers = text + [background]
    game.render_block()

    while True:
        # Get button input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            # If the start button is pressed, go to the game scene
            game_scene()


def game_scene():
    # This function is the main game scene
    # Insert the background and ship sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # The size of the background is 10 by 8 tiles, each tile is 16x16 pixels
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # Place the sprite under the location (75, 66) on the screen
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    game = stage.Stage(ugame.display, constants.FPS)
    # The layers are the background and the ship
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    while True:
        # Get button input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw the sprites and update the screen
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    menu_scene()
