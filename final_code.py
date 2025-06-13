#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 30, 2025
# This program

import ugame
import stage
import time
import random
import supervisor

import constants


def instructions_scene():
    # Use the background and sprites from the image bank
    image_bank = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(20, 20)
    text1.text("Instructions:")
    text.append(text1)

    text2 = stage.Text(width=25, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(8, 40)
    text2.text("Get 7 points to win!")
    text.append(text2)

    text3 = stage.Text(width=25, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(15, 60)
    text3.text("Press A to begin")
    text.append(text3)
    # Control the display refresh rate
    game = stage.Stage(ugame.display, constants.FPS)
    # Text above the background
    game.layers = text + [background]
    # Show all the layers on the screen
    game.render_block()
    # While loop to keep the scene running
    while True:
        # Check which button is pressed
        keys = ugame.buttons.get_pressed()
        # If the A button is pressed, go to the menu scene
        if keys & ugame.K_X != 0:
            menu_scene()
        # Update the game and refresh the screen
        game.tick()


def win_scene(final_score):
    # Load the win sound, open it, and play it
    # rb means read binary, so it can be played
    win_music = open("win.wav", "rb")
    # Sound system from Ugame
    sound = ugame.audio
    # Stop any sound that is currently playing
    sound.stop()
    # Make sure sound is not muted
    sound.mute(False)
    # Play the win sound
    sound.play(win_music)
    # Load the background layout use for the win screen under the following file
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # Set the background grid to the image bank, contain the image
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # Create a list to show the text on the screen
    text = []
    # The first text box and 
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    # Move the text to this position on the screen
    text1.move(40, 60)
    # Showing you win message
    text1.text("YOU WIN!")
    # Add the text to the list so it can be displayed
    text.append(text1)
    # Make sure the scene is displayed and for 3 seconds
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    time.sleep(3.0)
    # Stop the sound
    sound.stop()
    # Go to game over scene
    game_over_scene(final_score)

def game_over_scene(final_score):
    # This function is the game over scene
    # Turn off sound from last scene
    sound = ugame.audio
    sound.stop()
    # image banks for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16 ("mt_game_studio.bmp")
    # Sets the background to image 0 in the image bank
    # Add text objects
    background = stage.Grid (image_bank_2, constants.SCREEN_GRID_X,
                             constants.SCREEN_GRID_Y)
    text = []
    text1= stage.Text (width=29, height=14, font=None, palette = constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text (width=29, height=14, font=None, palette = constants.BLUE_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette = constants.BLUE_PALETTE, buffer = None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    game = stage.Stage (ugame.display, constants. FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()  # reloads the program

        game.tick()
# This game is the splash scene


def splash_scene():
    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # used this program to split the image into tile:

    image_bank = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

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

    game = stage.Stage(ugame.display, constants.FPS)
    # The layers are the background and the ship
    game.layers = [background]
    game.render_block()

    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        instructions_scene()


def menu_scene():
    # This function is the main game scene
    # Insert the background and ship sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

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

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

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

    # For score
    score = 5
    # For lives
    lives = 3
    # Sound is on
    mute = False
    # Create a Text object to display the score on screen
    score_text = stage.Text (width=29, height=14)
    # Clear all existed text
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))

    lives_text = stage.Text(width=29, height=14)
    lives_text.clear()
    lives_text.cursor(0, 0)
    lives_text.move(90, 1)
    lives_text.text("Lives: {0}".format(lives))

    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        # Loops through all aliens.
        for alien_number in range(len(aliens)):
            # If the alien is off screen, move it on screen
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                             constants.SCREEN_X - constants.SPRITE_SIZE),
                                                             constants.OFF_TOP_SCREEN)
                break

    # Insert the background and ship sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    pew_sound = open("pew.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    crash_sound = open("crash.wav", "rb")

    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # The size of the background is 10 by 8 tiles, each tile is 16x16 pixels
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    # Place the sprite under the location (75, 66) on the screen
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # Place one alien on the screen
    show_alien()

    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    game = stage.Stage(ugame.display, constants.FPS)
    # The layers are the background and the ship
    game.layers = [score_text] + [lives_text] + lasers + [ship] + aliens + [background]
    game.render_block()

    speed_fast = False
    # Track DOWN button
    down_button = constants.button_state["button_up"]
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


        # Checks if the right button is currently being pressed.
        if keys & ugame.K_RIGHT != 0:
            # The new x position of the ship
            # Current x position of the ship plus the current speed
            new_x = ship.x + current_speed
            # If new position is off the screen to the right
            if new_x > (constants.SCREEN_X - constants.SPRITE_SIZE):
                # Reset it to the left edge of the screen
                new_x = 0  # wrap around to left edge
            # Move the ship to the new position
            ship.move(new_x, ship.y)

        if keys & ugame.K_LEFT != 0:
            new_x = ship.x - current_speed
            if new_x < 0:
                new_x = constants.SCREEN_X - constants.SPRITE_SIZE  # wrap around to right edge
            ship.move(new_x, ship.y)
        # Checks if the UP button is currently being pressed.
        if keys & ugame.K_UP != 0:
            # If not been pressed, change the button state to just pressed.
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            # If button been pressed
            elif up_button == constants.button_state["button_just_pressed"]:
                # Change the button state to still pressed.
                up_button = constants.button_state["button_still_pressed"]
        # If the button is not pressed
        else:
            # Check if the button is still pressed
            if up_button == constants.button_state["button_still_pressed"]:
                # change the button state to released
                up_button = constants.button_state["button_released"]
            # If botton is not down
            else:
                # Change the button state to up
                up_button = constants.button_state["button_up"]
        # If the UP button is just pressed
        if up_button == constants.button_state["button_just_pressed"]:
            # The opposite of current mute state
            mute = not mute
            # Tells the program to mute or unmute the sound
            sound.mute(mute)
        # If down button is pressed
        if keys & ugame.K_DOWN != 0:
            # If the button is not pressed, change the button state to just pressed.
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            # If the button is already pressed
            elif down_button == constants.button_state["button_just_pressed"]:
                # Change the button state to still pressed.
                down_button = constants.button_state["button_still_pressed"]
        # If the button is not currently pressed
        else:
            # If the button is still pressed before, change the button state to released
            if down_button == constants.button_state["button_still_pressed"]:
                # Change the button state to released
                down_button = constants.button_state["button_released"]
            # If the button is not pressed
            else:
                # Not in any movement
                down_button = constants.button_state["button_up"]
        # If the down button is just pressed
        if down_button == constants.button_state["button_just_pressed"]:
            # Opposite of current speed_fast state
            speed_fast = not speed_fast
        # If the speed_fast is True, then the current speed is 3 times the normal speed
        if speed_fast:
            current_speed = constants.SPRITE_MOVEMENT_SPEED * 3
        # If the speed_fast is False, then the current speed is the normal speed
        else:
            current_speed = constants.SPRITE_MOVEMENT_SPEED

        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED
                )

                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y
                    )

        # Each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                           aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    if score >= 7:
                        win_scene(score)

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide (lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                          lasers[laser_number].x + 11, lasers[laser_number].y + 12, 
                                          aliens[alien_number].x + 1, aliens[alien_number].y,
                                          aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants. OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
        # Loop which do the following, inside the aliens list:
        for alien_number in range(len(aliens)):
            # If the alien is on the screen, for the collision to happen
            if aliens[alien_number].x > 0:
                # Built-in function to detect collision between two rectangular sprites.
                if stage.collide (aliens[alien_number].x + 1, aliens[alien_number].y,
                                  aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                  ship.x, ship.y,
                                  ship.x + 15, ship.y +15):
                                  #alien hit the ship
                                 # If the alien hit the ship, stop the sound
                                 sound.stop()
                                 # Play the crash sound instead
                                 sound.play(crash_sound)
                                 # Decrease the value of lives by 1
                                 lives -= 1
                                 # Remove the previous text in order to update the text
                                 lives_text.clear()
                                 # the cursor is the top left corner of the text
                                 lives_text.cursor(0, 0)
                                 # Move the text to x = 90, y = 1
                                 lives_text.move(90, 1)
                                 # Print the number of lives left on the screen
                                 lives_text.text("Lives: {0}".format(lives))
                                 # Check if lives are 0 or below, meaning game over.
                                 if lives <= 0:
                                     # Hold for 3 second to read
                                     time.sleep(3.0)
                                     # Go to the game over scene
                                     game_over_scene(score)
                                # Still has lives
                                 else:
                                     # Hold for 1 second to read
                                     time.sleep(1.0)
                                     # The ship moves back to where it shoot the aliens
                                     ship.move(75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))


        # Redraw the sprites and update the screen
        game.render_sprites(aliens + lasers + [ship])
        game.tick()


if __name__ == "__main__":
    splash_scene()