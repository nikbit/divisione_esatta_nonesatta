let Dividendo = 0
let Divisore = 0
input.onButtonPressed(Button.A, function () {
    if (Dividendo % Divisore == 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onGesture(Gesture.Shake, function () {
    Dividendo = randint(1, 20)
    Divisore = randint(1, 20)
    basic.showNumber(Dividendo)
    basic.showString(":")
    basic.showNumber(Divisore)
    basic.showString("?")
})
input.onButtonPressed(Button.B, function () {
    if (Dividendo % Divisore != 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("Esatta=A - non esatta=B")
})
