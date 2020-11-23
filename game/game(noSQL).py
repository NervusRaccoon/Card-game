import pygame
import random

pygame.init()

scX = 1000
scY = 600
screen = pygame.display.set_mode((scX, scY))

pygame.display.set_caption("Cart Game")

x = 40
y = 280
width = 190
height = 300
widthC = 100
heightC = 150
widthS = 600
heightS = 30
playerImg = pygame.image.load('hero.png')
background = pygame.image.load('1.png')
background = pygame.transform.scale(background, (1000, 600))
atk5 = pygame.image.load('5(1).png')
atk5 = pygame.transform.scale(atk5, (widthC, heightC))
atk10 = pygame.image.load('10(1).png')
atk10 = pygame.transform.scale(atk10, (widthC, heightC))
atk15 = pygame.image.load('15(1).png')
atk15 = pygame.transform.scale(atk15, (widthC, heightC))
atk20 = pygame.image.load('20(1).png')
atk20 = pygame.transform.scale(atk20, (widthC, heightC))

blood5 = pygame.image.load('5(2).png')
blood5 = pygame.transform.scale(blood5, (widthC, heightC))
blood10 = pygame.image.load('10(2).png')
blood10 = pygame.transform.scale(blood10, (widthC, heightC))
blood15 = pygame.image.load('15(2).png')
blood15 = pygame.transform.scale(blood15, (widthC, heightC))
blood20 = pygame.image.load('20(2).png')
blood20 = pygame.transform.scale(blood20, (widthC, heightC))

fire5 = pygame.image.load('5(3).png')
fire5 = pygame.transform.scale(fire5, (widthC, heightC))
fire10 = pygame.image.load('10(3).png')
fire10 = pygame.transform.scale(fire10, (widthC, heightC))
fire15 = pygame.image.load('15(3).png')
fire15 = pygame.transform.scale(fire15, (widthC, heightC))
fire20 = pygame.image.load('20(3).png')
fire20 = pygame.transform.scale(fire20, (widthC, heightC))

shield5 = pygame.image.load('5(4).png')
shield5 = pygame.transform.scale(shield5, (widthC, heightC))
shield10 = pygame.image.load('10(4).png')
shield10 = pygame.transform.scale(shield10, (widthC, heightC))
shield15 = pygame.image.load('15(4).png')
shield15 = pygame.transform.scale(shield15, (widthC, heightC))
shield20 = pygame.image.load('20(4).png')
shield20 = pygame.transform.scale(shield20, (widthC, heightC))

cleverTrick5 = pygame.image.load('5(5).png')

heal5 = pygame.image.load('5(6).png')
heal5 = pygame.transform.scale(heal5, (widthC, heightC))
heal10 = pygame.image.load('10(6).png')
heal10 = pygame.transform.scale(heal10, (widthC, heightC))
heal15 = pygame.image.load('15(6).png')
heal15 = pygame.transform.scale(heal15, (widthC, heightC))
heal20 = pygame.image.load('20(6).png')
heal20 = pygame.transform.scale(heal20, (widthC, heightC))

actFalse = pygame.image.load('noCard.png')
actFalse = pygame.transform.scale(actFalse, (widthC, heightC))
scaleLine = pygame.image.load('line.png')
scaleLine = pygame.transform.scale(scaleLine, (widthS, heightS))
playerImg = pygame.transform.scale(playerImg, (int(width), int(height)))
aliceEm1 = pygame.image.load('Alice1.png')
aliceEm2 = pygame.image.load('Alice2.png')
aliceEm1 = pygame.transform.scale(aliceEm1, (250, 500))
mobImg = pygame.image.load('mob.png')
mobImg = pygame.transform.scale(mobImg, (int(width), int(height)))
mAlice = pygame.image.load('Alice.png')
mAlice = pygame.transform.scale(mAlice, (int(width), int(height)))
slime = pygame.image.load('slime.png')
slime = pygame.transform.scale(slime, (int(width), int(height)))
treeButton = pygame.image.load('state.png')
treeButton = pygame.transform.scale(treeButton, (140, 50))
tree = pygame.image.load('tree.png')
tree = pygame.transform.scale(tree, (400, 500))
choiceTalentImg = pygame.image.load('choice.png')
choiceTalentImg = pygame.transform.scale(choiceTalentImg, (400, 500))
treeActiveCell = pygame.image.load('treeActive.png')
treeActiveCell = pygame.transform.scale(treeActiveCell, (90, 85))
imgBloodEffect = pygame.image.load('mobblood.png')
imgBloodEffect = pygame.transform.scale(imgBloodEffect, (int(width), int(height)))
imgFireEffect = pygame.image.load('mobfire.png')
imgFireEffect = pygame.transform.scale(imgFireEffect, (int(width), int(height)))

textFont = pygame.font.Font('freesansbold.ttf', 25)
textName = pygame.font.Font('freesansbold.ttf', 20)
textDesc = pygame.font.Font('freesansbold.ttf', 16)

# позиции карт
pos = []
pos.append(pygame.Rect(270, 430, widthC, heightC))
pos.append(pygame.Rect(390, 430, widthC, heightC))
pos.append(pygame.Rect(510, 430, widthC, heightC))
pos.append(pygame.Rect(630, 430, widthC, heightC))

# позиции талантов
treeButtonPos = pygame.Rect(30, 20, 140, 50) # позиция кнопки
talentTree = [] #(450, 205) (380, 270) (524, 273) (335, 353) (450, 353) (575, 354) (333, 452) (450, 450) (574, 453)
talentTree.append(['Обычный удар', 'true', 'Обычный удар наносящий столько урона, сколько указано на карте', 450, 205, 1]) #1
talentTree.append(['Кровотечение', 'false', 'Обычный удар с дополнительным эффектом кровотечения: эффект отнимает у противника по 2/3/4/5 единиц здоровья в течение 5 ходов(в зависимости от цифры на карточке). Эффект не стакается.', 380, 270, 2]) #2
talentTree.append(['Поджог', 'false', 'Обычный удар с дополнительным эффектом поджога: эффект отнимает у противника по 2/3/4/5 единиц здоровья в течение 5 ходов(в зависимости от цифры на карточке). Эффект не стакается.', 524, 273, 2]) #3
talentTree.append(['Блок', 'false', 'Накладывает на героя щит на 1 ход, блокирующий 50/60/70/80% урона', 335, 353, 3]) #4
talentTree.append(['Ловкий трюк', 'false', 'Позволяет после использования 3 карт обновить их, оставив одну на руках', 450, 353, 3]) #5
talentTree.append(['Исцеление', 'false', 'Мгновенно исцеляет 20/30/40/50 единиц здоровья герою', 575, 354, 3]) #6
talentTree.append(['Вампиризм', 'false', 'В течение 3 ходов, когда герой атакует, он восполняет', 333, 452, 4]) #7
talentTree.append(['Отразить удар', 'false', 'Накладывает на героя щит на 1 ход, блокирующий 50/60/70/80% урона и наносящий противнику столько же урона, сколько было заблокировано', 450, 450, 4]) #8
talentTree.append(['Заморозка', 'false', 'Ударяет противника и замораживает его на 1 ход, из-за чего он пропускает свой следующий ход.', 574, 453, 4]) #9

# хранилище всех возможных видов карт
storage = []
storage.append([5, 'atk', atk5])
storage.append([10, 'atk', atk10])
storage.append([15, 'atk', atk15])
storage.append([20, 'atk', atk20])

# данные активных карт(которые сейчас на экране)
active = []
i = 0
while i < 4:
    r = random.randint(0, len(storage)-1)
    active.append([r, 'true'])
    screen.blit(storage[r][2], pos[i])
    i = i + 1

# прорисовка основных объектов
def drawBack(mMob, mob, mx, my):
    screen.blit(background, (0, 0))
    screen.blit(playerImg, (x, y))
    if count > 0:
        pygame.draw.rect(screen, (0, 0, 0), (203, 30, int(600/200*count), 30))
    screen.blit(scaleLine, (200, 30))
    screen.blit(mMob, (scX-x-width, y))
    screen.blit(mob, (mx, my))
    pygame.draw.rect(screen, (255, 0, 0), (86, 541, int(140/100*hpPlayer), 31))
    pygame.draw.rect(screen, (255, 0, 0), (817, 541, int(140/storageHPmob*hpMob), 31))
    screen.blit(treeButton, (30, 20))
    text = textFont.render(str(int(hpMob)), True, (0, 0, 0))
    screen.blit(text, (870, 545))
    text = textFont.render(str(int(hpPlayer)), True, (0, 0, 0))
    screen.blit(text, (135, 545))
    if bloodEffect == True:
        screen.blit(imgBloodEffect, (scX - x - width, y))
    if fireEffect == True:
        screen.blit(imgFireEffect, (scX - x - width, y))
    i = 0
    while i < 4:
        if active[i][1] == 'true':
            screen.blit(storage[active[i][0]][2], pos[i])
        else:
            screen.blit(actFalse, pos[i])
        i = i + 1

# прорисовка дерева талантов
def drawTree(e):
    screen.blit(tree, (300, 50))
    text = textFont.render(str(int(e/10)), True, (0, 0, 0))
    screen.blit(text, (535, 172))
    i = 0
    while i < len(talentTree) - 1:
        if talentTree[i][1] == 'true':
            screen.blit(treeActiveCell, (talentTree[i][3], talentTree[i][4]))
        i += 1

def choiceTalent(name, description, img):
    screen.blit(choiceTalentImg, (300, 50))
    text = textName.render(name, True, (0, 0, 0))
    place = text.get_rect(center=(500, 180)) # 420 168
    screen.blit(text, place)
    blitText(screen, description, (335, 280), 530, textDesc)
    card = pygame.transform.scale(img, (90, 125))
    screen.blit(card, (560, 290))

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

# рандомайзер карт
def Fill():
    i = 0
    while i < 4:
        if random.randint(1, 100) > 65:
            r = random.randint(0, len(storage)-1)
        else:
            r = random.randint(0, int((len(storage)/talents))-1)
        if active[i][1] == 'false':
            active[i][0] = r
            active[i][1] = 'true'
            screen.blit(storage[r][2], pos[i])
        i = i + 1

# мобы
def Alice(hp):
    print("Лиса ответила на 10 дмг")
    hp = hp - 10
    drawBack(mAlice, aliceEm1, 500, 70)
    return hp

def fightSlime(hp):
    global shieldEffect
    global hpMob
    damage = 10
    if hpMob > 0:
        if shieldEffect == True:
            print("Заблокировал")
            damageInShield(damage)
            shieldEffect = False
        else:
            hp = hp - damage
        drawBack(slime, playerImg, x, y)
    return hp

def damageInShield(dmg):
    global hpPlayer
    global shieldEffectStrength
    if shieldEffectStrength == 20:
        hpPlayer -= int(dmg*20/100)
    elif shieldEffectStrength == 15:
        hpPlayer -= int(dmg*30/100)
    elif shieldEffectStrength == 10:
        hpPlayer -= int(dmg*40/100)
    elif shieldEffectStrength == 5:
        hpPlayer -= int(dmg*50/100)

def talentCard(number):
    if number == 1:
        storage.append([5, 'blood', blood5])
        storage.append([10, 'blood', blood10])
        storage.append([15, 'blood', blood15])
        storage.append([20, 'blood', blood20])
    if number == 2:
        storage.append([5, 'fire', fire5])
        storage.append([10, 'fire', fire10])
        storage.append([15, 'fire', fire15])
        storage.append([20, 'fire', fire20])
    if number == 3:
        storage.append([5, 'shield', shield5])
        storage.append([10, 'shield', shield10])
        storage.append([15, 'shield', shield15])
        storage.append([20, 'shield', shield20])
    if number == 5:
        storage.append([5, 'heal', heal5])
        storage.append([10, 'heal', heal10])
        storage.append([15, 'heal', heal15])
        storage.append([20, 'heal', heal20])

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
        if hpMob - number < 0:
            hpMob = 0
        else:
            hpMob = hpMob - number
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
exp = 100 #0
lvl = 50 #10
treeAct = False
talents = 1
moveCount = 0
bloodEffect = False
fireEffect = False
shieldEffect = False
cleverTrickEffect = False
choiceTalentBool = False
countActiveCard = 0
drawBack(mobImg, playerImg, x, y)
while run:
    pygame.time.delay(100)

    if hpPlayer == 0:
        print("Поздравляю, ты сдох")
        run = False

    if count == 200 and fight == False and endFight == False:
        fight = True
        player = True
        storageHPmob = 200
        drawBack(mAlice, aliceEm1, 500, 70)
        count = 201
    elif (count == 25 or count == 70 or count == 75) and fight == False and endFight == False:
        fight = True
        player = True
        hpMob = 50
        storageHPmob = 50
        #hpPlayer = fightSlime(hpPlayer)
        drawBack(slime, playerImg, x, y)

    if mob == True and fight == True and count == 200:
        hpPlayer = Alice(hpPlayer)
        mob = False
        player = True
    elif mob == True and fight == True and (count == 25 or count == 70 or count == 75):
        hpPlayer = fightSlime(hpPlayer)
        mob = False
        player = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            i = 0
            act = False

            if fight == False and choiceTalentBool == False:
                if treeButtonPos.collidepoint(mousePos) and treeAct == False:
                    treeAct = True
                    drawTree(exp)
                elif treeButtonPos.collidepoint(mousePos) and treeAct == True:
                    treeAct = False
                    drawBack(mobImg, playerImg, x, y)
            if treeAct == True:
                i = 0
                if choiceTalentBool == False:
                    while i < len(talentTree):
                        talentPos = pygame.Rect(talentTree[i][3], talentTree[i][4], 90, 85)
                        if talentPos.collidepoint(mousePos):
                            if i == 0:
                                choiceTalent(talentTree[i][0], talentTree[i][2], atk5)
                            elif i == 1:
                                choiceTalent(talentTree[i][0], talentTree[i][2], blood5)
                            elif i == 2:
                                choiceTalent(talentTree[i][0], talentTree[i][2], fire5)
                            elif i == 3:
                                choiceTalent(talentTree[i][0], talentTree[i][2], shield5)
                            elif i == 4:
                                choiceTalent(talentTree[i][0], talentTree[i][2], cleverTrick5)
                            elif i == 5:
                                choiceTalent(talentTree[i][0], talentTree[i][2], heal5)
                            else:
                                choiceTalent(talentTree[i][0], talentTree[i][2], blood5)
                            choiceTalentBool = True
                            talentID = i
                        i += 1
                else:
                    yesButtonPos = pygame.Rect(350, 470, 140, 60)
                    #pygame.draw.rect(screen, (0, 0, 0), yesButtonPos)
                    noButtonPos = pygame.Rect(515, 470, 140, 60)
                    if yesButtonPos.collidepoint(mousePos) and int(exp/10) > 0 and int(lvl/10) >= talentTree[talentID][5] and talentTree[talentID][1] == 'false':
                        talentTree[talentID][1] = 'true'
                        talentCard(talentID)
                        if talentID != 4:
                            talents += 1
                        exp -= 10
                        drawTree(exp)
                        choiceTalentBool = False
                        if talentID == 4:
                            cleverTrickEffect = True
                    if noButtonPos.collidepoint(mousePos):
                        choiceTalentBool = False
                        drawTree(exp)

            if treeAct == False:
                while i < 4:
                    if pos[i].collidepoint(mousePos) :
                        if active[i][1] == 'true':
                            active[i][1] = 'false'
                            screen.blit(actFalse, pos[i])
                            if not fight:
                                if count <= 200:
                                    count = count + storage[active[i][0]][0]
                                    if count > 200:
                                        count = 200
                                drawBack(mobImg, playerImg, x, y)
                                endFight = False

                            if fight == True:
                                if player:
                                    mob = True
                                    player = False
                                    playerMove(storage[active[i][0]][1], storage[active[i][0]][0])
                                    if hpMob == 0:
                                        if (count == 25 or count == 70 or count == 75):
                                            exp += 5
                                            lvl += 5
                                        endFight = True
                                        fight = False
                                        #hpPlayer = 100
                                        drawBack(mobImg, playerImg, x, y)
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
