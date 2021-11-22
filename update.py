import pygame
import random
import time
import var


def Naruto_punch_action(deg_x, deg_y):
    main_punch = var.Punch_animation()
    main_punch.punch_bool = True
    main_punch.deg_x = deg_x
    main_punch.deg_y = deg_y
    punch_damage = var.Floating_message('-'+str(var.Naruto_clone_damage * var.is_sennin_active), 8, 32, var.width//2, 150, 10, 'Shrift/Blood.ttf')
    var.Floating_words.add(punch_damage)
    main_punch.rev = random.randint(0, 1)
    main_punch.angle = random.randint(0, 90)
    var.Naruto_punch.add(main_punch)


XP_score = var.Text_animation(20, 'Shrift/Nordic.ttf')
damage_score = var.Text_animation(20, 'Shrift/Nordic.ttf')
total_damage_score = var.Text_animation(20, 'Shrift/Nordic.ttf')
total_damage_digit = var.Text_animation(20, 'Shrift/Nordic.ttf')
chakra_score = var.Text_animation(24, 'Shrift/Nordic.ttf')

inf_created = var.Text_animation(20, 'Shrift/Nordic.ttf')

#(linit breaker = cost//3)

def Screen_update():
    var.oboi.Ani()
    var.orochi_move.Ani()
    var.Picture_insert('Clone/Clone.jpg', 352, 307, var.width-75, 250, 5, (254, 254, 254))
    var.Picture_insert('System/inf.png', 1000, 1000, 0, var.height-1000//13, 13, (255, 255, 255))
    var.Picture_insert('System/oboi.png', 1000, 1000, 10, 10, 20, (255, 255, 255))
    chakra_score.deg_x = 100
    chakra_score.deg_y = 15
    XP_score.deg_x = 4
    damage_score.deg_x = 4
    XP_score.deg_y = 60
    damage_score.deg_y = 90
    total_damage_score.deg_x = 4
    total_damage_score.deg_y = 120
    total_damage_digit.deg_x = 40
    total_damage_digit.deg_y = 150
    chakra_score.Ani("CHAKRA:  " + str(var.Naruto_chakra) + '/' + str(var.Naruto_chakra_limit), (220, 0, 0))
    XP_score.Ani('XP:  ' + str(var.Naruto_XP), (230, 0, 0))
    damage_score.Ani('DMG:  ' + str(var.Naruto_clone_damage), (230, 0, 0))
    total_damage_score.Ani('Total DMG:', (230, 0, 0))
    total_damage_digit.Ani(str(var.Naruto_total_damage), (230, 0, 0))

def Inf_Screen_update():
    var.oboi.Ani()
    var.orochi_move.Ani()
    inf_created.deg_x = var.width-250
    inf_created.deg_y = var.height - 20
    inf_created.Ani("Created by pognick", (220, 220, 0))
    var.Picture_insert('System/exit.png', 50, 50, var.width - 70, 20, 1, (255, 255, 255))
    if var.perehod:
        for i in range(15):
            var.display.fill((255, 255, 255))
            var.oboi.Ani()
            inf_created.deg_x = var.width - 250
            inf_created.deg_y = var.height - 20
            inf_created.Ani("Created by pognick", (220, 220, 0))
            var.Picture_insert('System/exit.png', 50, 50, var.width - 70, 20, 1, (255, 255, 255))
            var.orochi_hurt.x_slash = random.randint(-1, 1)
            var.orochi_hurt.y_slash = random.randint(-1, 1)
            var.orochi_hurt.x_sl = 5
            var.orochi_hurt.y_sl = 5
            var.orochi_hurt.Ani()
            pygame.display.update()
            time.sleep(0.02)

        var.perehod = False




def Punch_update():
    temp = set({})
    for i in var.Naruto_punch:
        if i.punch_bool:
            if i.rev == 0:
                var.display.fill((50, 50, 50))
                var.oboi.Ani()
                var.Picture_insert('Clone/Clone.jpg', 352, 307, var.width-75, 250, 5, (254, 254, 254))
                var.Picture_insert('System/inf.png', 1000, 1000, 0, var.height - 1000//13, 13, (255, 255, 255))
                var.Picture_insert('System/oboi.png', 1000, 1000, 10, 10, 20, (255, 255, 255))
                chakra_score.deg_x = 100
                chakra_score.deg_y = 15
                chakra_score.Ani("CHAKRA:  " + str(var.Naruto_chakra) + '/' + str(var.Naruto_chakra_limit),
                                 (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                XP_score.Ani('XP:  ' + str(var.Naruto_XP),
                             (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                damage_score.Ani('DMG:  ' + str(var.Naruto_clone_damage), (250, 0, 0))
                total_damage_digit.Ani(str(var.Naruto_total_damage),
                                       (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                total_damage_score.Ani('Total DMG:',
                                       (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                var.orochi_hurt.x_slash = random.randint(-1, 1)
                var.orochi_hurt.y_slash = random.randint(-1, 1)
                var.orochi_hurt.x_sl = 5
                var.orochi_hurt.y_sl = 5
                var.orochi_hurt.Ani()
                i.Ani()

            else:
                var.display.fill((50, 50, 50))
                var.oboi.Ani()
                var.Picture_insert('Clone/Clone.jpg', 352, 307, var.width-75, 250, 5, (254, 254, 254))
                var.Picture_insert('System/inf.png', 1000, 1000, 0, var.height - 1000//13, 13, (255, 255, 255))
                var.Picture_insert('System/oboi.png', 1000, 1000, 10, 10, 20, (255, 255, 255))
                chakra_score.deg_x = 100
                chakra_score.deg_y = 15
                XP_score.Ani('XP:  ' + str(var.Naruto_XP),
                             (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                damage_score.Ani('DMG:  ' + str(var.Naruto_clone_damage), (250, 0, 0))
                total_damage_digit.Ani(str(var.Naruto_total_damage),
                                       (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                total_damage_score.Ani('Total DMG:',
                                       (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                chakra_score.Ani("CHAKRA:  " + str(var.Naruto_chakra) + '/' + str(var.Naruto_chakra_limit),
                                 (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)))
                var.orochi_hurt.x_slash = random.randint(-1, 1)
                var.orochi_hurt.y_slash = random.randint(-1, 1)
                var.orochi_hurt.x_sl = 5
                var.orochi_hurt.y_sl = 5
                var.orochi_hurt.Ani()
                i.Ani_reverse()
            if i.punch_bool:
                temp.add(i)
    var.Naruto_punch = temp


def Clone_update():
    for i in range(var.Naruto_clone_limit):
        if var.Naruto_army.get(i) != None:
            if var.Naruto_army[i].time % var.Naruto_clone_speed == 0:
                Naruto_punch_action(random.randint(var.width // 2 - 100, var.width // 2 + 120),
                                    random.randint(var.height // 2 - 175, var.height // 2 + 130))
                var.Naruto_chakra += var.Naruto_clone_chakra_absorb * var.is_sennin_active
                var.Naruto_XP += var.Naruto_clone_XP_absorb * var.is_sennin_active
                var.Naruto_total_damage += var.Naruto_clone_damage * var.is_sennin_active
                if var.Naruto_chakra > var.Naruto_chakra_limit:
                    var.Naruto_chakra = var.Naruto_chakra_limit
            var.Naruto_army.get(i).time += 1
            if var.Naruto_army[i].time > var.Naruto_clone_life_period:
                var.Naruto_army.pop(i)
                temp = var.Smoke_animation()
                temp.deg_x = var.width-90
                temp.deg_y = 310
                var.Naruto_Clone_Animation.add(temp)
    if len(var.Naruto_army) > 0:
        temp = var.Text_animation(24, 'Shrift/Nordic.ttf')
        var.Picture_insert('Clone/Nar.jpg', 630, 630, var.width-90, 310, 7, (254, 254, 254))
        temp.deg_x = var.width-60
        temp.deg_y = 405
        temp.Ani(str(len(var.Naruto_army)), (200, 0, 0))
    temp_anim = set({})
    for i in var.Naruto_Clone_Animation:
        i.Ani()
        if i.b_bool:
            temp_anim.add(i)
    var.Naruto_Clone_Animation = temp_anim

def Sennin_update():
    if (var.Naruto_chakra_limit >= 275) and not var.is_sennin:
        phrase = var.Floating_message('Sennin is unlocked', 200, up=0, size=32, deg_x=var.width // 2 - 170, deg_y=170)
        var.Floating_words.add(phrase)
        var.is_sennin = True
        var.is_sennin_ready = True
        var.is_Inf = True
        var.is_Naruto = False
        var.game_stage = 3
        var.sennin_time = time.time() - var.sennin_cd - 1
        var.perehod = True
        var.game_stage = 3

    if var.is_sennin:
        if var.is_sennin_active == 2:
            var.Picture_insert('Sennin/Sen.png', 250, 350, 5, 250, 2, (255, 254, 255))
            var.concentrate.Ani()
            if var.sennin_time + var.sennin_duration < time.time():
                var.concentrate.i_mod = 0
                var.is_sennin_active = 1
                var.is_sennin_ready = False
        elif var.is_sennin_ready:
            var.Picture_insert('Sennin/Sen.png', 250, 350, 5, 250, 2, (255, 254, 255))
        else:
            var.Picture_insert('Sennin/Sen0.png', 250, 350, 5, 250, 2, (255, 254, 255))
            temp = var.Text_animation(24, 'Shrift/Nordic.ttf')
            temp.deg_x = 20
            temp.deg_y = 430
            x = "{0:.2f}".format((var.sennin_time + var.sennin_cd) - time.time())
            temp.Ani(x, (200, 0, 0))
            if var.sennin_time + var.sennin_cd < time.time():
                var.is_sennin_ready = True
                var.is_sennin_active = 1

def Word_update():
    word_temp = set({})
    for i in var.Floating_words:
        i.float.Ani(i.message, (random.randint(200, 250), 0, 0))
        i.float.deg_y -= i.up
        i.time += 1
        if i.time <= i.life_period:
            word_temp.add(i)
    var.Floating_words = word_temp