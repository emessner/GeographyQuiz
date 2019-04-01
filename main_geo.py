import pygame as pg
import random
from settings_geo import *
import time
from os import path

class Game():
    
    def __init__(self):
        # Initializing the game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(NAME)
        self.clock = pg.time.Clock()
        self.clock.tick(FPS)
        self.running = True
        self.playing = True
        self.font_name = pg.font.match_font(FONT)
        self.score = 0
        self.count = 0
        self.farbe = []
        self.x_pos = []
        self.y_pos = []
        for i in range(ANZAHL):
            red = random.randint(0,255)
            green = random.randint(0, 255)
            blue = random.randint(0,255)
            self.farbe.append((red, green, blue))
            x = random.randint(0,900)
            self.x_pos.append(x)
            y = random.randint(-600,0)
            self.y_pos.append(y)
        self.load_data()
        self.get_flags()
        
    def load_data(self):
        # Loading Files like Highscore, Sprites, Sounds
        self.dir = path.dirname(__file__)
        self.bgimage = pg.image.load(path.join(self.dir, BG_IMG)).convert_alpha()
        self.flags_spritesheet = pg.image.load(path.join(self.dir, FLAGS)).convert()
        with open (path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
                
        # Load Sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.point_collect = pg.mixer.Sound(path.join(self.snd_dir, 'Pickup_Coin17.ogg'))
        self.wrong = pg.mixer.Sound(path.join(self.snd_dir, 'failed.ogg'))
        
    def get_flags(self):
        self.flag_list = []
        width = 232
        height = 156
        x_diff = 53
        y_diff = 77
        for row in range(15):
            if row == 0:
                y = 85
            else:
                y += y_diff+height
            for col in range(14):
                if col == 0:
                    x =95
                else:
                    x += x_diff + width
                flag = pg.Surface((width, height))
                flag.blit(self.flags_spritesheet, (0, 0), (x, y, width, height))
                flag = pg.transform.scale(flag, (width//2, height//2))
                self.flag_list.append(flag)


    def countdown(self, start):
        self.total_seconds = (TIME - start)
        if self.total_seconds < 0:
            self.total_seconds = 0
        self.minutes = int(self.total_seconds // 60)
        self.seconds = int(self.total_seconds % 60)

        
    def new(self):
        # Start a new game
        self.score = 0
        self.count = 0
        self.record = 0
        self.asked_questions = []
        self.t0 = time.time()
        self.run()
    
    def run(self):
        # Game Loop  
        self.playing = True
        while self.playing:
            self.draw()
            self.update()
            self.events()

    
    def update(self):
        # Game Loop - Update
        # Game Loop draw
        if self.dt >= 60:
            self.playing = False
            self.time_up_screen()
        
        answer = self.wait_for_event()
        if isinstance(answer, int) and (answer == 1 or answer == 2 or answer == 3):   
            answer -= 1
            if answer == self.antworten.index(self.antwort1):
                self.score += 1
                self.point_collect.play()
            else:
                self.wrong.play()
                self.false_screen()
        self.count += 1

            
    def events(self):
        # Game Loops - Event
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False                
                self.running = False

              
    def draw(self):
        
        zufall = random.choice([0, 1])
        if zufall == 0:
            self.frage = random.choice(COUNTRY)
            
            while self.frage in self.asked_questions:
                self.frage = random.choice(COUNTRY)
            
            self.asked_questions.append(self.frage)
                
            stelle_antwort = COUNTRY.index(self.frage)
            self.antwort1 = CAPITAL[stelle_antwort]        
            
            self.antwort2 = random.choice(CAPITAL)
            if self.antwort2 == self.antwort1:
                self.antwort2 = random.choice(CAPITAL)
                
            
            self.antwort3 = random.choice(CAPITAL)
            if self.antwort3 == self.antwort1 or self.antwort3 == self.antwort2:
                self.antwort3 = random.choice(CAPITAL)
            
            self.antworten = [self.antwort1, self.antwort2, self.antwort3]
            random.shuffle(self.antworten)
            
            self.screen.blit(self.bgimage, BG_POS)
    
            self.t1 = time.time()
            self.dt = self.t1 - self.t0
            self.countdown(self.dt)
            pg.draw.rect(self.screen, GREY, [WIDTH/11, 25, 100, 20])
            self.draw_text("Score: {}/{}".format(self.score, self.count), 22, RED, WIDTH/2, 20)
            self.draw_text("Time: {0:02}:{1:02}".format(self.minutes, self.seconds), 22, RED, WIDTH/7, 20)
            self.draw_text("What is the capital of {}?".format(self.frage), 36, RED, WIDTH/2, HEIGHT/2 - 50)        
            self.draw_text("1) {}".format(self.antworten[0]), 28, RED, WIDTH/2, HEIGHT/2)
            self.draw_text("2) {}".format(self.antworten[1]), 28, RED, WIDTH/2, HEIGHT/2 + 30)
            self.draw_text("3) {}".format(self.antworten[2]), 28, RED, WIDTH/2, HEIGHT/2 + 60)        
        else:
            self.frage = random.choice(self.flag_list)
            self.frage.set_colorkey(BG_FLAG)
            
            while self.frage in self.asked_questions:
                self.frage = random.choice(self.flag_list)
            
            self.asked_questions.append(self.frage)
                
            stelle_antwort = self.flag_list.index(self.frage)
            self.antwort1 = COUNTRY_FLAGS[stelle_antwort]        
            
            self.antwort2 = random.choice(COUNTRY_FLAGS)
            if self.antwort2 == self.antwort1:
                self.antwort2 = random.choice(COUNTRY_FLAGS)
                
            
            self.antwort3 = random.choice(COUNTRY_FLAGS)
            if self.antwort3 == self.antwort1 or self.antwort3 == self.antwort2:
                self.antwort3 = random.choice(COUNTRY_FLAGS)
            
            self.antworten = [self.antwort1, self.antwort2, self.antwort3]
            random.shuffle(self.antworten)
            
            self.screen.blit(self.bgimage, BG_POS)
    
            self.t1 = time.time()
            self.dt = self.t1 - self.t0
            self.countdown(self.dt)
            pg.draw.rect(self.screen, GREY, [WIDTH/11, 25, 100, 20])
            self.draw_text("Score: {}/{}".format(self.score, self.count), 22, RED, WIDTH/2, 20)
            self.draw_text("Time: {0:02}:{1:02}".format(self.minutes, self.seconds), 22, RED, WIDTH/7, 20)
            self.draw_text("To which country belongs this flag: ", 36, RED, WIDTH/2, HEIGHT/2 - 50)        
            self.screen.blit(self.frage, (WIDTH/4*3, HEIGHT/2 - 65))
            self.draw_text("1) {}".format(self.antworten[0]), 28, RED, WIDTH/2, HEIGHT/2)
            self.draw_text("2) {}".format(self.antworten[1]), 28, RED, WIDTH/2, HEIGHT/2 + 30)
            self.draw_text("3) {}".format(self.antworten[2]), 28, RED, WIDTH/2, HEIGHT/2 + 60) 

        # After drawing everything flip the screen
        pg.display.flip()
        
    
    def false_screen(self):
        # Show screen with correct answer when false
        self.screen.blit(self.bgimage, BG_POS)
        self.draw_text("Your answer is not correct", 28, RED, WIDTH/2, HEIGHT/2)
        self.draw_text("The correct answer is "+self.antwort1, 28, RED, WIDTH/2, HEIGHT/2 + 30)
        pg.display.flip()
        self.wait_for_key()
        
    def time_up_screen(self):
        # Show screen with correct answer when false
        self.screen.blit(self.bgimage, BG_POS)
        self.draw_text_bold("Your time is up!", 40, RED, WIDTH/2, HEIGHT*1/4)
        self.draw_text("You answered {} of {} questions correctly".format(self.score, self.count), 34, RED, WIDTH/2, HEIGHT/2 + 30)
        self.draw_text("To play another round press ENTER", 28, RED, WIDTH/2, HEIGHT*3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text_bold("Congraulations!! New Highscore: "+str(self.highscore), 34, RED, WIDTH/2, HEIGHT/2)
            with open (path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
            self.record = 1
        else:
            self.draw_text("HIGHSCORE: "+str(self.highscore), 22, RED, WIDTH/2, HEIGHT/2)
        pg.display.flip()        
        self.wait_for_key()
    
    def show_start_screen(self):
        # Show Start Screen with introduction
        self.screen.blit(self.bgimage, BG_POS)
        self.draw_text(NAME, 48, RED, WIDTH/2, HEIGHT/3)
        self.draw_text("Use the keys 1, 2 or 3 to enter your answer", 30, RED, WIDTH/2, HEIGHT/3+60)
        self.draw_text("Press key to play", 22, RED, WIDTH/2, HEIGHT-60)
        self.draw_text("HIGHSCORE: "+str(self.highscore), 22, RED, WIDTH/2, 40)
        pg.display.flip()
        self.wait_for_start_key()
    
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
        
    def draw_text_bold(self, text, size, color, x, y):
        font = pg.font.SysFont(self.font_name, size, bold = True)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def confetti(self):
        for j in range(ANZAHL):
            self.y_pos[j] += 2
            pg.draw.ellipse(self.screen, self.farbe[j],[self.x_pos[j], self.y_pos[j], 6, 6])
            if self.y_pos[j] > 600:
                self.y_pos[j] -= 600


    def wait_for_start_key(self):
        self.clock.tick(60)        
        waiting = True        
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    if self.playing:
                        self.playing = False  
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False
            pg.display.flip()
            

    def wait_for_key(self):
        self.clock.tick(60)
        waiting = True
        while waiting:
            if self.record == 1:
                self.screen.blit(self.bgimage, BG_POS)
                self.draw_text_bold("Your time is up!", 40, RED, WIDTH/2, HEIGHT*1/4)
                self.draw_text("You answered {} of {} questions correctly".format(self.score, self.count), 34, RED, WIDTH/2, HEIGHT/2 + 30)
                self.draw_text("To play another round press ENTER", 28, RED, WIDTH/2, HEIGHT*3/4)
                self.draw_text_bold("Congraulations!! New Highscore: "+str(self.highscore), 34, RED, WIDTH/2, HEIGHT/2)
                self.confetti()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    if self.playing:
                        self.playing = False  
                    self.running = False
                if event.type == pg.KEYDOWN and (event.key != pg.K_1 and 
                                                 event.key != pg.K_KP1 and 
                                                 event.key != pg.K_2 and 
                                                 event.key != pg.K_KP2 and 
                                                 event.key != pg.K_3 and 
                                                 event.key != pg.K_KP3):
                    waiting = False
                    
    def wait_for_event(self):
        self.clock.tick(30)
        waiting_event = True
        while waiting_event:
            self.t1 = time.time()
            self.dt = self.t1 - self.t0
            self.countdown(self.dt)
            pg.draw.rect(self.screen, GREY, [WIDTH/11, 25, 100, 20])            
            self.draw_text("Time: {0:02}:{1:02}".format(self.minutes, self.seconds), 22, RED, WIDTH/7, 20)
            pg.display.flip()
            if self.dt >= TIME:
                waiting_event = False
                self.playing = False
                self.time_up_screen()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting_event = False
                    if self.playing:
                        self.playing = False                
                    self.running = False
                elif event.type == pg.KEYDOWN and (event.key == pg.K_1 or event.key == pg.K_KP1):
                    guess = 1
                    waiting_event = False
                    return(guess)
                elif event.type == pg.KEYDOWN and (event.key == pg.K_2 or event.key == pg.K_KP2):
                    guess = 2
                    return(guess)
                    waiting_event = False
                elif event.type == pg.KEYDOWN and (event.key == pg.K_3 or event.key == pg.K_KP3):
                    guess = 3
                    waiting_event = False
                    return(guess)


                    
   
    
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    
pg.quit()
