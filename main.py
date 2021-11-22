import pygame
import random
import time
import var
import update

#Naruto
#225 - Rasengan
#275 = Sennin modo, wind, wind x3 to rasengan, sennin modo x2 to all
#300 - oboi 2
#325 - Bomb x5 to rasengan all chakra
#350oboi3
#Naruto breaker limit  - cost//5 + 1

# initialize pygame
pygame.init()
# create display & run update
print(pygame.font.get_fonts())


def max(a, b):
    if a > b:
        return a
    else:
        return b


def min(a, b):
    if a > b:
        return b
    else:
        return a

pygame.display.update()
pygame.display.set_caption("Dattebayo!!!")





game_end = False
clock = pygame.time.Clock()

while not game_end:
    # game loop
    if var.is_Naruto:
        deg_x = 0
        deg_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                deg_x = pygame.mouse.get_pos()[0]
                deg_y = pygame.mouse.get_pos()[1]
                #print(pygame.mouse.get_pos())
                if (var.width//2-100 < deg_x < var.width//2+120) and (var.height//2-175 < deg_y < var.height//2+130):
                    update.Naruto_punch_action(deg_x, deg_y)
                    var.Naruto_chakra += var.Naruto_clone_chakra_absorb * var.is_sennin_active
                    var.Naruto_XP += var.Naruto_clone_XP_absorb * var.is_sennin_active
                    var.Naruto_total_damage += var.Naruto_clone_damage * var.is_sennin_active
                    if var.Naruto_chakra > var.Naruto_chakra_limit:
                        var.Naruto_chakra = var.Naruto_chakra_limit
                elif (var.width-75 < deg_x < 370+(352//5)) and (250 < deg_y < 250 + 307//5):
                    if len(var.Naruto_army) == var.Naruto_clone_limit:
                        phrase = var.Floating_message('Clone limit', size=24, up=1, deg_x=var.width//2-100)
                        var.Floating_words.add(phrase)
                    elif var.Naruto_chakra < var.Naruto_clone_cost:
                        phrase = var.Floating_message('Less chakra', size=24, up=1, deg_x=var.width//2-100)
                        var.Floating_words.add(phrase)
                    else:
                        var.Naruto_chakra -= var.Naruto_clone_cost
                        var.Naruto_chakra_limit += var.Naruto_clone_cost//3
                        var.Naruto_chakra_limit = min(var.Naruto_chakra_limit, var.total_Naruto_chakra_limit)
                        for i in range(var.Naruto_clone_limit):
                            if var.Naruto_army.get(i) == None:
                                var.Naruto_army[i] = var.Naruto_clone(i)
                                temp = var.Smoke_animation()
                                temp.deg_x = var.width-90
                                temp.deg_y = 310
                                var.Naruto_Clone_Animation.add(temp)
                                break
                elif (var.width-80 < deg_x) and (340 < deg_y < 400):
                    for i in range(var.Naruto_clone_limit):
                        if var.Naruto_army.get(i) != None:
                            var.Naruto_army.pop(i)
                            temp = var.Smoke_animation()
                            temp.deg_x = var.width-90
                            temp.deg_y = 310
                            var.Naruto_Clone_Animation.add(temp)
                            break

                elif (20 < deg_x << 145) and (250 < deg_y < 425) and (var.is_sennin_active == 1) and var.is_sennin_ready:
                    var.is_sennin_active = 2
                    var.is_sennin_ready = False
                    var.sennin_time = time.time()
                elif (deg_x < 1000/13) and (var.height-1000/13 < deg_y < var.height):
                    var.is_Inf = True
                    var.is_Naruto = False
                elif (10 < deg_x < 60) and (10 < deg_y < 60):
                    var.music.change()
                    var.oboi.change()

        update.Screen_update()

        update.Punch_update()

        update.Clone_update()

        update.Sennin_update()

        update.Word_update()


    if var.is_Inf:
        deg_x = 0
        deg_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                deg_x = pygame.mouse.get_pos()[0]
                deg_y = pygame.mouse.get_pos()[1]
                # print(pygame.mouse.get_pos())
                if (var.width - 70 < deg_x < var.width - 20) and (20 < deg_y < 70):
                    var.is_Inf = False
                    var.is_Naruto = True

        update.Inf_Screen_update()


    time.sleep(0.01)

    # clear screen
    pygame.display.update()

    # set FPS
    clock.tick(60)



# close app, if required
pygame.quit()
quit()