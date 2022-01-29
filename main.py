def on_button_pressed_a():
    if Dividendo % Divisore == 0:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(Dividendo)
    basic.show_string(":")
    basic.show_number(Divisore)
    basic.show_string("?")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    if Dividendo % Divisore != 0:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_string("Esatta (A) - non esatta (B)")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Divisore = 0
Dividendo = 0
Dividendo = randint(1, 20)
Divisore += randint(1, 20)