## 🔴🟢 Red light Green light game, using MicroPython and a Raspberry Pi Pico.

This is a game based on the red light green ligth concept using a Raspberry Pi Pico, Breadboard, Button, LEDs, Jump Wires and a Speaker.

---

### Features
- Simple and clean object-oriented design.
- Red/Green LED toggle on random second intervals.
- Yellow LED toggles on button press by user.
- Sound on toggle between red and green LED, victory and elimination
- Victory after 20 steps taken
- Elimination if the yellow and green LEDs are active simultaneously

---

### How to play

- 🏁 When the game starts, the Thonny console will display a message indicating the game is about to begin.
- 🔴 Red Light: Press the button twice during red light to register one step forward.
- 🟢 Green Light: Pressing the button during green light is not allowed — doing so results in elimination.
- ⏲️ The red and green lights toggle randomly every 1 to 5 seconds, keeping you in suspense about when it’s safe to move.
- 🏆 The player requires 20 steps for victory.

### Hardware requirements

- 1x Raspberry Pi Pico.
- 1x Breadboard.
- 1x Button.
- 3x LEDs (red, green and yellow).
- 1x Speaker.
- 12 Jump Wire cables.

|Component|GPIO Pin|  
|---------|--------|
|Button|15|
|Red LED|14|
|Green LED|13|
|Yellow LED|12|
|Speaker|11|

## Getting started

1. Install Thonny IDE.
2. Clone repository and add the files to the Raspberry Pi Pico storage.
3. Attach Raspberry Pi Pico, components and jump wires to breadboard.
4. Run main.py script
