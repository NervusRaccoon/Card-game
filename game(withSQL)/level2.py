import pygame
import function

def running():

    function.clearBD()
    pos = function.posCards()
    active = function.createActiveCard()

    run = True
    count = 0
    fight = False
    player = False
    mob = True
    treeAct = False
    choiceTalentBool = False
    openChest = False
    animation = False
    function.drawBack(active, count, None, 2)
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
            fight, player, enemyName = function.checkStep(count, fight, player, 2)
        if mob == True and fight == True:
            if enemyName == 'Owl':
                function.fightOwl(active, count)
            elif enemyName == 'Bullfinch':
                function.fightBullfinch(active, count)
            elif enemyName == 'Hen':
                function.fightHen(active, count)
            elif enemyName == 'Magpie':
                function.fightMagpie(active, count)
            if enemyName != 'Chest':
                mob = False
                player = True
        if enemyName == 'Chest' and animation == False:
            function.drawBack(active, count, enemyName, 2)
        enHP, plHP = function.printHP(fight, enHP, plHP)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                act = False
                if lose == False and win == False:
                    function.bottleCheck(active, count, mousePos, laught, angry, punch, 2)
                    if enemyName == 'Chest':
                        animation, openChest, fight = function.openChest(active, count, animation, openChest, fight, 2)

                    if (treeAct == False) and (transition == False) and ((enemyName == 'Chest' and openChest == True) or (enemyName != 'Chest')):
                        active, act, fight, mob, player, count, win = function.cardManipulation(mousePos, pos, active, count,
                                                                                           fight, player, mob, act, win, 2)

                    if fight == False and transition == False:
                        treeAct, transition = function.checkButtons(active, count, mousePos, treeAct, transition, choiceTalentBool, enemyName, openChest, 2)
                        if treeAct == True and transition == False:
                            choiceTalentBool, talentID = function.talentTree(mousePos, choiceTalentBool, talentID)
                    if transition == True:
                        run, transition = function.toMenu(mousePos, run, transition, active, count, 2)
                elif lose == True:
                    run = function.loseTransition(mousePos, run)
                elif win == True:
                    run = function.winTransition(mousePos, run, 2)
        if run:
            pygame.display.update()

    pygame.quit()

if __name__=="__main__":
    running()