import pygame
import random
import time


pygame.init()

width = 400
height = 650
display = pygame.display.set_mode((width, height), pygame.SCALED)
#print(pygame.display.get_window_size())
width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]


class Punch_animation:
    serf_punch = pygame.Surface((264, 199)).convert()
    serf_punch.fill((255, 254, 255))
    serf_punch.set_colorkey((255, 254, 255))
    Punch_gif = {}
    deg_x = 0
    deg_y = 0
    rev = 0
    angle = 0
    for i in range(7):
        s = "Punch/" + str(i) + ".png"
        temp = pygame.image.load(s).convert_alpha()
        Punch_gif[i] = pygame.transform.scale(temp, (temp.get_width()//6, temp.get_height()//6))
    i_punch = 0
    punch_bool = False

    def Ani(self):
        #orochi_hurt.Ani()
        serf_punch1 = pygame.transform.rotate(self.serf_punch, self.angle)
        serf_punch1.fill((255, 254, 255))
        serf_punch1.set_colorkey((255, 254, 255))
        Punch_gif1 = pygame.transform.rotate(self.Punch_gif[self.i_punch], self.angle)
        serf_punch1.blit(Punch_gif1, (0, 0))
        display.blit(serf_punch1, (self.deg_x-(132//3), self.deg_y-(115//3)))
        if self.i_punch == 6:
            self.i_punch = 0
            self.punch_bool = False
        else:
            if self.i_punch == 0:
                effect.punch()
            self.i_punch += 1

    def Ani_reverse(self):
        orochi_hurt.Ani()
        serf_punch1 = pygame.transform.rotate(self.serf_punch, self.angle)
        serf_punch1.fill((255, 254, 255))
        serf_punch1.set_colorkey((255, 254, 255))
        Punch_gif1 = pygame.transform.rotate(self.Punch_gif[self.i_punch], self.angle)
        serf_punch1.blit(pygame.transform.flip(Punch_gif1, True, False), (0, 0))
        display.blit(serf_punch1, (self.deg_x-(132//3), self.deg_y-(115//3)))
        if self.i_punch == 6:
            self.i_punch = 0
            self.punch_bool = False
        else:
            if self.i_punch == 0:
                effect.punch()
            self.i_punch += 1


class Orochi_animation_move:
    serf_orochi = pygame.Surface((250, 350)).convert()
    serf_orochi.fill((255, 254, 255))
    serf_orochi.set_colorkey((255, 254, 255))
    Orochi_gif = {}
    for i in range(2):
        s = "Orochi/" + str(i) + ".png"
        Orochi_gif[i] = pygame.image.load(s)
    i_orochi = 0
    orochi_bool = True

    def Ani(self):
        temp = self.Orochi_gif[self.i_orochi // 10]
        self.serf_orochi.blit(pygame.transform.scale(temp, (temp.get_width()*2 // 3, temp.get_height()*2 // 3)), (0, 0))
        display.blit(self.serf_orochi, (width//2-250//3, height//2-350//3))
        if self.i_orochi == 19:
            self.i_orochi = 0
        #else:
        #    self.i_orochi += 1


class Orochi_animation_hurt:
    serf_orochi = pygame.Surface((250, 350)).convert()
    serf_orochi.fill((255, 254, 255))
    serf_orochi.set_colorkey((255, 254, 255))
    Orochi_gif = {}
    for i in range(2):
        s = "Orochi/" + str(i) + ".png"
        Orochi_gif[i] = pygame.image.load(s)
    i_orochi = 10
    orochi_bool = True
    x_slash = 0
    y_slash = 0
    x_sl = 5
    y_sl = 5

    def Ani(self):
        temp = self.Orochi_gif[self.i_orochi // 10]
        self.serf_orochi.blit(pygame.transform.scale(temp, (temp.get_width()*2 // 3, temp.get_height()*2//3)), (0, 0))
        display.blit(self.serf_orochi, (width//2-250//3 + self.x_slash*self.x_sl, height//2-350//3 + self.y_slash*self.y_sl))
        if self.i_orochi == 19:
            self.i_orochi = 0
        #else:
        #    self.i_orochi += 1


class BG:
    serf_oboi = pygame.Surface((1200, 800)).convert()
    serf_oboi.fill((255, 254, 255))
    serf_oboi.set_colorkey((255, 254, 255))
    oboi = {}
    mod = 2
    i_oboi = 0
    Oboi_gif = {}
    for i in range(4):
        s = "BG/" + str(i) + ".jpg"
        Oboi_gif[i] = pygame.image.load(s)

    def change(self):
        self.i_oboi = (self.i_oboi + 1) % self.mod

    def Ani(self):
        self.serf_oboi.blit(self.Oboi_gif[self.i_oboi], (0, 0))
        display.blit(self.serf_oboi, (width//2 - 600, 0))


class turn_music:
    orochi_music = pygame.mixer.Sound("Sounds/Orochi.mp3")
    akatsuki_music = pygame.mixer.Sound("Sounds/Akatsuki.mp3")
    heavy_music = pygame.mixer.Sound("Sounds/Heavy.mp3")
    dragon_music = pygame.mixer.Sound("Sounds/Dragon.mp3")
    t = True
    music_dict = {0: heavy_music, 1: dragon_music, 2: akatsuki_music, 3: orochi_music}
    i_music = 0
    music_dict[0].set_volume(0.2)
    music_dict[0].play(-1)
    mod = 2

    def turn(self):
        if self.t:
            self.t = False
            self.music_dict[self.i_music].stop()
        else:
            self.t = True
            self.music_dict[self.i_music].set_volume(0.2)
            self.music_dict[self.i_music].play(-1)


    def change(self):
        self.music_dict[self.i_music].stop()
        self.i_music = (self.i_music + 1) % self.mod
        self.music_dict[self.i_music].set_volume(0.2)
        self.music_dict[self.i_music].play(-1)


class turn_effect:
    dattebayo_sound = pygame.mixer.Sound("Sounds/Dattebayo.mp3")
    punch_sound = pygame.mixer.Sound("Sounds/Punch.mp3")
    smoke_sound = pygame.mixer.Sound("Sounds/Smoke.mp3")
    mod_sound = pygame.mixer.Sound("Sounds/mod.mp3")
    t = True

    def turn(self):
        if self.t:
            self.t = False
            self.dattebayo_sound.set_volume(0)
            self.punch_sound.set_volume(0)
            self.smoke_sound.set_volume(0)
        else:
            self.t = True
            self.dattebayo_sound.set_volume(1)
            self.punch_sound.set_volume(1)
            self.smoke_sound.set_volume(1)

    def dattebayo(self):
        self.dattebayo_sound.play()

    def punch(self):
        self.punch_sound.play()

    def smoke(self):
        self.smoke_sound.play()

    def mod(self):
        self.mod_sound.play()

class Text_animation:

    def __init__(self, x=64, s='Shrift/Blood.ttf'):
        self.deg_x = 0
        self.deg_y = 0
        self.txt = pygame.font.Font(s, x)

    def Ani(self, x, col=(255, 255, 255), bl=False):
        text = self.txt.render(x, bl, col)
        display.blit(text, (self.deg_x, self.deg_y))


def Picture_insert(s, width, height, deg_x, deg_y, scale=1, fon=(255, 254, 255), angle=0):
    serf = pygame.Surface((width, height)).convert()
    serf.fill(fon)
    serf.set_colorkey(fon)
    pic = pygame.image.load(s).convert_alpha()
    pic = pygame.transform.scale(pic, (pic.get_width() // scale, pic.get_height() // scale))
    pic = pygame.transform.rotate(pic, angle)
    serf.blit(pic, (0, 0))
    display.blit(serf, (deg_x, deg_y))


class Smoke_animation:
    serf = pygame.Surface((100, 104)).convert()
    serf.fill((0, 0, 0))
    serf.set_colorkey((0, 0, 0))
    Smoke_gif = {}
    deg_x = 0
    deg_y = 0
    for i in range(10):
        s = "Clone/" + str(i) + ".gif"
        Smoke_gif[i] = pygame.image.load(s).convert_alpha()
    i_smoke = 0
    b_bool = True

    def Ani(self):
        self.serf.fill((0, 0, 0))
        self.serf.set_colorkey((0, 0, 0))
        self.serf.blit(self.Smoke_gif[self.i_smoke], (0, 0))
        display.blit(self.serf, (self.deg_x, self.deg_y))
        if self.i_smoke == 9:
            self.i_smoke = 0
            self.b_bool = False
        else:
            if self.i_smoke == 0:
                effect.smoke()
            self.i_smoke += 1


class Mod_animation:
    serf = pygame.Surface((125, 110)).convert()
    serf.fill((0, 0, 0))
    serf.set_colorkey((0, 0, 0))
    Mod_gif = {}
    deg_x = 0
    deg_y = 0
    for i in range(11):
        s = "Sennin/" + str(i) + ".gif"
        Mod_gif[i] = pygame.image.load(s).convert_alpha()
    i_mod = 0
    b_bool = True

    def Ani(self):
        self.serf.fill((0, 0, 0))
        self.serf.set_colorkey((0, 0, 0))
        self.serf.blit(self.Mod_gif[self.i_mod], (0, 0))
        display.blit(self.serf, (self.deg_x, self.deg_y))
        if self.i_mod == 10:
            self.i_mod = 0
            self.b_bool = False
        else:
            if(self.i_mod == 0):
                effect.mod()
            self.i_mod += 1




concentrate = Mod_animation()
concentrate.deg_x = 0
concentrate.deg_y = 425 - 120
orochi_move = Orochi_animation_move()
orochi_hurt = Orochi_animation_hurt()
oboi = BG()
music = turn_music()
effect = turn_effect()
Naruto_punch = set({})
Naruto_Clone_Animation = set({})
Floating_words = set({})
Naruto_army = {}


is_Naruto = True
is_Sasuke = False
is_Menu = False
is_Inf = False
Naruto_chakra = 200
Sasuke_chakra = 0
Naruto_chakra_limit = 200
total_Naruto_chakra_limit = 40000
Sasuke_chakra_limit = 100
total_Sasuke_chakra_limit = 20000
Naruto_XP = 0
Naruto_total_damage = 0
Sasuke_XP = 0
Sasuke_total_damage = 0


Naruto_clone_damage = 2
total_Naruto_clone_damage = 100
Naruto_clone_limit = 3
total_Naruto_clone_limit = 15
Naruto_clone_life_period = 200
total_Naruto_clone_life_period = 2000
Naruto_clone_speed = 60
total_Naruto_clone_speed = 15
Naruto_clone_cost = 30
Naruto_clone_chakra_absorb = Naruto_clone_damage//2 + 1
Naruto_clone_XP_absorb = Naruto_clone_damage//4 + 1

Naruto_clone_damage_lvl = 0
total_Naruto_clone_damage_lvl = 10
Naruto_clone_limit_lvl = 0
total_Naruto_clone_limit_lvl = 10
Naruto_clone_life_period_lvl = 0
total_Naruto_clone_life_period_lvl = 10
Naruto_clone_speed_lvl = 0
total_Naruto_clone_speed_lvl = 5

game_stage = 0
perehod = False

sennin_cd = 10
sennin_duration = 4
sennin_time = time.time()
is_sennin = False
is_sennin_active = 1
is_sennin_ready = False

combo_list_Naruto = set({})
is_rasengan = False
rasengan_cd = 3

is_oboi2 = False
is_oboi3 = False


class Naruto_clone:
    time = 0
    #attack_period = 20
    #life_period = 200
    #Naruto_clone_bool = True
    number = 0
    def __init__(self, x):
        self.number = x


class Floating_message:

    def __init__(self, mes, life_period=30, size=32, deg_x=width // 2 - 200, deg_y=120, up=2, shrift='Shrift/Nordic.ttf'):
        self.message = mes
        self.time = 0
        self.life_period = life_period
        self.float = Text_animation(size, shrift)
        self.float.deg_x = deg_x
        self.float.deg_y = deg_y
        self.up = up



