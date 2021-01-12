import pygame
import os.path
import function

#from menu import mainMenu

filepath = os.path.dirname(__file__)

pygame.init()

#screen = window.screen

textFont = pygame.font.Font('freesansbold.ttf', 25)
textName = pygame.font.Font('freesansbold.ttf', 20)
textDesc = pygame.font.Font('freesansbold.ttf', 16)

def running():
    function.clearBD()
    pos = function.posCards()
    active = function.createActiveCard()

    # основной цикл
    run = True
    count = 0
    fight = False
    player = False
    mob = True
    treeAct = False
    choiceTalentBool = False
    openChest = False
    animation = False
    function.drawBack(active, count, None, 1)
    transition = False
    enHP = 0
    plHP = 0
    laught = False
    angry = False
    punch = False
    normal = True
    talentID = 0
    lose = False
    win = False
    while run:
        pygame.time.delay(100)
        lose = function.checkPlayerHP(lose)
        if fight == False:
            fight, player, enemyName = function.checkStep(count, fight, player, 1)
        if mob == True and fight == True:
            if enemyName == 'Alice':
                laught, angry, normal, punch = function.fightAlice(active, count, laught, angry, normal, punch)
            elif enemyName == 'Slime':
                function.fightSlime(active, count)
            elif enemyName == 'Dog':
                function.fightDog(active, count)
            if enemyName != 'Chest':
                mob = False
                player = True
        if enemyName == 'Chest' and animation == False:
            function.drawBack(active, count, enemyName, 1)
        enHP, plHP = function.printHP(fight, enHP, plHP)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                act = False
                if lose == False and win == False:
                    function.bottleCheck(active, count, mousePos, laught, angry, punch, 1)
                    if enemyName == 'Chest':
                        animation, openChest, fight = function.openChest(active, count, animation, openChest, fight, 1)

                    if (treeAct == False) and (transition == False) and ((enemyName == 'Chest' and openChest == True) or (enemyName != 'Chest')):
                        active, act, fight, mob, player, count, win = function.cardManipulation(mousePos, pos, active, count,
                                                                                           fight, player, mob, act, win, 1)

                    if fight == False and transition == False:
                        treeAct, transition = function.checkButtons(active, count, mousePos, treeAct, transition, choiceTalentBool, enemyName, openChest, 1)
                        if treeAct == True and transition == False:
                            choiceTalentBool, talentID = function.talentTree(mousePos, choiceTalentBool, talentID)
                    if transition == True:
                        run, transition = function.toMenu(mousePos, run, transition, active, count, 1)
                elif lose == True:
                    run = function.loseTransition(mousePos, run)
                elif win == True:
                    run = function.winTransition(mousePos, run, 1)
        if run:
            pygame.display.update()

    pygame.quit()

if __name__=="__main__":
    running()