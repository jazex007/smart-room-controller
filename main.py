# description in next  lines down
# 
# this project is one of two basic parts of advanced smart server ecosystem this is part one the controller

def on_received_number(receivedNumber):
    global stopconcon
    # concon means connection control
    if receivedNumber == 1.000000000000141:
        stopconcon = 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global page
    if complete == 5:
        # stop animation command is used when you wan to interrupt anything on screen and then print another
        led.stop_animation()
        page += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("getting location")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global page
    if complete == 5:
        led.stop_animation()
        page += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

page = 0
concontime = 0
stopconcon = 0
complete = 0
# the program sets variables to their base value
complete = 0
radio.set_transmit_power(7)
radio.set_group(1)
# this is just animation and its not necessari
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . # . . .
        # . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . # . . .
        # . . . .
""")
basic.show_leds("""
    . . . . .
        . . . # .
        . . # . .
        . # . . .
        # . . . .
""")
basic.show_leds("""
    . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
""")
basic.show_string("Hello!")
basic.show_string("smart room")
basic.show_string("controller")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # . . .
""")
stopconcon = 550
# this is the place when just basic animation is used to tell it you are connected to server by adding third point and deleting it when the connection is false  then the fourth dot load when you are connected to server
while stopconcon == 550:
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # . . .
    """)
    radio.send_number(101100010001110100000)
    basic.pause(2000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # . .
    """)
    # this variable concontime captures how many times the program tried to find server
    concontime += 1
    # now if the concontime value is 10 so its 10. try  of connecting to server this run the restart sequence
    if concontime == 10:
        basic.show_string("restarting")
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """)
        # this command will restart whole system
        control.reset()
# just another animation
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
""")
basic.show_leds("""
    # . . . .
        # # . . .
        # # # # #
        . . . # #
        . . . . #
""")
basic.show_leds("""
    # # . . .
        # # # . .
        # # # # #
        . . # # #
        . . . # #
""")
basic.show_leds("""
    # # # . .
        # # # # .
        # # # # #
        . # # # #
        . . # # #
""")
basic.show_leds("""
    # # # # .
        # # # # .
        # # # # #
        . # # # #
        . # # # #
""")
basic.show_leds("""
    # # # # #
        # # # # .
        # # # # #
        . # # # #
        # # # # #
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.show_string("complete")
# this will run if you are connected to the server  and on value of 5 it allows other codes to run
complete = 5
# this code will run for ever from up to down but it can be interupted by other events like pressed buttons  radio recieve or more .....

def on_forever():
    global page
    # basic logic this will direct   the gui or some sort of gui cause  microbit does contain just primitive sort of gui based on words numbers and simple pictures like emojis or pictograms
    if page == 0:
        basic.show_string("menu")
    elif page == 1:
        basic.show_string("rover:vacuumer")
    elif page == 2:
        basic.show_string("weather")
    elif page == 3:
        basic.show_string("soon")
    elif page == 4:
        page = 3
    elif page == -1:
        page = 0
basic.forever(on_forever)
