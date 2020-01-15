.. _game:

****
Game
****

The game scene is where you will build this game, there are many parts you must include but the most important will be the collison between the buttons coming from the top of the screen and the buttons which indicate when to press the designated button. The animation on the left of the screen will not be shown how to create here but in the jungle joe animation section. After setting the background you must first we must make the button locations on the screen show up to know when to press the designated button which is just putting a sprite at a specific location and is shown in the code below. After the sprites are in place and your backgroud is set now we will get sprites to come from top of screen. Since there are six unique sprites and they need to have the same X location as there stationary counterparts that are on screen. 

The most important part of this game is its collision, as any game of this genre has this as there main attraction. The collision is like any other when the two sprites are touching and the designated button is pressed, the moving sprite should be moved to the off screen location. The best part about this game is that there will never be two of the same games as there is a random factor which determines how many more sprites come down and which sprites come down. The code for the collision detection is apart of the game code which will be shown below:

Next we must make the lives and score system, In this game the user has 5 lives (unless playing on endless mode) and the score they can reach is unlimited. Every time the user presses the designated button at the correct time, the user will recieve a point. The code for this is your standard text code that is shown apart of the code below and the score palette is a palette you can use. The lives system is very simple, if a moving sprite reaches the max Y screen size + its sprite size the user will lose a life. The lives will be shown through the neopixels. Instead of putting lives on the screen and making the screen feel cramped, we will be moving the lives count to the neopixals that are at the bottom of the pybadge. The lights on the pybadge will be set to gren at the start of the game and when the user loses a life, one of the lights will turn to red until all are red and user loses the game. The code for the lives system is also shown in the finshed code for the game scene which is below.

Now we will be adding the finshing touches to the game scene, to get everything to load we must render all the sprites, and call the opther functions while taking the final hieght, which is shown in the jungle joe animation section, and the users final score. This is shown in the final code below.

After you have finished with the game scene you may add sounds if you desire, the sounds will mostly relate to jungle joe animation and when you lose the game.
.. toctree::
   def game_scene(game_mode):
    # this function is the game scene
    sprites = []
    number_of_lives = 5
    score = 0
    button_speed = 1
    height = 0
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]
    left_button = constants.button_state["button_up"]
    right_button = constants.button_state["button_up"]

    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_2_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2,3)
            background.tile(x_location, y_location, tile_picked)
    for x_location in range(constants.SCREEN_GRID_2_X, constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 5)

    # Displays key sprites.
    a_button_sprite = stage.Sprite(image_bank_3, 12, constants.A_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(a_button_sprite)
    b_button_sprite = stage.Sprite(image_bank_3, 11, constants.B_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(b_button_sprite)
    left_arrow = stage.Sprite(image_bank_3, 8, constants.LEFT_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(left_arrow)
    right_arrow = stage.Sprite(image_bank_3, 7, constants.RIGHT_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(right_arrow)
    up_arrow = stage.Sprite(image_bank_3, 10, constants.UP_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(up_arrow)
    down_arrow = stage.Sprite(image_bank_3, 9, constants.DOWN_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(down_arrow)

    text = []
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score:{0}".format(score))
    text.append(score_text)

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    for pixel_number in range(0, 5):
        pixels[pixel_number] = (0, 10, 0)
    pixels.show()

    def score_update():
        # I know this is a function that is using variables outside of itself!
        # BUT this code is going to be used in multiple places
        # update the score when you correctly hit a button or when you hit a milestone
        score = score + 1
        # Refreshes score text
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("Score:{0}".format(score))
        game.render_block()

    def show_abutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make a button show up on screen in the x-axis
        for a_button_number in range(len(abutton)):
            if abutton[a_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                abutton[a_button_number].move(constants.A_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    abutton = []
    for a_button_number in range(constants.TOTAL_NUMBER_OF_A_BUTTON):
        a_single_abutton = stage.Sprite(image_bank_3, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        abutton.append(a_single_abutton)

    # current number of buttons that should be moving down screen, start with just 1
    abutton_count = 1
    show_abutton()

    def show_bbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for b_button_number in range(len(bbutton)):
            if bbutton[b_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                bbutton[b_button_number].move(constants.B_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    bbutton = []
    for b_button_number in range(constants.TOTAL_NUMBER_OF_B_BUTTON):
        a_single_bbutton = stage.Sprite(image_bank_3, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        bbutton.append(a_single_bbutton)

    # current number of buttons that should be moving down screen, start with just 1
    bbutton_count = 0
    show_bbutton()

    def show_upbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for up_button_number in range(len(upbutton)):
            if upbutton[up_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                upbutton[up_button_number].move(constants.UP_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    upbutton = []
    for up_button_number in range(constants.TOTAL_NUMBER_OF_UP_BUTTON):
        a_single_upbutton = stage.Sprite(image_bank_3, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        upbutton.append(a_single_upbutton)

    # current number of buttons that should be moving down screen, start with just 1
    upbutton_count = 0
    show_upbutton()

    def show_downbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for down_button_number in range(len(downbutton)):
            if downbutton[down_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                downbutton[down_button_number].move(constants.DOWN_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    downbutton = []
    for down_button_number in range(constants.TOTAL_NUMBER_OF_DOWN_BUTTON):
        a_single_downbutton = stage.Sprite(image_bank_3, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        downbutton.append(a_single_downbutton)

    # current number of buttons that should be moving down screen, start with just 1
    downbutton_count = 0
    show_downbutton()

    def show_leftbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for left_button_number in range(len(leftbutton)):
            if leftbutton[left_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                leftbutton[left_button_number].move(constants.LEFT_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    leftbutton = []
    for left_button_number in range(constants.TOTAL_NUMBER_OF_LEFT_BUTTON):
        a_single_leftbutton = stage.Sprite(image_bank_3, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        leftbutton.append(a_single_leftbutton)

    # current number of buttons that should be moving down screen, start with just 1
    leftbutton_count = 0
    show_leftbutton()

    def show_rightbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for right_button_number in range(len(rightbutton)):
            if rightbutton[right_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                rightbutton[right_button_number].move(constants.RIGHT_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    rightbutton = []
    for right_button_number in range(constants.TOTAL_NUMBER_OF_RIGHT_BUTTON):
        a_single_rightbutton = stage.Sprite(image_bank_3, 1, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        rightbutton.append(a_single_rightbutton)

    # current number of button that should be moving down screen, start with just 1
    rightbutton_count = 0
    show_rightbutton()

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + jungle_joe + logs + border + abutton + bbutton + upbutton + downbutton + leftbutton + rightbutton + sprites + [background]

    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # update game logic
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_UP != 0:
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
        else:
            if up_button == constants.button_state["button_still_pressed"]:
                up_button = constants.button_state["button_released"]
            else:
                up_button = constants.button_state["button_up"]

        if keys & ugame.K_DOWN != 0:
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            elif down_button == constants.button_state["button_just_pressed"]:
                down_button = constants.button_state["button_still_pressed"]
        else:
            if down_button == constants.button_state["button_still_pressed"]:
                down_button = constants.button_state["button_released"]
            else:
                down_button = constants.button_state["button_up"]

        if keys & ugame.K_LEFT != 0:
            if left_button == constants.button_state["button_up"]:
                left_button = constants.button_state["button_just_pressed"]
            elif left_button == constants.button_state["button_just_pressed"]:
                left_button = constants.button_state["button_still_pressed"]
        else:
            if left_button == constants.button_state["button_still_pressed"]:
                left_button = constants.button_state["button_released"]
            else:
                left_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:
            if right_button == constants.button_state["button_up"]:
                right_button = constants.button_state["button_just_pressed"]
            elif right_button == constants.button_state["button_just_pressed"]:
                right_button = constants.button_state["button_still_pressed"]
        else:
            if right_button == constants.button_state["button_still_pressed"]:
                right_button = constants.button_state["button_released"]
            else:
                right_button = constants.button_state["button_up"]

        for a_button_number in range(len(abutton)):
            if abutton_count > 0:
                if abutton[a_button_number].x > 0: # meaning it is on the screen
                    abutton[a_button_number].move(abutton[a_button_number].x, abutton[a_button_number].y + button_speed)
                    if abutton[a_button_number].y > constants.SCREEN_Y:
                        abutton[a_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_abutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for b_button_number in range(len(bbutton)):
            if bbutton_count > 0:
                if bbutton[b_button_number].x > 0: # meaning it is on the screen
                    bbutton[b_button_number].move(bbutton[b_button_number].x, bbutton[b_button_number].y + button_speed)
                    if bbutton[b_button_number].y > constants.SCREEN_Y:
                        bbutton[b_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_bbutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for up_button_number in range(len(upbutton)):
            if upbutton_count > 0:
                if upbutton[up_button_number].x > 0: # meaning it is on the screen
                    upbutton[up_button_number].move(upbutton[up_button_number].x, upbutton[up_button_number].y + button_speed)
                    if upbutton[up_button_number].y > constants.SCREEN_Y:
                        upbutton[up_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_upbutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for down_button_number in range(len(downbutton)):
            if downbutton_count > 0:
                if downbutton[down_button_number].x > 0: # meaning it is on the screen
                    downbutton[down_button_number].move(downbutton[down_button_number].x, downbutton[down_button_number].y + button_speed)
                    if downbutton[down_button_number].y > constants.SCREEN_Y:
                        downbutton[down_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_downbutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for left_button_number in range(len(leftbutton)):
            if leftbutton_count > 0:
                if leftbutton[left_button_number].x > 0: # meaning it is on the screen
                    leftbutton[left_button_number].move(leftbutton[left_button_number].x, leftbutton[left_button_number].y + button_speed)
                    if leftbutton[left_button_number].y > constants.SCREEN_Y:
                        leftbutton[left_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_leftbutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for right_button_number in range(len(rightbutton)):
            if rightbutton_count > 0:
                if rightbutton[right_button_number].x > 0: # meaning it is on the screen
                    rightbutton[right_button_number].move(rightbutton[right_button_number].x, rightbutton[right_button_number].y + button_speed)
                    if rightbutton[right_button_number].y > constants.SCREEN_Y:
                        rightbutton[right_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_rightbutton() # make it randomly show up at top again
                        if game_mode == 0:
                            number_of_lives = number_of_lives - 1

        for a_button_number in range(len(abutton)):
            if abutton[a_button_number].x > 0 and a_button == constants.button_state["button_just_pressed"]:
                if stage.collide(abutton[a_button_number].x, abutton[a_button_number].y,
                                     abutton[a_button_number].x, abutton[a_button_number].y + 7,
                                     a_button_sprite.x, a_button_sprite.y,
                                     a_button_sprite.x, a_button_sprite.y + 7):
                        # when you press designated button when it is on top of sprite
                    abutton[a_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    abutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_abutton()

        for b_button_number in range(len(bbutton)):
            if bbutton[b_button_number].x > 0 and b_button == constants.button_state["button_just_pressed"]:
                if stage.collide(bbutton[b_button_number].x, bbutton[b_button_number].y,
                                     bbutton[b_button_number].x, bbutton[b_button_number].y + 7,
                                     b_button_sprite.x, b_button_sprite.y,
                                     b_button_sprite.x, b_button_sprite.y + 7):
                        # when you press designated button when it is on top of sprite
                    bbutton[b_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    bbutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_bbutton()

        for up_button_number in range(len(upbutton)):
            if upbutton[up_button_number].x > 0 and up_button == constants.button_state["button_just_pressed"]:
                if stage.collide(upbutton[up_button_number].x, upbutton[up_button_number].y,
                                     upbutton[up_button_number].x, upbutton[up_button_number].y + 7,
                                     up_arrow.x, up_arrow.y,
                                     up_arrow.x, up_arrow.y + 7):
                        # when you press designated button when it is on top of sprite
                    upbutton[up_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    upbutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_upbutton()

        for down_button_number in range(len(downbutton)):
            if downbutton[down_button_number].x > 0 and down_button == constants.button_state["button_just_pressed"]:
                if stage.collide(downbutton[down_button_number].x, downbutton[down_button_number].y,
                                     downbutton[down_button_number].x, downbutton[down_button_number].y + 7,
                                     down_arrow.x, down_arrow.y,
                                     down_arrow.x, down_arrow.y + 7):
                        # when you press designated button when it is on top of sprite
                    downbutton[down_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    downbutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_downbutton()

        for left_button_number in range(len(leftbutton)):
            if leftbutton[left_button_number].x > 0 and left_button == constants.button_state["button_just_pressed"]:
                if stage.collide(leftbutton[left_button_number].x, leftbutton[left_button_number].y,
                                 leftbutton[left_button_number].x, leftbutton[left_button_number].y + 7,
                                 left_arrow.x, left_arrow.y,
                                 left_arrow.x, left_arrow.y + 7):
                        # when you press designated button when it is on top of sprite
                    leftbutton[left_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    leftbutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_leftbutton()

        for right_button_number in range(len(rightbutton)):
            if rightbutton[right_button_number].x > 0 and right_button == constants.button_state["button_just_pressed"]:
                if stage.collide(rightbutton[right_button_number].x, rightbutton[right_button_number].y,
                                 rightbutton[right_button_number].x, rightbutton[right_button_number].y + 7,
                                 right_arrow.x, right_arrow.y,
                                 right_arrow.x, right_arrow.y + 7):
                        # when you press designated button when it is on top of sprite
                    rightbutton[right_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score_update()
                    rightbutton_count = 0
                    rand_amount_number = random.randint(1, 2)
                    for loop_counter in range(rand_amount_number):
                        random_selection = random.randint(1, 6)
                        if random_selection == 1:
                            abutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 2:
                            bbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 3:
                            upbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 4:
                            downbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 5:
                            leftbutton_count = 1
                            loop_counter = loop_counter + 1
                        elif random_selection == 6:
                            rightbutton_count = 1
                            loop_counter = loop_counter + 1
                    show_rightbutton()

        if number_of_lives == 5:
            for pixel_number in range(0, 5):
                    pixels[pixel_number] = (0, 10, 0)
                    pixels.show()
        if number_of_lives == 4:
            for pixel_number in range(1):
                    pixels[pixel_number] = (25, 0, 0)
                    pixels.show()
        if number_of_lives == 3:
            for pixel_number in range(2):
                    pixels[pixel_number] = (25, 0, 0)
                    pixels.show()
        if number_of_lives == 2:
            for pixel_number in range(3):
                    pixels[pixel_number] = (25, 0, 0)
                    pixels.show()
        if number_of_lives == 1:
            for pixel_number in range(4):
                    pixels[pixel_number] = (25, 0, 0)
                    pixels.show()
        if number_of_lives == 0:
            for pixel_number in range(5):
                    pixels[pixel_number] = (25, 0, 0)
                    pixels.show()
                    game_over_scene(score, height)

        # redraw sprite list
        game.render_sprites(logs + sprites + jungle_joe + abutton + bbutton + upbutton + downbutton + leftbutton + rightbutton)
        game.tick()  # wait until refresh rate finishes
        
.. toctree::
   :maxdepth: 1
   :glob:

   Background <background>
   Jungle JOe <jungle_joe>

