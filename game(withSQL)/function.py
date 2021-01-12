import pygame
import os.path
import pyodbc
import random
import socket
import window
import menu
import level1
import level2

filepath = os.path.dirname(__file__)
server = 'DESKTOP-853A94C'#'HOME2\MSSQLSERVER00'
database = 'gameDB'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

ip = socket.gethostbyname(socket.gethostname())
idPlayer = 1

def idCheck():
    global idPlayer

    cursor.execute("SELECT id_player FROM player WHERE ip = '" + ip + "'")
    idPlayer = cursor.fetchall()
    if len(idPlayer) != 0:
        idPlayer = idPlayer[0][0]

cursor.execute("SELECT path, width, height FROM image WHERE id_image = 22")
noCard = cursor.fetchall()

pygame.init()

screen = window.screen

textFont = pygame.font.Font('freesansbold.ttf', 25)
textName = pygame.font.Font('freesansbold.ttf', 20)
textDesc = pygame.font.Font('freesansbold.ttf', 16)

maxPlayerHP = 0
def clearBD():
    global maxPlayerHP

    idCheck()
    cursor.execute("UPDATE card SET usability = 'not used' WHERE id_card >= 5")
    cursor.execute("UPDATE talent SET activity = 'inactive' WHERE id_talent >= 2")
    cursor.execute("SELECT COUNT(*) FROM enemy AS count_enemy")
    N = cursor.fetchall()
    N = N[0][0]
    cursor.execute("SELECT max_health_point FROM enemy ORDER BY id_enemy ASC")
    enemyHP = cursor.fetchall()
    i = 1
    while i < N:
        cursor.execute("UPDATE enemy SET health_point = " + str(enemyHP[i-1][0]) + ", activity = 'false' WHERE id_enemy = " + str(i))
        i += 1
    cursor.execute("SELECT strength FROM player WHERE id_player = " + str(idPlayer))
    gameStrength = cursor.fetchall()
    gameStrength = gameStrength[0][0]
    playerHP = 0
    if gameStrength == 'hard':
        playerHP = 150
    elif gameStrength == 'norm':
        playerHP = 200
    elif gameStrength == 'easy':
        playerHP = 400
    maxPlayerHP = playerHP
    cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + ", experience = 0, max_experience = 0 WHERE id_player = " + str(idPlayer))
    cursor.execute("UPDATE effect SET activity = 'false', strength = 0, step_count = 0")
    cursor.execute("UPDATE enemy_emergence SET passed = 'false'")

    cnxn.commit()

def posButtons():
    cursor.execute("SELECT width, height, posX, posY FROM image WHERE name = 'MenuButton' or name = 'Talent tree button' ORDER BY id_image ASC")
    data = cursor.fetchall()
    menuButton = pygame.Rect(data[1][2], data[1][3], data[1][0], data[1][1])
    treeButton = pygame.Rect(data[0][2], data[0][3], data[0][0], data[0][1])
    return menuButton, treeButton

def posCards():
    pos = []
    widthC = 100
    heightC = 150
    pos.append(pygame.Rect(270, 430, widthC, heightC))
    pos.append(pygame.Rect(390, 430, widthC, heightC))
    pos.append(pygame.Rect(510, 430, widthC, heightC))
    pos.append(pygame.Rect(630, 430, widthC, heightC))

    return pos

pos = posCards()

def createActiveCard():
    active = []
    i = 0
    while i < 4:
        r = random.randint(0, 3)
        active.append([r, 'true', r]) #active[i][0] - номер карты, active[i][1] - состояние карты, active[i][1] - номер карты для поиска в списке картинок
        i += 1

    return active

def drawBack(active, count, mobName, level):
    # ФОН
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'background' and id_game_level = " + str(level))
    data = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))), (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))

    cursor.execute("SELECT name, activity, step_count FROM effect")
    effects = cursor.fetchall()

    # ЭФФЕКТ ТЕМНОТЫ
    if effects[9][0] == 'Dark' and effects[9][1] == 'true':
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE name = 'Dark'")
        data = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                           (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    # ПРОРИСОВКА СОРОКИ
    if effects[10][1] == 'false' and level == 2 and count == 365:
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 1082 or id_image = 1081")
        magpie = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(magpie[0][0]))),
                                       (int(magpie[0][1]), int(magpie[0][2]))), (magpie[0][3], magpie[0][4]))
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(magpie[1][0]))),
                                   (int(magpie[1][1]), int(magpie[1][2]))), (magpie[1][3], magpie[1][4]))
    # ДЕТАЛИ
    cursor.execute("SELECT path, width, height, posX, posY, id_game_level FROM image WHERE purpose = 'detail'")
    data = cursor.fetchall()
    i = 0
    while i < len(data):
        if data[i][5] == level or data[i][5] == None:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[i][0]))), (int(data[i][1]), int(data[i][2]))), (data[i][3], data[i][4]))
        i += 1

    # ШКАЛЫ И МОБЫ
    cursor.execute("SELECT name, path, width, height, posX, posY FROM image WHERE purpose = 'mob' and (id_game_level = " + str(level) + " or id_game_level IS NULL)")
    data = cursor.fetchall()
    i = 0
    while i < len(data):
        if mobName == data[i][0] and effects[9][1] == 'false' and mobName != 'Magpie':
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[i][1]))),
                                               (int(data[i][2]), int(data[i][3]))), (data[i][4], data[i][5]))
        i += 1
    if mobName == 'Alice(angry)' or mobName == 'Alice(laughs)':
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 30")
        miniAlice = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(miniAlice[0][0]))),
                                       (int(miniAlice[0][1]), int(miniAlice[0][2]))), (miniAlice[0][3], miniAlice[0][4]))
    if mobName == 'Owl' and effects[9][1] == 'true':
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 1079 or id_image = 1078")
        owl = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(owl[0][0]))),
                                       (int(owl[0][1]), int(owl[0][2]))), (owl[0][3], owl[0][4]))
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(owl[1][0]))),
                                   (int(owl[1][1]), int(owl[1][2]))), (owl[1][3], owl[1][4]))
    if mobName == 'Magpie':
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 1082 or id_image = 1083")
        magpie = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(magpie[0][0]))),
                                    (int(magpie[0][1]), int(magpie[0][2]))), (magpie[0][3], magpie[0][4]))
        if effects[10][1] == 'true':
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(magpie[1][0]))),
                                       (int(magpie[1][1]), int(magpie[1][2]))), (magpie[1][3], magpie[1][4]))
    cursor.execute("SELECT max_health_point, health_point FROM enemy WHERE activity = 'true'")
    enemyHP = cursor.fetchall()
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    pygame.draw.rect(screen, (255, 0, 0), (86, 541, int(140/maxPlayerHP*playerHP[0][0]), 31))
    if len(enemyHP) != 0 and mobName != 'Chest' and mobName != 'Chest(open)':
        pygame.draw.rect(screen, (255, 0, 0), (817, 541, int(140/enemyHP[0][0]*enemyHP[0][1]), 31))
    cursor.execute("SELECT max_step_count FROM game_level WHERE id_game_level = " + str(level))
    maxCount = cursor.fetchall()
    maxCount = maxCount[0][0]
    if count > 0:
        pygame.draw.rect(screen, (0, 0, 0), (203, 30, int(600/maxCount*count), 30))

    if len(enemyHP) != 0 and mobName != 'Chest' and mobName != 'Chest(open)':
        text = textFont.render(str(int(enemyHP[0][1])), True, (0, 0, 0))
        screen.blit(text, (870, 545))
    text = textFont.render(str(int(playerHP[0][0])), True, (0, 0, 0))
    screen.blit(text, (135, 545))

    # ЭФФЕКТЫ И КАРТЫ
    cursor.execute("SELECT COUNT(*) FROM effect")
    effectsCount = cursor.fetchall()
    effectsCount = effectsCount[0][0]
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'effect'")
    data = cursor.fetchall()
    i = 1
    while i < effectsCount:
        if effects[i][1] == 'true':
            if effects[i][0] == 'Bleeding':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                                   (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
            if effects[i][0] == 'Burning':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[1][0]))),
                                                   (int(data[1][1]), int(data[1][2]))), (data[1][3], data[1][4]))
            if effects[i][0] == 'Bite':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[2][0]))),
                                                   (int(data[2][1]), int(data[2][2]))), (data[2][3], data[1][4]))
            if effects[i][0] == 'Vampirism':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[3][0]))),
                                                   (int(data[3][1]), int(data[3][2]))), (data[3][3], data[3][4]))
            if effects[i][0] == 'Repulse':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[4][0]))),
                                                   (int(data[4][1]), int(data[4][2]))), (data[4][3], data[4][4]))
            if effects[i][0] == 'Shield':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[5][0]))),
                                                   (int(data[5][1]), int(data[5][2]))), (data[5][3], data[5][4]))
            if effects[i][0] == 'Freezing':
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[6][0]))),
                                                   (int(data[6][1]), int(data[6][2]))), (data[6][3], data[6][4]))
            if effects[i][0] == 'Bottle':
                cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE purpose = 'bottle' ORDER BY id_image ASC")
                bottle = cursor.fetchall()
                step = effects[i][2]
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(bottle[step][0]))),
                                                   (int(bottle[step][1]), int(bottle[step][2]))), (bottle[step][3], bottle[step][4]))

        i += 1

    cursor.execute("SELECT id_card, image.path, image.width, image.height FROM card INNER JOIN image ON card.id_image = image.id_image WHERE card.usability = 'used'")
    data = cursor.fetchall()
    i = 0
    while i < 4:
        if active[i][1] == 'true':
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[active[i][2]][1]))),
                                               (int(data[active[i][2]][2]), int(data[active[i][2]][3]))), pos[i])
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(noCard[0][0]))), (int(noCard[0][1]), int(noCard[0][2]))), pos[i])
        i += 1

    #posMob = pygame.Rect(0, 70, 800, 700)
    #pygame.draw.rect(screen, (0, 0, 0), posMob)


# отдельно прорисовка дерева талантов
def drawTalentTree():
    cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE id_image = 35")
    data = cursor.fetchall()
    cursor.execute("SELECT experience FROM player_state WHERE id_player = " + str(idPlayer))
    exp = cursor.fetchall()
    screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))), (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
    text = textFont.render(str(int(exp[0][0]/10)), True, (0, 0, 0))
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
def Fill(active):
    number = -1
    cursor.execute("SELECT COUNT(id_card) AS cardCount FROM card WHERE usability = 'used'")
    cardCount = cursor.fetchall()
    cardCount = cardCount[0][0]
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

    return active

def damageInShield(strength, dmg):
    if strength == 20:
        dmg = dmg*20/100
    elif strength == 15:
        dmg = dmg*30/100
    elif strength == 10:
        dmg = dmg*40/100
    elif strength == 5:
        dmg = dmg*50/100
    cursor.execute("UPDATE effect SET activity = 'false' WHERE name = 'Shield'")
    cnxn.commit()

    return dmg

def repulse(strength, dmg):
    if strength == 20:
        dmg = dmg*20/100
    elif strength == 15:
        dmg = dmg*30/100
    elif strength == 10:
        dmg = dmg*40/100
    elif strength == 5:
        dmg = dmg*50/100
    cursor.execute("UPDATE effect SET activity = 'false' WHERE name = 'Repulse'")
    cnxn.commit()

    return dmg

def printHP(fight, sEnemyHP, sPlayerHP):
    hpM = textFont.render('', True, (255, 0, 0))
    hpP = textFont.render('', True, (255, 0, 0))
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    if fight == True:
        cursor.execute("SELECT health_point, max_health_point, name FROM enemy WHERE activity = 'true'")
        enemy = cursor.fetchall()
        if enemy[0][0] == 0:
            enemyHP = enemy[0][1]
        else:
            enemyHP = enemy[0][0]
        if enemyHP < sEnemyHP:
            hpM = textFont.render('-' + str(sEnemyHP - enemyHP), True, (255, 0, 0))
        if playerHP < sPlayerHP:
            hpP = textFont.render('-' + str(sPlayerHP - playerHP), True, (255, 0, 0))
        #if playerHP > sPlayerHP:
        #    hpP = textFont.render('+' + str(playerHP - sPlayerHP), True, (0, 255, 0))
        if enemy[0][2] != 'Chest':
            place = hpM.get_rect(center=(860, 330))
            screen.blit(hpM, place)
            place = hpP.get_rect(center=(134, 330))
            screen.blit(hpP, place)
            sPlayerHP = playerHP
            sEnemyHP = enemyHP

    return sEnemyHP, sPlayerHP

def talentCard(number):
    if number != 5:
        cursor.execute("UPDATE card SET usability = 'used' WHERE id_talent = " + str(number))
        cnxn.commit()
    cursor.execute("UPDATE talent SET activity = 'active' WHERE id_talent = " + str(number))
    cnxn.commit()

def playerMove(card, number):
    cursor.execute("SELECT health_point FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT name, activity, strength, step_count FROM effect ORDER BY id_effect ASC")
    effects = cursor.fetchall()
    if effects[0][0] == 'Bleeding' and effects[0][1] == 'true':
        enemyHP = tickingEffectCount(enemyHP, effects[0][3])
        if effects[0][3] == 5:
            cursor.execute("UPDATE effect SET activity = 'false', strength = 0, step_count = 0 WHERE name = 'Bleeding'")
        else:
            cursor.execute("UPDATE effect SET step_count = " + str(effects[0][3] + 1) +" WHERE name = 'Bleeding'")
    if effects[1][0] == 'Burning' and effects[1][1] == 'true':
        enemyHP = tickingEffectCount(enemyHP, effects[1][3])
        if effects[1][3] == 5:
            cursor.execute("UPDATE effect SET activity = 'false', strength = 0, step_count = 0 WHERE name = 'Burning'")
        else:
            cursor.execute("UPDATE effect SET step_count = " + str(effects[1][3] + 1) + " WHERE name = 'Burning'")
    if effects[4][0] == 'Vampirism' and effects[4][1] == 'true':
        vampirism(effects[4][2], number, playerHP)
        if effects[1][3] == 3:
            cursor.execute("UPDATE effect SET activity = 'false', strength = 0, step_count = 0 WHERE name = 'Vampirism'")
        else:
            cursor.execute("UPDATE effect SET step_count = " + str(effects[4][3] + 1) + " WHERE name = 'Vampirism'")
    if card == 'blood':
        if effects[0][0] == 'Bleeding' and effects[0][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + ", step_count = 0 WHERE name = 'Bleeding'")
    if card == 'fire':
        if effects[1][0] == 'Burning' and effects[1][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + ", step_count = 0 WHERE name = 'Burning'")
    if card == 'shield':
        if effects[3][0] == 'Bleeding' and effects[3][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + " WHERE name = 'Shield'")
    if card == 'repulse':
        if effects[5][0] == 'Repulse' and effects[5][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + " WHERE name = 'Repulse'")
    if card == 'freeze':
        if effects[6][0] == 'Freezing' and effects[6][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + " WHERE name = 'Freezing'")
    if card == 'heal':
        heal = 0
        if number == 20:
            heal = 50
        elif number == 15:
            heal = 40
        elif number == 10:
            heal = 30
        elif number == 5:
            heal = 20
        if playerHP + heal > 100:
            playerHP = 100
        else:
            playerHP += heal
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
    if card == 'vamp':
        if effects[4][0] == 'Vampirism' and effects[4][1] == 'false':
            cursor.execute("UPDATE effect SET activity = 'true', strength = " + str(number) + ", step_count = 0 WHERE name = 'Vampirism'")
        vampirism(number, number, playerHP)
    if card == 'blood' or card == 'fire' or card == 'atk' or card == 'vamp' or card == 'freeze':
        if effects[9][1] == 'false' and effects[10][1] == 'false':
            if enemyHP - number < 0:
                enemyHP = 0
            else:
                enemyHP -= number
    cursor.execute("UPDATE enemy SET health_point = " + str(enemyHP) + " WHERE activity = 'true'")

    if enemyHP == 0:
        cursor.execute("UPDATE effect SET activity = 'false', strength = 0, step_count = 0 WHERE id_effect <> 9")

    cnxn.commit()

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

def vampirism(strength, atk, playerHP):
    heal = playerHP
    if strength == 5:
        heal += int(atk*0,4)
    elif strength == 10:
        heal += int(atk * 0,5)
    elif strength == 15:
        heal += int(atk * 0,6)
    elif strength == 20:
        heal += int(atk * 0,7)
    cursor.execute("UPDATE player_state SET health_point = " + str(heal) + " WHERE id_player = " + str(idPlayer))
    cnxn.commit()

def checkStep(count, fight, player, level):
    cursor.execute("SELECT enemy.name, enemy_emergence.emergence_count, enemy.max_health_point, enemy_emergence.passed FROM enemy INNER JOIN enemy_emergence ON enemy.id_enemy = enemy_emergence.id_enemy WHERE enemy.id_game_level = " + str(level))
    enemySpawn = cursor.fetchall()
    N = len(enemySpawn)
    #cursor.execute("SELECT COUNT(*) FROM enemy_emergence AS count_enemy_spawn")
    #N = cursor.fetchall()
    #N = N[0][0]
    i = 1
    name = None
    if fight == False:
        while i <= N:
            if count == enemySpawn[i-1][1] and enemySpawn[i-1][3] == 'false':
                fight = True
                player = True
                name = enemySpawn[i-1][0]
                cursor.execute("UPDATE enemy SET health_point = " + str(enemySpawn[i-1][2]) + ", activity = 'true' WHERE name = '" + str(name) + "' and id_game_level = " + str(level))
                cnxn.commit()
            i += 1
    return fight, player, name

def checkPlayerHP(endOfTheGame):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    if playerHP <= 0:
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE name = 'Lose'")
        data = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                           (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
        endOfTheGame = True

    return endOfTheGame

loseMenu = pygame.Rect(250, 470, 150, 90)
loseAgain = pygame.Rect(565, 465, 90, 90)
def loseTransition(mousePos, run):
    if loseMenu.collidepoint(mousePos):
        menu.running()
    if loseAgain.collidepoint(mousePos):
        cursor.execute("SELECT id_game_level FROM player WHERE id_player = " + str(idPlayer))
        data = cursor.fetchall()
        if len(data) != 0:
            level = data[0][0]
        else:
            level = 1
        if level == 1:
            level1.running()
        if level == 2:
            level2.running()
    run = False

    return run

winMenu = pygame.Rect(250, 470, 150, 90)
winNext = pygame.Rect(565, 465, 270, 90)
def winTransition(mousePos, run, level):
    if level == 1:
        cursor.execute("UPDATE player SET id_game_level = 2 WHERE id_player = " + str(idPlayer))
        cnxn.commit()
    if winMenu.collidepoint(mousePos):
        menu.running()
    if winNext.collidepoint(mousePos):
        cursor.execute("SELECT id_game_level FROM player WHERE id_player = " + str(idPlayer))
        data = cursor.fetchall()
        if len(data) != 0:
            level = data[0][0]
        else:
            level = 1
        if level == 1:
            level1.running()
        if level == 2:
            level2.running()
    run = False

    return run

def checkButtons(active, count, mousePos, treeAct, transition, choiceT, enemyName, openChest, level):
    menu, tree = posButtons()
    if (choiceT == False) and (enemyName == None or (enemyName == 'Chest' and openChest == True)):
        if tree.collidepoint(mousePos) and treeAct == False:
            treeAct = True
            drawTalentTree()
        elif tree.collidepoint(mousePos) and treeAct == True:
            treeAct = False
            drawBack(active, count, None, level)
    if menu.collidepoint(mousePos):
        cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE name = 'transitionToMenu'")
        data = cursor.fetchall()
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                           (int(data[0][1]), int(data[0][2]))), (data[0][3], data[0][4]))
        transition = True

    return treeAct, transition

posYes = pygame.Rect(250, 470, 150, 90)
posNo = pygame.Rect(625, 465, 150, 90)
def toMenu(mousePos, run, transition, active, count, level):
    if posYes.collidepoint(mousePos):
        run = False
        menu.running()
    if posNo.collidepoint(mousePos):
        transition = False
        drawBack(active, count, None, level)
    return run, transition

def talentTree(mousePos, choiceT, talentID):
    cursor.execute("SELECT id_talent, posX, posY, required_level, activity FROM talent")
    talent = cursor.fetchall()
    if choiceT == False:
        i = 0
        while i < len(talent):
            talentPos = pygame.Rect(talent[i][1], talent[i][2], 90, 85)
            if talentPos.collidepoint(mousePos):
                choiceTalent(talent[i][0])
                talentID = talent[i][0] - 1
                choiceT = True
            i += 1
    if choiceT == True:
        yesButtonPos = pygame.Rect(350, 470, 140, 60)
        noButtonPos = pygame.Rect(515, 470, 140, 60)
        cursor.execute("SELECT experience, max_experience FROM player_state WHERE id_player = " + str(idPlayer))
        exp = cursor.fetchall()
        if yesButtonPos.collidepoint(mousePos) and int(exp[0][0] / 10) > 0 and int((exp[0][1] + 10) / 10) >= talent[talentID][3] and talent[talentID][4] == 'inactive':
            talentCard(talentID+1)
            cursor.execute("UPDATE player_state SET experience = " + str(exp[0][0] - 10) + " WHERE id_player = " + str(idPlayer))
            drawTalentTree()
            choiceT = False
            if talentID == 4:
                cursor.execute("UPDATE effect SET activity = 'true' WHERE name = 'CleverTrick'")
            cnxn.commit()
        if noButtonPos.collidepoint(mousePos):
            choiceT = False
            drawTalentTree()

    return choiceT, talentID

countAct = 0
def cardManipulation(mousePos, pos, active, count, fight, player, mob, act, win, level):
    global countAct
    i = 0
    while i < 4:
        if pos[i].collidepoint(mousePos):
            if active[i][1] == 'true':
                active[i][1] = 'false'
                cursor.execute("SELECT point, type FROM card WHERE id_card = " + str(active[i][0] + 1))
                point = cursor.fetchall()
                screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(noCard[0][0]))),
                                                   (int(noCard[0][1]), int(noCard[0][2]))), pos[i])
                cursor.execute("SELECT activity, step_count FROM effect WHERE name = 'Bottle'")
                bottle = cursor.fetchall()
                if bottle[0][0] == 'true' and bottle[0][1] < 5:
                    cursor.execute("UPDATE effect SET step_count = " + str(bottle[0][1] + 1) + " WHERE name = 'Bottle'")
                    cnxn.commit()
                cursor.execute("SELECT max_step_count FROM game_level WHERE id_game_level = " + str(level))
                maxCount = cursor.fetchall()
                maxCount = maxCount[0][0]
                if not fight:
                    if count + int(point[0][0]) > maxCount:
                        count = maxCount
                    else:
                        count += int(point[0][0])
                    drawBack(active, count, None, level)

                if fight:
                    if player:
                        cursor.execute("SELECT experience, max_experience FROM player_state WHERE id_player = " + str(idPlayer))
                        playerState = cursor.fetchall()
                        mob = True
                        player = False
                        playerMove(point[0][1], int(point[0][0]))
                        cursor.execute("SELECT health_point, experience, name FROM enemy WHERE activity = 'true'")
                        enemyState = cursor.fetchall()
                        if enemyState[0][0] == 0 and enemyState[0][2] != 'Chest':
                            if enemyState[0][2] != 'Alice':
                                cursor.execute("UPDATE player_state SET experience = " + str(int(playerState[0][0] + enemyState[0][1])) + ", max_experience = " + str(int(playerState[0][1] + enemyState[0][1])) + " WHERE id_player = " + str(idPlayer))
                                fight = False
                                cursor.execute("UPDATE enemy_emergence SET passed = 'true' WHERE emergence_count = " + str(count))
                                cursor.execute("UPDATE enemy SET activity = 'false'")
                                drawBack(active, count, None, level)
                            if count != maxCount:
                                text = textFont.render('Вы получили ' + str(enemyState[0][1]) + ' опыта!', True, (0, 0, 0))
                                place = text.get_rect(center=(500, 80))
                                screen.blit(text, place)
                            else:
                                cursor.execute("SELECT path, width, height, posX, posY FROM image WHERE name = 'win'")
                                data = cursor.fetchall()
                                screen.blit(
                                    pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                                           (int(data[0][1]), int(data[0][2]))),(data[0][3], data[0][4]))
                                win = True
                                break
                        cursor.execute("SELECT activity FROM effect WHERE name = 'Freezing'")
                        freeze = cursor.fetchall()
                        freeze = freeze[0][0]
                        if freeze == 'true':
                            mob = False
                            player = True
                            cursor.execute("UPDATE effect SET activity = 'false' WHERE name = 'Freezing'")
                            cnxn.commit()
        if active[i][1] == 'true':
            act = True
            countAct += 1
        i = i + 1
    if countAct < 2:
        cursor.execute("SELECT activity FROM effect WHERE name = 'CleverTrick'")
        effect = cursor.fetchall()
        if effect[0][0] == 'true':
            act = False
    countAct = 0
    if act == False and win == False:
        Fill(active)

    return active, act, fight, mob, player, count, win

def ifShield(punch, hp):
    cursor.execute("SELECT activity, strength FROM effect WHERE name = 'Shield'")
    shield = cursor.fetchall()
    if shield[0][0] == 'true':
        punch = damageInShield(shield[0][1], punch)
    cursor.execute("SELECT activity, strength FROM effect WHERE name = 'Repulse'")
    rep = cursor.fetchall()
    if rep[0][0] == 'true':
        if hp - int(hp * 0.5) < 0:
            hp = 0
        else:
            hp -= int(hp * 0.5)
        punch = repulse(rep[0][1], punch)
        cursor.execute("UPDATE enemy SET health_point = " + str(hp) + " WHERE activity = 'true'")
        cnxn.commit()
    return punch

def bottleCheck(active, count, mousePos, laught, angry, punch, level):
    cursor.execute("SELECT activity, step_count FROM effect WHERE name = 'Bottle'")
    bottle = cursor.fetchall()
    cursor.execute("SELECT width, height, posX, posY FROM image WHERE purpose = 'bottle' ORDER BY id_image ASC")
    data = cursor.fetchall()
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    hp = cursor.fetchall()
    hp = hp[0][0]
    pos = pygame.Rect(data[0][2], data[0][3], data[0][0], data[0][1])
    if bottle[0][0] == 'true' and bottle[0][1] == 5 and pos.collidepoint(mousePos):
        if hp + 20 <= 200:
            hp += 20
        else:
            hp = 200
        cursor.execute("UPDATE effect SET step_count = 0 WHERE name = 'Bottle'")
        cursor.execute("UPDATE player_state SET health_point = " + str(hp) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        cursor.execute("SELECT name, type FROM enemy WHERE activity = 'true'")
        enemy = cursor.fetchall()
        if len(enemy) != 0:
            name = enemy[0][0]
            if enemy[0][1] != 'Alice':
                drawBack(active, count, name, level)
            else:
                if enemy[0][0] == 'Alice':
                    if punch == True:
                        drawBack(active, count, 'Alice(angry)', 1)
                    elif angry == True:
                        drawBack(active, count, 'Alice(angry)', 1)
                    elif laught == True:
                        drawBack(active, count, 'Alice(laughs)', 1)
                    else:
                        drawBack(active, count, 'Alice', 1)
        else:
            drawBack(active, count, None, level)

    # _________________________________ФУНКЦИИ БОЕВ ВСЕХ МОНСТРОВ_____________________________ #
def fightAlice(active, count, laught, angry, normal, punch):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    AliceState = cursor.fetchall()
    AliceHP = AliceState[0][0]
    AliceDMG = AliceState[0][1]
    AlicePunch = AliceDMG
    text = textFont.render('', True, (0, 0, 0))
    if angry == True:
        if random.randint(1, 100) > 50:
            laught = True
            angry = False
            AlicePunch = 0
            text = textFont.render('Алиса смеется над тобой', True, (0, 0, 0))
        else:
            angry = False
            punch = True
            text = textFont.render('Алиса ударила со всей силы)', True, (255, 0, 0))
            AlicePunch = 30
    elif angry == False and AliceHP < 200:
        if random.randint(1, 100) > 70:
            angry = True
            normal = False
            text = textFont.render('Алиса начинает злиться', True, (0, 0, 0))
    if AliceHP > 0:
        if playerHP - AlicePunch < 0:
            playerHP = 0
        else:
            playerHP -= AlicePunch
    cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
    cnxn.commit()
    if AliceHP > 0:
        if normal == True:
            drawBack(active, count, 'Alice', 1)
        elif punch == True:
            drawBack(active, count, 'Alice(angry)', 1)
            normal = True
            punch = False
        elif angry == True:
            drawBack(active, count, 'Alice(angry)', 1)
        elif laught == True:
            drawBack(active, count, 'Alice(laughs)', 1)
            normal = True
            laught = False
        place = text.get_rect(center=(500, 80))
        screen.blit(text, place)
        ifShield(AlicePunch, AliceHP)

    return laught, angry, normal, punch

def fightSlime(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    ifShield(enemyDMG, enemyHP)
    if enemyHP > 0:
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        drawBack(active, count, 'Slime', 1)

def fightDog(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    cursor.execute("SELECT activity, step_count FROM effect WHERE name = 'Bite'")
    bite = cursor.fetchall()
    if enemyHP > 0:
        if bite[0][0] == 'false':
            if random.randint(1, 100) > 50:
                cursor.execute("UPDATE effect SET activity = 'true', step_count = 0 WHERE name = 'Bite'")
                bite[0][0] = 'true'
        else:
            enemyDMG += 3
            cursor.execute("UPDATE effect SET step_count = " + str(bite[0][1] + 1) + " WHERE name = 'Bite'")
            if bite[0][1] == 2:
                cursor.execute("UPDATE effect SET activity = 'false', step_count = 0 WHERE name = 'Bite'")
        ifShield(enemyDMG, enemyHP)
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        drawBack(active, count, 'Dog', 1)
        if bite[0][0] == 'true':
            text = textFont.render('Бешеный пес укусил Вас!(получение урона +5)', True, (255, 0, 0))
            place = text.get_rect(center=(500, 80))
            screen.blit(text, place)

def openChest(active, count, anim, opened, fight, level):
    if anim == False:
        drawBack(active, count, 'Chest(open)', level)
        text = textFont.render('Вы получили зелье здоровья! Оно восполняется 5 ходов.', True, (0, 0, 0))
        place = text.get_rect(center=(500, 80))
        screen.blit(text, place)
        anim = True
    else:
        opened = True
        cursor.execute("SELECT id_enemy_emergence FROM enemy_emergence INNER JOIN enemy ON enemy.id_enemy = enemy_emergence.id_enemy WHERE name = 'Chest' and id_game_level = " + str(level))
        idEmergence = cursor.fetchall()
        idEmergence = idEmergence[0][0]
        cursor.execute("UPDATE enemy_emergence SET passed = 'true' WHERE id_enemy_emergence = " + str(idEmergence))
        cursor.execute("UPDATE enemy SET activity = 'false'")
        cursor.execute("UPDATE effect SET activity = 'true' WHERE name = 'Bottle'")
        cnxn.commit()
        drawBack(active, count, None, level)
        fight = False

    return anim, opened, fight

def fightBullfinch(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    ifShield(enemyDMG, enemyHP)
    if enemyHP > 0:
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        drawBack(active, count, 'Bullfinch', 2)

def fightHen(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    enemyDMG = enemyDMG * random.randint(1, 3)
    ifShield(enemyDMG, enemyHP)
    if enemyHP > 0:
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        drawBack(active, count, 'Hen', 2)

def fightOwl(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    cursor.execute("SELECT activity, step_count FROM effect WHERE name = 'Dark'")
    dark = cursor.fetchall()
    if enemyHP > 0:
        if dark[0][0] == 'false':
            if random.randint(1, 100) > 70:
                cursor.execute("UPDATE effect SET activity = 'true', step_count = 0 WHERE name = 'Dark'")
                dark[0][0] = 'true'
        else:
            cursor.execute("UPDATE effect SET step_count = " + str(dark[0][1] + 1) + " WHERE name = 'Dark'")
            if dark[0][1] == 2:
                cursor.execute("UPDATE effect SET activity = 'false', step_count = 0 WHERE name = 'Dark'")
        ifShield(enemyDMG, enemyHP)
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        if dark[0][0] == 'true' and dark[0][1] < 2:
            text = textFont.render('Наступает темнота', True, (255, 0, 0))
            place = text.get_rect(center=(500, 80))
            screen.blit(text, place)
        drawBack(active, count, 'Owl', 2)

def fightMagpie(active, count):
    cursor.execute("SELECT health_point FROM player_state WHERE id_player = " + str(idPlayer))
    playerHP = cursor.fetchall()
    playerHP = playerHP[0][0]
    cursor.execute("SELECT health_point, normal_damage, max_health_point FROM enemy WHERE activity = 'true'")
    enemyState = cursor.fetchall()
    enemyHP = enemyState[0][0]
    enemyDMG = enemyState[0][1]
    cursor.execute("SELECT activity, step_count FROM effect WHERE name = 'Dark'")
    fly = cursor.fetchall()
    if enemyHP > 0:
        if fly[0][0] == 'false' and enemyHP < enemyState[0][2]:
            if random.randint(1, 100) > 80:
                cursor.execute("UPDATE effect SET activity = 'true', step_count = 0 WHERE name = 'Fly'")
                fly[0][0] = 'true'
        elif fly[0][0] == 'true':
            cursor.execute("UPDATE effect SET step_count = " + str(fly[0][1] + 1) + " WHERE name = 'Fly'")
            if fly[0][1] == 2:
                cursor.execute("UPDATE effect SET activity = 'false', step_count = 0 WHERE name = 'Fly'")
        ifShield(enemyDMG, enemyHP)
        enemyDMG = enemyDMG * random.randint(1, 4)
        if playerHP - enemyDMG < 0:
            playerHP = 0
        else:
            playerHP -= enemyDMG
        cursor.execute("UPDATE player_state SET health_point = " + str(playerHP) + " WHERE id_player = " + str(idPlayer))
        cnxn.commit()
        drawBack(active, count, 'Magpie', 2)
        if fly[0][0] == 'true' and fly[0][1] < 2:
            text = textFont.render('Сорока взлетает в небо', True, (255, 0, 0))
            place = text.get_rect(center=(500, 80))
            screen.blit(text, place)