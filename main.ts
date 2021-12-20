// description in next  lines down
// 
// this project is one of two basic parts of advanced smart server ecosystem this is part one the controller
radio.onReceivedNumber(function (receivedNumber) {
    // concon means connection control
    if (receivedNumber == 1.000000000000141) {
        stopconcon = 1
    }
})
input.onButtonPressed(Button.A, function () {
    if (complete == 5) {
        // stop animation command is used when you wan to interrupt anything on screen and then print another
        led.stopAnimation()
        page += 1
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("getting location")
})
input.onButtonPressed(Button.B, function () {
    if (complete == 5) {
        led.stopAnimation()
        page += -1
    }
})
let page = 0
let concontime = 0
let stopconcon = 0
let complete = 0
// the program sets variables to their base value
complete = 0
radio.setTransmitPower(7)
radio.setGroup(1)
// this is just animation and its not necessari
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . # . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . #
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.showString("Hello!")
basic.showString("smart room")
basic.showString("controller")
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # . . .
    `)
stopconcon = 550
// this is the place when just basic animation is used to tell it you are connected to server by adding third point and deleting it when the connection is false  then the fourth dot load when you are connected to server
while (stopconcon == 550) {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # . . .
        `)
    radio.sendNumber(101100010001110100000)
    basic.pause(2000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # . .
        `)
    // this variable concontime captures how many times the program tried to find server
    concontime += 1
    // now if the concontime value is 10 so its 10. try  of connecting to server this run the restart sequence
    if (concontime == 10) {
        basic.showString("restarting")
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        // this command will restart whole system
        control.reset()
    }
}
// just another animation
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # . . . .
    # # . . .
    # # # # #
    . . . # #
    . . . . #
    `)
basic.showLeds(`
    # # . . .
    # # # . .
    # # # # #
    . . # # #
    . . . # #
    `)
basic.showLeds(`
    # # # . .
    # # # # .
    # # # # #
    . # # # #
    . . # # #
    `)
basic.showLeds(`
    # # # # .
    # # # # .
    # # # # #
    . # # # #
    . # # # #
    `)
basic.showLeds(`
    # # # # #
    # # # # .
    # # # # #
    . # # # #
    # # # # #
    `)
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.showString("complete")
// this will run if you are connected to the server  and on value of 5 it allows other codes to run
complete = 5
// this code will run for ever from up to down but it can be interupted by other events like pressed buttons  radio recieve or more .....
basic.forever(function () {
    // basic logic this will direct   the gui or some sort of gui cause  microbit does contain just primitive sort of gui based on words numbers and simple pictures like emojis or pictograms
    if (page == 0) {
        basic.showString("menu")
    } else if (page == 1) {
        basic.showString("rover:vacuumer")
    } else if (page == 2) {
        basic.showString("weather")
    } else if (page == 3) {
        basic.showString("soon")
    } else if (page == 4) {
        page = 3
    } else if (page == -1) {
        page = 0
    }
})
