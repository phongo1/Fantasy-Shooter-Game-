# phong le cxj8ar
# diana nguyen tuh8gz

import uvage
import random

camera = uvage.Camera(800, 600)

characters = uvage.load_sprite_sheet('characters_sheet.png',2, 5)
box = uvage.from_image(400, 100, characters[0])
box.scale_by(.4)

octopus = uvage.from_image(285,380, 'octopus.png')
octopus.scale_by(.055)


character_positions = [
    (235, 85),
    (320, 85),
    (400, 85),
    (480, 85),
    (560, 85),
    (235, 175),
    (320, 175),
    (400, 175),
    (480, 175),
    (560, 175)
]
platfrm = uvage.load_sprite_sheet('platform.png', 2, 1)
platforms = [
    uvage.from_image(50,370, platfrm[1]),
    uvage.from_image(750, 305, platfrm[1])
]
animation = uvage.load_sprite_sheet("explosion_animation.png", 4, 3)
explosion = uvage.from_image(400, 300, animation[-1])
explosion.scale_by(.4)

ink = uvage.from_image(400,200, 'redInk.png')
ink.scale_by(.075)


arrow = uvage.load_sprite_sheet('arrow_sheet.png', 5, 4)
a = uvage.from_image(400,200, arrow[0])
a.scale_by(2)


red = uvage.from_image(235, 85, 'redspot.png')
red.scale_by(.013)

kaboom = uvage.from_image(400,300 , 'kaboom.png')
kaboom.scale_by(.1)

firemap = uvage.from_image(400,175, 'firemap.png')
firemap.scale_by(.9)

ouch = uvage.from_image(400,300, 'ouch.png')
ouch.scale_by(.2)

coin = uvage.from_image(140, -165, 'coin.png')
coin.scale_by(.05)

animation1 = uvage.load_sprite_sheet('blast.png',6, 8)
blast = uvage.from_image(400, 300, animation1[-1])

characters = uvage.load_sprite_sheet('characters_sheet.png',2, 5)
character = uvage.from_image(400, 300, characters[4])

current_frame = 0
current_frame1 = 0

Nwall = uvage.from_color(box.x, box.y - 305, "black", 800, 20)
Ewall = uvage.from_color(box.x + 405, box.y, "black", 20, 800)
Swall = uvage.from_color(box.x, box.y + 305, 'black', 800, 20)
Wwall = uvage.from_color(box.x - 405, box.y, 'black', 20, 800)

bubbles = uvage.from_image(400, 300, 'bubbles.png')
bubbles.scale_by(.12)
bubbles.rotate(-5)

camera.x = box.x
camera.y = box.y

flip = False
game_on = False
game_over = True
idle_screen = True
touch = False

bulletsN = []
bulletsS = []
bulletsW = []
bulletsE = []
enemies = []
boss = []
Ebullets = []
health1 = 100
i = 0
i2 = 0
i3 = 0
b_index = 0
arrowindex = 0
dictionaryCounter = 0
gold = 0

#player stats (added on from upgrades)
health2 = 1
fireRate = 0
speed1 = 0
fireRadius = 0
fireDamage = 0
lifeCount = 1

removed_enemy = []
removed_boss = []

def shoot():
    global level
    global counter
    global i2
    global fireRadius
    global flip

    if uvage.is_pressing('w'):     # DIRECTIONAL SHOOTING MECHANIC
        f = uvage.from_image(box.x, box.y - 55, 'fireball.png')
        f.scale_by(.1 +fireRadius)
        bulletsN.append(f)
        boom = uvage.from_image(box.x, box.y - 45, 'boom.png')
        boom.scale_by(.06)
        camera.draw(boom)
    elif uvage.is_pressing('s'):
        # box.move
        f = uvage.from_image(box.x, box.y + 55, 'fireball.png')
        f.scale_by(.1 +fireRadius)
        bulletsS.append(f)
        boom = uvage.from_image(box.x, box.y + 45, 'boom.png')
        boom.scale_by(.06)
        camera.draw(boom)
    elif uvage.is_pressing('a'):   # ORIENTS PLAYER TO DIRECTION OF SHOOTING
        if flip == True:
            box.flip()
            flip = False
        if uvage.is_pressing('a') and uvage.is_pressing('right arrow'):
            box.flip()
        f = uvage.from_image(box.x - 55, box.y - 10, 'fireball.png')
        f.scale_by(.1 + fireRadius)
        bulletsW.append(f)
        boom = uvage.from_image(box.x - 45, box.y, 'boom.png')
        boom.scale_by(.06)
        camera.draw(boom)
    elif uvage.is_pressing('d'):
        if flip == False:
            box.flip()
            flip = True
        if uvage.is_pressing('d') and uvage.is_pressing('left arrow'):
            box.flip()

        f = uvage.from_image(box.x + 55, box.y - 10, 'fireball.png')   # FIREBALL PROJECTILE
        f.scale_by(.1 + fireRadius)
        bulletsE.append(f)
        boom = uvage.from_image(box.x + 45, box.y, 'boom.png')
        boom.scale_by(.06)
        camera.draw(boom)



count = 0
level = 1


def spawn_enemies():
    global count
    global level
    global health1
    global health2
    if level == 1 and count == 0:   #SPAWNS ENEMIES
        for i in range(5):
            enemies.append(
                uvage.from_image(random.randrange(0, 801), box.y - random.randrange(400, 700), 'redDragon.png'))
            LoR = random.randrange(0, 2)
            if LoR == 0:
                enemies.append(uvage.from_image(box.x - random.randrange(400,550), random.randrange(-200,500), 'whiteDragon1.png'))
            elif LoR == 1:
                enemies.append(uvage.from_image(box.x + random.randrange(400,550), random.randrange(-200,500), 'whiteDragon2.png'))

        count += 1
    if level == 2 and count == 2:
        for i in range(7):
            uvage.from_image(random.randrange(0, 801), box.y - random.randrange(400, 700), 'redDragon.png')

            LoR = random.randrange(0, 2)
            if LoR == 0:
                enemies.append(uvage.from_image(box.x - random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon1.png'))
            elif LoR == 1:
                enemies.append(uvage.from_image(box.x + random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon2.png'))
        count += 1
    if level == 3 and count == 4:
        for i in range(9):
            uvage.from_image(random.randrange(0, 801), box.y - random.randrange(400, 700), 'redDragon.png')

            LoR = random.randrange(0, 2)
            if LoR == 0:
                enemies.append(uvage.from_image(box.x - random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon1.png'))
            elif LoR == 1:
                enemies.append(uvage.from_image(box.x + random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon2.png'))
        count += 1
    if level == 4 and count == 6:
        fireboss = uvage.from_image(random.randrange(0, 801), -250, 'fireboss.png')
        fireboss.scale_by(.025)
        boss.append(fireboss)
        for i in range(6):
            uvage.from_image(random.randrange(0, 801), box.y - random.randrange(400, 700), 'redDragon.png')

            LoR = random.randrange(0, 2)
            if LoR == 0:
                enemies.append(uvage.from_image(box.x - random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon1.png'))
            elif LoR == 1:
                enemies.append(uvage.from_image(box.x + random.randrange(400, 550), random.randrange(-200, 500),
                                                'whiteDragon2.png'))
        count += 1
    if level == 5 and count == 8:
        health1 = 400
        waterboss = uvage.from_image(random.randrange(0, 801), -400, 'waterboss.png')
        waterboss.scale_by(.270)
        boss.append(waterboss)
        count += 1
    if level == 6 and count == 10:
        health1 = 600
        metalboss = uvage.from_image(-200, 330, 'metalboss.png')
        metalboss.scale_by(.4)
        boss.append(metalboss)
        count += 1


def kill_enemies():
    global level
    global count
    global health1
    global game_over
    global game_on
    global Ebullets
    global gold
    global animation
    global current_frame
    global current_frame1
    global bullets_total
    global removed_enemy
    global coinCounter
    global fireDamage
    global health2
    bullets_total = []
    for each in bulletsN:    # REMOVES BULLET FROM MAP AFTER TOUCHING WALL TO MINIMIZE LAG
        bullets_total.append(each)
        if each.touches(Nwall):
            bulletsN.remove(each)
    for each in bulletsE:
        bullets_total.append(each)
        if each.touches(Ewall):
            bulletsE.remove(each)
    for each in bulletsW:
        bullets_total.append(each)
        if each.touches(Wwall):
            bulletsW.remove(each)
    for each in bulletsS:  # REMOVES BULLETS ONCE THEY TOUCH WALL TO REDUCE LAG
        bullets_total.append(each)
        if each.touches(Swall):
            bulletsS.remove(each)
    for each in bullets_total:
        for enemy in enemies:  #REMOVES ENEMY WHEN HIT BY BULLET
            if each.touches(enemy) or enemy.touches(bubbles):
                enemies.remove(enemy)
                if each in bulletsN:
                    bulletsN.remove(each)
                elif each in bulletsE:
                    bulletsE.remove(each)
                elif each in bulletsS:
                    bulletsS.remove(each)
                elif each in bulletsW:
                    bulletsW.remove(each)
                removed_enemy.append(enemy)
                gold += 4
        for b in boss: # REMOVES BOSS WHEN HIT BY BULLET
            if each.touches(b):
                health1 -= 1 + fireDamage
                explosion.image = animation[int(current_frame)]
                explosion.x = each.x
                explosion.y = each.y
                camera.draw(explosion)
                camera.display()
                current_frame += 1
                if current_frame == 12:
                    current_frame = 0
                if each in bulletsN:   # REMOVES BULLETS AFTER HITTING BOSS
                    bulletsN.remove(each)
                if each in bulletsE:
                    bulletsE.remove(each)
                if each in bulletsS:
                    bulletsS.remove(each)
                if each in bulletsW:
                    bulletsW.remove(each)
                if health1 <= 0:
                    boss.remove(b)
                    removed_boss.append(b)
                    if level == 4: # GOLD FOR RED BOSS
                        gold += 50
                        print(50)
                    elif level == 5: # GOLD FOR BLUE BOSS
                        gold += 100
                        print(100)


    if enemies == [] and boss == []:
        count += 1
        level += 1
    for each in enemies:
        if box.touches(each):    # IF PLAYER TOUCHES ENEMY HEALTH IS REMOVED AND GAME IS OVER IF HEALTH =0
            enemies.remove(each)
            health2 -= 1
            ouch.x = box.x - 10
            ouch.y = each.y
            camera.draw(ouch)
            if health2 <= 0:
                game_over = True
                game_on = False

    for each in boss:
        if box.touches(each):
            health2 -= 1
            ouch.x = box.x - 10
            ouch.y = each.y
            camera.draw(ouch)
            if health2 <= 0:
                game_over = True
                game_on = False
    for each in Ebullets:
        if box.touches(each):
            Ebullets.remove(each)
            health2 -= 1
            ouch.x = box.x - 10
            ouch.y = each.y
            camera.draw(ouch)
            if health2 <= 0:
                game_over = True
                game_on = False


def movement():
    global touch
    global b_index
    speed = 7 + speed1
    if not box.top_touches(bubbles):
        box.speedy += 1
    box.move_speed()
    global flip
    if uvage.is_pressing("right arrow"):
        box.x += speed
        if flip == False:
            box.flip()
            flip = True
    bubbles.y -= 3  #GIVES BUBBLES MOVEMENT
    if b_index == 5:
        bubbles.x += 2
    elif b_index == 15:
        bubbles.x += 4
    elif b_index == 40:
        bubbles.x -= 2
    elif b_index == 50:
        bubbles.x -= 4
    if b_index >= 51:
        b_index = 0

    if bubbles.y <= -300: # RESETS POSITION OF BUBBLES WHEN HITS TOP WALL
        bubbles.y = 300



    if uvage.is_pressing("left arrow"):
        box.x -= speed
        if flip == True:
            box.flip()
            flip = False
    if uvage.is_pressing("up arrow"): # JUMP
        box.y -= 25

    if uvage.is_pressing("down arrow"):
        box.y += speed

    for each in bulletsN:
        each.y -= 20
    for each in bulletsS:
        each.y += 20
    for each in bulletsW:
        each.x -= 20
    for each in bulletsE:
        each.x += 20
    for each in enemies:
        if box.x < each.x:
            each.x -= 2.5
        if box.y < each.y:
            each.y -= 2.5
        if box.x > each.x:
            each.x += 2.5
        if box.y > each.y:
            each.y += 2.5
        for j in range(len(enemies)):
            i = 1
            if enemies.index(enemies[-1]) > enemies.index(each) + i:  # STOPS OVERLAP OF ENEMIES
                if each.touches(enemies[enemies.index(each) + i]):
                    each.move_to_stop_overlapping(enemies[enemies.index(each) + i])
            i += 1

    for each in platforms:
        if box.touches(each):
            box.move_to_stop_overlapping(each)

    for each in boss:
        if box.x < each.x and level == 4:
            each.x -= 3
        if box.x > each.x and level == 4:
            each.x += 3
        if box.y < each.y and level == 4:
            each.y -= 3
        if box.y > each.y and level == 4:
            each.y += 3
        if box.x < each.x and level == 5:
            each.x -= 4.75
        if box.x > each.x and level == 5:
            each.x += 4.75
        if each.y < -130 and level == 5:
            each.y += 3.5
        if box.x < each.x and level == 6:
            each.x -= 3
        if box.x > each.x and level == 6:
            each.x += 3

    for each in Ebullets:
        each.speedy = 8
        each.move_speed()
    if box.touches(Nwall):  # CHARACTER COLLISION PHYSICS WITH WALLS
        box.move_to_stop_overlapping(Nwall)

    if box.touches(Ewall):
        box.move_to_stop_overlapping(Ewall)
    if box.touches(Swall):
        box.move_to_stop_overlapping(Swall)
    if box.touches(Wwall):
        box.move_to_stop_overlapping(Wwall)


def draw_objects():
    camera.draw(octopus)
    rock = uvage.from_image(400, 420, 'pinkrock.png')
    rock.scale_by(1)
    camera.draw(rock)

    camera.draw(bubbles)

    plant = uvage.from_image(400, 360, 'pinkplant.png')
    plant.scale_by(.065)
    camera.draw(plant)

    camera.draw(box)

    camera.draw(Nwall)
    camera.draw(Ewall)
    camera.draw(Swall)
    camera.draw(Wwall)






    for each in platforms:
        camera.draw(each)

    for b in boss:
        if level <= 5:
            camera.draw(uvage.from_text(b.x, b.bottom + 30, str(health1), 40, 'red', True))
        elif level >= 6:
            camera.draw(uvage.from_text(b.x, b.bottom - 150, str(health1), 40, 'red', True))


    for each in bulletsN:
        camera.draw(each)
        each.rotate(60)
    for each in bulletsS:
        camera.draw(each)
        each.rotate(60)
    for each in bulletsW:
        camera.draw(each)
        each.rotate(60)
    for each in bulletsE:
        camera.draw(each)
        each.rotate(60)
    for each in enemies:
        camera.draw(each)
    for each in boss:
        camera.draw(each)
        if level == 4:
            each.rotate(25)
    for each in Ebullets:
        camera.draw(each)


def upgrades():
    global gold
    global health2
    global speed1
    global fireRate
    global fireRadius
    global fireDamage
    global lifeCount
    FireRateCost= 30
    healthCost = 75
    speedCost = 30
    radiusCost = 40
    if gold >= FireRateCost and uvage.is_pressing('1') and fireRate <= 5:
        gold -= FireRateCost
        fireRate += 1
    if gold >= speedCost and uvage.is_pressing('2') and speed1 <= 4:
        gold -= speedCost
        speed1+= 1
    if gold >= radiusCost and uvage.is_pressing('3') and fireRadius <= .15:
        gold -= radiusCost
        fireRadius +=.03
        fireDamage += 2
    if gold >= healthCost and uvage.is_pressing('4') and health2 <= 5:
        gold -= healthCost
        health2 += 1
        lifeCount += 1
    camera.draw(coin)
    camera.draw(uvage.from_text(175, -165, str(gold), 30, 'gold2'))
    camera.draw(uvage.from_text(65, -165, 'Level: ' + str(level), 30, 'black'))

    camera.draw(uvage.from_text(100, 280, 'Character Stats:', 25, 'black', italic=False, bold=True))
    camera.draw(uvage.from_color(100, 290, 'black', 110, 3))

    camera.draw(uvage.from_text(95, 310, '1) Fire Rate: 5', 20, 'black', italic=False, bold=False))
    camera.draw(uvage.from_text(160, 310, '+ ' + str(float(fireRate)), 20, 'indianred', italic=False, bold=False))

    camera.draw(uvage.from_text(90, 330, '2) Speed: 10', 20, 'black', italic=False, bold=False))
    camera.draw(uvage.from_text(160, 330, '+ ' + str(float(speed1)), 20, 'indianred', italic=False, bold=False))

    camera.draw(uvage.from_text(110, 350, '3) Fire Damage: 20', 20, 'black', italic=False, bold=False))
    camera.draw(uvage.from_text(200, 350, '+ ' + str(float(fireDamage)), 20, 'indianred', italic=False, bold=False))
    camera.draw(
        uvage.from_text(80, 370, '4) Lives: ' + str(health2), 20, 'black', italic=False, bold=False))
    heart = uvage.from_image(130, 370, 'heart.png')
    heart.scale_by(.04)
    camera.draw(heart)
def kill_animation():
    global removed_enemy
    global current_frame
    global removed_boss
    global current_frame1
    if removed_enemy:
        for each in removed_enemy:
            explosion.image = animation[int(current_frame)]  # KILLING ANIMATION
            explosion.x = each.x
            explosion.y = each.y
            camera.draw(explosion)
            camera.display()
            current_frame += 1
            if current_frame == 12:
                removed_enemy.remove(each)
                current_frame = 0
    if removed_boss:
        for each in removed_boss:  # KILLING ANIMATION
            blast.image = animation1[int(current_frame1)]
            blast.x = each.x
            blast.y = each.y
            camera.draw(blast)
            camera.display()
            current_frame1 += 1
            if current_frame1 == 47:
                removed_boss.remove(each)
                current_frame1 = 0

counter = 0
def tick():
    global game_over
    global game_on
    global counter
    global level
    global count
    global i
    global idle_screen
    global enemies
    global bulletsN
    global bulletsE
    global bulletsS
    global bulletsW
    global current_frame
    global fireRate
    global i2
    global health2
    global fireRadius
    global fireDamage
    global speed1
    global lifeCount
    global arrowindex
    global character_positions
    global dictionaryCounter
    global i3
    global b_index
    if idle_screen:
        camera.clear('mistyrose')
        cloud = uvage.from_image(400, -200, 'clouds.png')
        camera.draw(cloud)

        camera.draw(uvage.from_text(400, -120, 'PRESS SPACE TO START', 40, 'black', italic=False, bold=True))
        camera.draw(uvage.from_color(400, -100, 'black', 350, 3))
        camera.draw(uvage.from_text(400, -90, 'Avoid and shoot enemies | Buy upgrades and beat levels', 15, 'black',
                                    italic=False, bold=False))
        camera.draw(uvage.from_text(100, 280, 'Controls:', 25, 'black', italic=False, bold=True))
        camera.draw(uvage.from_color(100, 290, 'black', 100, 3))
        camera.draw(uvage.from_text(175, 320, 'HOLD "w" OR "a" OR "s" OR "d" to shoot', 20, 'black', italic=False, bold=False))
        camera.draw(uvage.from_circle(40, 320, 'black', 4))
        camera.draw(uvage.from_text(180, 360, '|arrow keys| to MOVE ~ up arrow to JUMP', 20, 'black', italic=False, bold=False))
        camera.draw(uvage.from_circle(40, 360, 'black', 4))
        if i%7 == 0:
            red.rotate(20)
            red.flip()
        camera.draw(red)

        chtr = uvage.from_image(400,125, 'characters_sheet.png')
        chtr.scale_by(.4)
        camera.draw(chtr)

        a.x = chtr.x + 250
        a.y = chtr.y
        a.image = arrow[arrowindex]
        camera.draw(a)
        a2 = a.copy_at(chtr.x - 250, chtr.y)
        a2.flip()
        camera.draw(a2)
        if arrowindex == 19:
            arrowindex = 0

        if uvage.is_pressing('right arrow') and i3 >= 10:  # SCROLLS THROUGH CHARACTERS
            dictionaryCounter += 1
            if dictionaryCounter == 10 or dictionaryCounter == 0:
                dictionaryCounter = 0
                red.y = 85
            red.x = character_positions[dictionaryCounter][0]
            if dictionaryCounter == 5 or dictionaryCounter == -5:
                red.y = 175
            i3 = 0
        if uvage.is_pressing('left arrow') and i3 >= 10:  # SCROLLS THROUGH CHARACTERS
            dictionaryCounter -= 1
            if dictionaryCounter == -10:
                dictionaryCounter = 0
            red.x = character_positions[dictionaryCounter][0]
            if dictionaryCounter == -6 or dictionaryCounter == 4:
                red.y = 85
            elif dictionaryCounter == -1:
                red.y = 175
            i3 = 0
        box.image = characters[dictionaryCounter]
        frame = uvage.from_image(chtr.x, chtr.y, 'frame.png')
        frame.scale_by(.25)
        camera.draw(frame)

        rose1 = uvage.from_image(120, 10, 'rose1.png')
        rose1.scale_by(.07)
        rose1.rotate(20)
        camera.draw(rose1)

        rose3 = uvage.from_image(700, 180, 'rose3.png')
        rose3.scale_by(.1)
        camera.draw(rose3)

        camera.display()
    if uvage.is_pressing('space') and game_over == True:
        game_on = True
        game_over = False
        idle_screen = False
        global health1
        box.x = camera.x
        box.y = camera.y
        enemies.clear()
        boss.clear()
        health1 = 100
        counter = 0
        level = 1
        count = 0
        health2 = lifeCount
    if game_over and idle_screen == False:
        counter += 1
    if game_over and idle_screen == False:
        if counter > 50:
            camera.clear('lightskyblue1')
            cld = uvage.from_image(400,-50, 'clouds2.png')
            cld.scale_by(.5)
            camera.draw(cld)
            camera.draw(uvage.from_text(400, -150, 'GAME OVER', 40, 'indianred', italic=False, bold=True))
            camera.draw(uvage.from_color(400, -130, 'indianred', 250, 5))
            camera.draw(uvage.from_text(400, -100, 'PRESS SPACE TO CONTINUE', 30, 'indianred', italic=False, bold=True))


            camera.draw(uvage.from_color(400,220,'mistyrose',380,90))

            blue1 = uvage.from_image(400,160, 'blue1.png')
            blue1.scale_by(.02)
            camera.draw(blue1)

            blue2 = uvage.from_image(400,165, 'blue2.png')
            blue2.scale_by(.04)
            camera.draw(blue2)

            camera.draw(uvage.from_text(400, 160, 'UPGRADES', 30, 'black', italic=False, bold=False))
            camera.draw(uvage.from_color(400, 170, 'black', 55, 3))
            camera.draw(uvage.from_text(430, 190, 'PRESS 1: Purchase +1.0 Fire Rate Upgrade', 20, 'black', italic=False, bold=False))
            camera.draw(uvage.from_text(250, 190, '30 GOLD', 20, 'gold2', italic=False, bold=False))
            camera.draw(uvage.from_text(415, 210, 'PRESS 2: Purchase +.2 Speed Upgrade', 20, 'black', italic=False, bold=False))
            camera.draw(uvage.from_text(250, 210, '30 GOLD', 20, 'gold2', italic=False, bold=False))
            camera.draw(uvage.from_text(430, 230, 'PRESS 3: Purchase +2.0 Projectile Upgrade', 20, 'black', italic=False, bold=False))
            camera.draw(uvage.from_text(250, 230, '40 GOLD', 20, 'gold2', italic=False, bold=False))
            camera.draw(uvage.from_text(405, 250, 'PRESS 4: Purchase +1 Life Upgrade', 20, 'black', italic=False,
                                        bold=False))
            camera.draw(uvage.from_text(250, 250, '75 GOLD', 20, 'gold2', italic=False, bold=False))

            camera.draw(coin)
            camera.draw(uvage.from_text(180, -165, str(gold), 30, 'gold2'))
            camera.draw(uvage.from_text(65, -165, 'Level: ' + str(level), 30, 'black'))
            camera.display()

    if game_on:
        if level >= 7:
            camera.clear('white')
            camera.draw(uvage.from_text(400, 0, 'YOU WIN!', 60, 'black'))
            camera.display()
        else:
            camera.clear('lightskyblue1')
            draw_objects()
            if i % (10-fireRate) == 0:
                shoot()
            if i2 % 30 == 0 and level == 5:
                for each in boss:
                    if level == 5:
                        ink.x = each.x
                        ink.y = each.y - 50
                        Ebullets.append(ink)
                    kaboom.x = each.x
                    kaboom.y = each.y + 50
                    camera.draw(kaboom)
            spawn_enemies()
            kill_enemies()
            movement()
            upgrades()
            kill_animation()
            camera.display()
    i += 1
    i2 += 1
    i3 += 1
    b_index += 1
    arrowindex +=1

uvage.timer_loop(50, tick)
