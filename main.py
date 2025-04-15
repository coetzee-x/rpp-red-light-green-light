class RedLightGreenLightGame:

    def __init__(self):
        from picozero import Button, LED, Speaker
        from time import sleep
        import random
        
        self.button = Button(15)
        self.led_red = LED(14)
        self.led_green = LED(13)
        self.led_yellow = LED(12)
        self.speaker = Speaker(11)

        self.sleep = sleep
        self.random = random
        
    def set_defaults(self):
        self.led_red.off()
        self.led_green.off()
        self.led_yellow.off()
        self.game_over = False
        self.total_steps = 0
        self.steps_to_win = 20
        self.button.when_pressed = None

    def is_game_over(self):
        if self.led_green.is_active and self.led_yellow.is_active:
            self.game_over = True
            print("Gotcha! You have been eliminated.")
            for freq in [440, 220]:
                self.speaker.play(freq, 0.3, 1, 1, True)
            self.button.when_pressed = None
            return True
        return False
    
    def is_victory(self):
        if self.total_steps >= self.steps_to_win:
            self.game_over = True
            print(f"Victory! You have made it to the end.")
            for freq in [523, 659, 784]:
                self.speaker.play(freq, 0.2, 1, 1, True)
            self.button.when_pressed = None
            return True
        return False
    
    def do_step(self):
        self.led_yellow.toggle()
        if self.is_game_over() or self.is_victory():return
        if not self.led_yellow.is_active:
            self.total_steps += 1
            print(f"Total Steps: {self.total_steps}")
            self.is_victory()
            
    def game_loop(self):
        print(f"The game is about to start. You require {self.steps_to_win} steps. Good luck!")
        self.sleep(3)
        self.button.when_pressed = self.do_step
        self.led_red.on()
        while not self.game_over:
            if self.is_victory():break
            if self.is_game_over():break
            if self.led_red.is_active:
                print("RED light!")
                self.speaker.play(440, 0.3, 1, 1, False)
            elif self.led_green.is_active:
                print("GREEN light!")
                self.speaker.play(60, 0.3, 1, 1, False)
            sleep_value = self.random.randint(1, 6)
            self.sleep(sleep_value)
            self.led_red.toggle()
            self.led_green.toggle()
        self.sleep(3)

    def start(self):
        while True:
            self.set_defaults()
            self.game_loop()
            
game = RedLightGreenLightGame()
game.start()
