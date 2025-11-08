/* Copyright (c) 2025 Isaac Ip All rights reserved
 *
 * Created by: Isaac Ip
 * Created on: Nov 2025
 * This program uses the bluetooth radios
*/

// variables
let distanceToObject: number = 0

// setup
radio.setGroup(12)
basic.showIcon(IconNames.Happy)

while (true) {
    distanceToObject = sonar.ping(
        DigitalPin.P0, 
        DigitalPin.P0, 
        PingUnit.Centimeters)
        basic.showNumber(distanceToObject)
        if (distanceToObject <= 10) {
            radio.sendString("Too Close!")
        }
}

radio.onReceivedString(function (receivedString) {
    basic.clearScreen()
    basic.showString(receivedString)
    basic.showIcon(IconNames.Happy)
})
