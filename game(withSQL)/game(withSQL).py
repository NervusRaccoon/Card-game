import pyodbc
import pygame
import os.path
import random
import time

clock = pygame.time.Clock()
filepath = os.path.dirname(__file__)
server = 'HOME2\MSSQLSERVER00'
database = 'gameDB'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

pygame.init()

scX = 1000
scY = 600
screen = pygame.display.set_mode((scX, scY))
pygame.display.set_caption("Cart Game")

textFont = pygame.font.Font('freesansbold.ttf', 25)
textName = pygame.font.Font('freesansbold.ttf', 20)
textDesc = pygame.font.Font('freesansbold.ttf', 16)

def zeroing():
    cursor.execute("UPDATE card SET usability = 'not used' WHERE id_card >= 5")
    cnxn.commit()
    cursor.execute("UPDATE talent SET activity = 'inactive' WHERE id_talent >= 2")
    cnxn.commit()

zeroing()

# позиции карт
widthC = 100
heightC = 150
pos = []
pos.append(pygame.Rect(270, 430, widthC, heightC))
pos.append(pygame.Rect(390, 430, widthC, heightC))
pos.append(pygame.Rect(510, 430, widthC, heightC))
pos.append(pygame.Rect(630, 430, widthC, heightC))

# данные активных карт(которые сейчас на экране)
active = []
i = 0
while i < 4:
    r = random.randint(0, 3)
    active.append([r, 'true', r]) #active[i][0] - номер карты, active[i][1] - состояние карты, active[i][1] - номер карты для поиска в списке картинок
    i = i + 1

# Отсутствие карты
cursor.execute("SELECT path, width, height FROM image WHERE id_image = 22")
noCard = cursor.fetchall()

# Прорисовка фона со всеми деталями
def drawBack(mobName):
    # ФОН
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'background'")
    data = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))), (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))

    # ДЕТАЛИ
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'detail'")
    data = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))), (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[1][0]))), (int(data[1][1]), int(data[1][2]))), (data[1][3], data[1][4]))
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[2][0]))), (int(data[2][1]), int(data[2][2]))), (data[2][3], data[2][4]))
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[3][0]))), (int(data[3][1]), int(data[3][2]))), (data[3][3], data[3][4]))

    # ШКАЛЫ И МОБЫ
    cursor.execute("SELECT name, path, width, height, posX, posY FROM image WHERE purpose = 'mob'")
    data = cursor.fetchall()
    i = 0
    while i < len(data):
        if mobName == data[i][0]:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[i][1]))),
                                               (int(data[i][2]), int(data[i][3]))), (data[i][4], data[i][5]))
        i += 1
    if mobName == 'Alice(angry)' or mobName == 'Alice(laughs)':
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 30")
        miniAlice = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(miniAlice[0][0]))),
                                       (int(miniAlice[0][1]), int(miniAlice[0][2]))), (miniAlice[0][3], miniAlice[0][4]))

    pygame.draw.rect(screen, (255, 0, 0), (86, 541, int(140/100*hpPlayer), 31))
    pygame.draw.rect(screen, (255, 0, 0), (817, 541, int(140/storageHPmob*hpMob), 31))
    if count > 0:
        pygame.draw.rect(screen, (0, 0, 0), (203, 30, int(600/200*count), 30))

    text = textFont.render(str(int(hpMob)), True, (0, 0, 0))
    screen.blit(text, (870, 545))
    text = textFont.render(str(int(hpPlayer)), True, (0, 0, 0))
    screen.blit(text, (135, 545))

    # ЭФФЕКТЫ И КАРТЫ
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'effect'")
    data = cursor.fetchall()
    if bloodEffect == True:
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                           (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    if fireEffect == True:
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[1][0]))),
                                           (int(data[1][1]), int(data[1][2]))), (data[1][3], data[1][4]))
    if biteEffect == True:
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[2][0]))),
                                           (int(data[2][1]), int(data[2][2]))), (data[2][3], data[1][4]))

    cursor.execute("SELECT id_card, image.path, image.width, image.height FROM card INNER JOIN image ON card.id_image = image.id_image WHERE card.usability = 'used'")
    data = cursor.fetchall()
    i = 0
    while i < 4:
        if active[i][1] == 'true':
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[active[i][2]][1]))),
                                               (int(data[active[i][2]][2]), int(data[active[i][2]][3]))), pos[i])
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(noCard[0][0]))), (int(noCard[0][1]), int(noCard[0][2]))), pos[i])
        i = i + 1

# отдельно прорисовка дерева талантов
def drawTalentTree(exp):
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 35")
    data = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))), (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    text = textFont.render(str(int(exp/10)), True, (0, 0, 0))
    screen.blit(text, (535, 172))
    i = 0
    cursor.execute("SELECT path, width, height FROM image WHERE id_image = 36")
    img = cursor.fetchall()
    cursor.execute("SELECT activity, posX, posY FROM talent")
    data = cursor.fetchall()
    while i < 8:
        if data[i][0] == 'active':
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(img[0][0]))),
                                               (int(img[0][1]), int(img[0][2]))), (data[i][1], data[i][2]))
        i += 1

def choiceTalent(number):
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 34")
    data = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                       (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    cursor.execute("SELECT name, description FROM talent")
    data = cursor.fetchall()
    text = textName.render(data[number-1][0], True, (0, 0, 0))
    place = text.get_rect(center=(500, 180)) # 420 168
    screen.blit(text, place)
    blitText(screen, data[number-1][1], (335, 280), 530, textDesc)
    if number != 5:
        cursor.execute("SELECT path FROM image INNER JOIN card ON card.id_image=image.id_image WHERE id_talent = " + str(number))
        card = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(card[0][0]))),
                                           (90, 125)), (560, 290))
    else:
        cursor.execute("SELECT path FROM image WHERE id_image = 17")
        card = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(card[0][0]))),
                                           (90, 125)), (560, 290))

def blitText(surface, text, pos, max_width, font):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, (0, 0, 0))
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

# рандомит и заполняет карты
def Fill():
    number = -1
    cursor.execute("SELECT COUNT(id_card) AS cardCount FROM card WHERE usability = 'used'")
    cardCount = cursor.fetchall()
    cardCount = cardCount[0][0]
    print("cardCount = " + str(cardCount))
    cursor.execute("SELECT COUNT(id_talent) AS talentCount FROM talent WHERE activity = 'active' AND id_talent != 5")
    talentCount = cursor.fetchall()
    talentCount = talentCount[0][0]
    cursor.execute("SELECT id_card, image.path, image.width, image.height FROM card INNER JOIN image ON card.id_image = image.id_image WHERE card.usability = 'used'")
    data = cursor.fetchall()
    cardList = []
    i = 0
    while i < cardCount:
        cardList.append(data[i][0])
        i += 1
    i = 0
    while i < 4:
        if random.randint(1, 100) > 65:
            r = random.choice(cardList)
            j = 0
            while j < len(cardList):
                if cardList[j] == r:
                    number = j
                j += 1
            r -= 1
        else:
            r = random.randint(0, int(cardCount/talentCount-1))
            number = -1
        if active[i][1] == 'false':
            active[i][1] = 'true'
            active[i][0] = r
            if number != -1:
                r = number
            active[i][2] = r
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[r][1]))), (int(data[r][2]), int(data[r][3]))), pos[i])
        i = i + 1

madAlice = False
def Alice():
    global hpPlayer
    global madAlice
    if madAlice == True:
        if random.randint(1, 100) > 50:
            drawBack('Alice(laughs)')
            text = textFont.render('Алиса смеется над тобой(удара не последовало)', True, (255, 0, 0))
            screen.blit(text, (240, 70))
        else:
            if hpPlayer - 15 < 0:
                hpPlayer = 0
            else:
                hpPlayer -= 15
            drawBack('Alice')
            text = textFont.render('Алиса ударила со всей силы(-30)', True, (255, 0, 0))
            screen.blit(text, (240, 70))
            madAlice = False
    elif madAlice == False and hpMob < 200:
        if random.randint(1, 100) > 70:
            madAlice = True
            drawBack('Alice(angry)')
            text = textFont.render('Алиса начинает злиться(подготовка)', True, (0, 0, 0))
            screen.blit(text, (240, 70))
        else:
            if hpPlayer - 5 < 0:
                hpPlayer = 0
            else:
                hpPlayer -= 5
            drawBack('Alice')

def fightSlime():
    global shieldEffect
    global hpMob
    global hpPlayer
    hit = True
    damage = 5
    if hpMob > 0:
        if shieldEffect == True and hit == True:
            print("Заблокировал")
            damage = damageInShield(damage)
            hit = False
            shieldEffect = False
        if shieldEffect == False and hit == True:
            damage = 5
            print("обычный удар")
        if hpPlayer - int(damage) < 0:
            hpPlayer = 0
        else:
            hpPlayer -= int(damage)
        drawBack('Slime')

biteEffect = False
biteEffectCount = 0
def fightDog():
    global shieldEffect
    global hpMob
    global hpPlayer
    global biteEffect
    global biteEffectCount
    hit = True
    damage = 5
    if hpMob > 0:
        if biteEffect == False:
            if random.randint(1, 100) > 50:
                biteEffect = True
                text = textFont.render('Бешеный пес укусил Вас!', True, (0, 255, 0))
                screen.blit(text, (240, 70))
            else:
                if shieldEffect == True and hit == True:
                    damage = damageInShield(damage)
                    hit = False
                    shieldEffect = False
                if shieldEffect == False and hit == True:
                    damage = 5
        else:
            if shieldEffect == True and hit == True:
                damage = damageInShield(damage)
                hit = False
                shieldEffect = False
            if shieldEffect == False and hit == True:
                damage = 5
            damage += 3
            biteEffectCount += 1
        if hpPlayer - int(damage) < 0:
            hpPlayer = 0
        else:
            hpPlayer -= int(damage)
        if biteEffectCount >= 3:
            biteEffectCount = 0
            biteEffect = False
        drawBack('Dog')
        if biteEffectCount == 0 and biteEffect == True:
            text = textFont.render('Бешеный пес укусил Вас!(получение урона +5)', True, (255, 0, 0))
            screen.blit(text, (270, 70))

def damageInShield(dmg):
    global shieldEffectStrength
    if shieldEffectStrength == 20:
        dmg = dmg*20/100
    elif shieldEffectStrength == 15:
        dmg = dmg*30/100
    elif shieldEffectStrength == 10:
        dmg = dmg*40/100
    elif shieldEffectStrength == 5:
        dmg = dmg*50/100
    return dmg

textHPmob = 0
textHPplayer = 100
hpM = textFont.render('', True, (255, 0, 0))
hpP = textFont.render('', True, (255, 0, 0))
def printHP():
    global textHPmob
    global textHPplayer
    global hpM
    global hpP
    if fight == True:
        if hpMob < textHPmob:
            hpM = textFont.render('-' + str(textHPmob - hpMob), True, (255, 0, 0))
        if hpPlayer < textHPplayer:
            hpP = textFont.render('-' + str(textHPplayer - hpPlayer), True, (255, 0, 0))
        if hpPlayer > textHPplayer:
            hpP = textFont.render('+' + str(hpPlayer - textHPplayer), True, (0, 255, 0))
        screen.blit(hpM, (850, 320))
        screen.blit(hpP, (115, 320))
        textHPplayer = hpPlayer
        textHPmob = hpMob
    else:
        hpM = textFont.render('', True, (255, 0, 0))
        hpP = textFont.render('', True, (255, 0, 0))

def talentCard(number):
    if number != 5:
        cursor.execute("UPDATE card SET usability = 'used' WHERE id_talent = " + str(number))
        cnxn.commit()
    cursor.execute("UPDATE talent SET activity = 'active' WHERE id_talent = " + str(number))
    cnxn.commit()

bloodEffectStrength = 0
bloodMoveCount = 0
fireEffectStrength = 0
fireMoveCount = 0
shieldEffectStrength = 0
def playerMove(card, number):
    global bloodEffect
    global fireEffect
    global shieldEffect
    global hpMob
    global hpPlayer
    global bloodEffectStrength
    global bloodMoveCount
    global fireEffectStrength
    global fireMoveCount
    global shieldEffectStrength

    if bloodEffect == True:
        hpMob = tickingEffectCount(hpMob, bloodEffectStrength)
        if bloodMoveCount == 5:
            bloodEffect = False
    if fireEffect == True:
        hpMob = tickingEffectCount(hpMob, fireEffectStrength)
        if fireMoveCount == 5:
            fireEffect = False
    if card == 'atk':
        if hpMob - number < 0:
            hpMob = 0
        else:
            hpMob -= number
    if card == 'blood':
        if hpMob - number < 0:
            hpMob = 0
        else:
            hpMob = hpMob - number
        if bloodEffect == False:
            bloodEffectStrength = number
            bloodMoveCount = 0
            bloodEffect = True
    if card == 'fire':
        if hpMob - number < 0:
            hpMob = 0
        else:
            hpMob = hpMob - number
        if fireEffect == False:
            fireEffectStrength = number
            fireMoveCount = 0
            fireEffect = True
    if card == 'shield':
        if shieldEffect == False:
            shieldEffectStrength = number
            shieldEffect = True
    if card == 'heal':
        if number == 20:
            if hpPlayer + 50 > 100:
                hpPlayer = 100
            else:
                hpPlayer += 50
        elif number == 15:
            if hpPlayer + 40 > 100:
                hpPlayer = 100
            else:
                hpPlayer += 40
        elif number == 10:
            if hpPlayer + 30 > 100:
                hpPlayer = 100
            else:
                hpPlayer += 30
        elif number == 5:
            if hpPlayer + 20 > 100:
                hpPlayer = 100
            else:
                hpPlayer += 20
    if hpMob == 0:
        bloodEffect = False
        bloodMoveCount = 0
        fireEffect = False
        fireMoveCount = 0
    if bloodEffect == True:
        bloodMoveCount += 1
    if fireEffect == True:
        fireMoveCount += 1

def tickingEffectCount(hp, number):
    if number == 20:
        if hp - 5 < 0:
            hp = 0
        else:
            hp = hp - 5
    if number == 15:
        if hp - 4 < 0:
            hp = 0
        else:
            hp = hp - 4
    if number == 10:
        if hp - 3 < 0:
            hp = 0
        else:
            hp = hp - 3
    if number == 5:
        if hp - 2 < 0:
            hp = 0
        else:
            hp = hp - 2
    return hp

# основной цикл
count = 0
hpPlayer = 100
run = True
fight = False
endFight = False
player = False
mob = False
sizeHP = 140
storageHPmob = 1
hpMob = 0
exp = 0 #0
lvl = 10 #10
treeAct = False
talents = 1
moveCount = 0
bloodEffect = False
fireEffect = False
shieldEffect = False
cleverTrickEffect = False
biteEffect = False
choiceTalentBool = False
openChest = False
countActiveCard = 0
animation = False
treeButtonPos = pygame.Rect(30, 20, 140, 50)
drawBack(None)
clock.tick(30)
while run:
    pygame.time.delay(100)

    printHP()
    if hpPlayer <= 0:
        hpPlayer = 0
        print("Поздравляю, ты сдох")
        run = False

    if count == 200 and fight == False and endFight == False:
        fight = True
        player = True
        storageHPmob = 150
        hpMob = 150
        drawBack('Alice')
    elif (count == 25 or count == 70 or count == 75) and fight == False and endFight == False:
        fight = True
        player = True
        hpMob = 30
        storageHPmob = 30
        drawBack('Slime')
    elif (count == 95 or count == 125 or count == 155 or count == 160) and fight == False and endFight == False:
        fight = True
        player = True
        if openChest == False:
            hpMob = 30
            storageHPmob = 30
            drawBack('Slime')
        else:
            hpMob = 50
            storageHPmob = 50
            drawBack('Dog')

    if count == 85 and openChest == False and animation == False:
        drawBack('Chest')

    if mob == True and fight == True and count == 200:
        Alice()
        mob = False
        player = True
    elif mob == True and fight == True and (count == 25 or count == 70 or count == 75):
        fightSlime()
        mob = False
        player = True
    elif (count == 95 or count == 125 or count == 155 or count == 160) and fight == True and mob == True:
        if openChest == False:
            fightSlime()
        else:
            fightDog()
        mob = False
        player = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            i = 0
            act = False

            if count == 85:
                if animation == False:
                    drawBack('Chest(open)')
                    text = textFont.render('Вы изучили нового монстра "Бешеный пес"!', True, (0, 0, 0))
                    screen.blit(text, (240, 70))
                    animation = True
                else:
                    openChest = True
                    drawBack(None)
            if fight == False and choiceTalentBool == False and count != 85:
                 if treeButtonPos.collidepoint(mousePos) and treeAct == False:
                    treeAct = True
                    drawTalentTree(exp)
                 elif treeButtonPos.collidepoint(mousePos) and treeAct == True:
                    treeAct = False
                    drawBack(None)
            if treeAct == True:
                i = 0
                cursor.execute("SELECT id_talent, posX, posY, required_level, activity FROM talent")
                talent = cursor.fetchall()
                if choiceTalentBool == False:
                    while i < len(talent):
                        talentPos = pygame.Rect(talent[i][1], talent[i][2], 90, 85)
                        if talentPos.collidepoint(mousePos):
                            choiceTalent(talent[i][0])
                            choiceTalentBool = True
                            talentID = talent[i][0] - 1
                        i += 1
                else:
                    yesButtonPos = pygame.Rect(350, 470, 140, 60)
                    #pygame.draw.rect(screen, (0, 0, 0), yesButtonPos)
                    noButtonPos = pygame.Rect(515, 470, 140, 60)
                    if yesButtonPos.collidepoint(mousePos) and int(exp/10) > 0 and int(lvl/10) >= talent[talentID][3] and talent[talentID][4] == 'inactive':
                        talentCard(talentID+1)
                        exp -= 10
                        drawTalentTree(exp)
                        choiceTalentBool = False
                        if talentID == 4:
                            cleverTrickEffect = True
                    if noButtonPos.collidepoint(mousePos):
                        choiceTalentBool = False
                        drawTalentTree(exp)

            if treeAct == False and ((count == 85 and openChest == True) or (count != 85)):
                while i < 4:
                    if pos[i].collidepoint(mousePos):
                        if active[i][1] == 'true':
                            active[i][1] = 'false'
                            print(str(active[i][0] + 1))
                            cursor.execute("SELECT point, type FROM card WHERE id_card = " + str(active[i][0] + 1))
                            point = cursor.fetchall()
                            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(noCard[0][0]))), (int(noCard[0][1]), int(noCard[0][2]))), pos[i])
                            if not fight:
                                if count + int(point[0][0]) > 200:
                                    count = 200
                                else:
                                    count += int(point[0][0])
                                    print ("Нашагал " + str(count))
                                drawBack(None)
                                endFight = False

                            if fight == True:
                                if player:
                                    mob = True
                                    player = False
                                    print(point[0][1], int(point[0][0]))
                                    playerMove(point[0][1], int(point[0][0]))
                                    expText = 0
                                    if hpMob == 0:
                                        if (count == 25 or count == 70 or count == 75):
                                            exp += 5
                                            lvl += 5
                                            expText = 5
                                        if (count == 95 or count == 125 or count == 155 or count == 160):
                                            if openChest == False:
                                                exp += 5
                                                lvl += 5
                                                expText = 5
                                            else:
                                                biteEffect = False
                                                exp += 9
                                                lvl += 9
                                                expText = 9
                                        endFight = True
                                        fight = False
                                        #hpPlayer = 100
                                        drawBack(None)
                                        if count != 200:
                                            text = textFont.render('Вы получили ' + str(expText) + ' опыта!', True, (0, 0, 0))
                                        else:
                                            text = textFont.render('Ты прошёл уровень', True, (0, 0, 0))
                                        screen.blit(text, (380, 80))
                    if active[i][1] == 'true':
                        act = True
                        countActiveCard += 1
                    i = i + 1
                if cleverTrickEffect == True and countActiveCard < 2:
                    act = False
                countActiveCard = 0
                if act == False:
                    Fill()

    pygame.display.update()

pygame.quit()