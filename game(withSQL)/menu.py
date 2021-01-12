import pyodbc
import pygame
import os.path
import socket
import window
import level1
import level2

ip = socket.gethostbyname(socket.gethostname())

filepath = os.path.dirname(__file__)
server = 'DESKTOP-853A94C'#'HOME2\MSSQLSERVER00'
database = 'gameDB'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

pygame.init()

screen = window.screen
textFont = pygame.font.Font('freesansbold.ttf', 40)

cursor.execute("SELECT path, width, height FROM image WHERE purpose = 'menu'")
data = cursor.fetchall()
newGameButton = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[0][0]))),
                                       (int(data[0][1]), int(data[0][2])))
loadGameButton = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[1][0]))),
                                       (int(data[1][1]), int(data[1][2])))
menuWindow = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[2][0]))),
                                       (int(data[2][1]), int(data[2][2])))
helpButton = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[3][0]))),
                                       (int(data[3][1]), int(data[3][2])))
exitButton = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[4][0]))),
                                       (int(data[4][1]), int(data[4][2])))
enterName = pygame.transform.scale(pygame.image.load(os.path.join(filepath, str(data[5][0]))),
                                       (int(data[5][1]), int(data[5][2])))


def running():
    newPlayer = False
    level = 1
    cursor.execute("SELECT id_game_level FROM player WHERE ip = '" + ip + "'")
    data = cursor.fetchall()
    if not data:
        newPlayer = True
        screen.blit(enterName, (0, 0))
    else:
        level = data[0][0]

    posNewGame = pygame.Rect(320, 120, 200, 110)
    posLoadGame = pygame.Rect(535, 110, 220, 130)
    posHelp = pygame.Rect(330, 250, 440, 70)
    posExit = pygame.Rect(415, 330, 360, 80)
    mainMenu = True
    run = True
    name = ''
    while run:
        #screen.blit(menuWindow, (0, 0))
        #pygame.draw.rect(screen, (0, 0, 0), posExit)
        if mainMenu == True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                mousePos = pygame.mouse.get_pos()
                if newPlayer == False:
                    if posNewGame.collidepoint(mousePos):
                        screen.blit(newGameButton, (0,0))
                    elif posLoadGame.collidepoint(mousePos):
                        screen.blit(loadGameButton, (0, 0))
                    elif posHelp.collidepoint(mousePos):
                        screen.blit(helpButton, (0, 0))
                    elif posExit.collidepoint(mousePos):
                        screen.blit(exitButton, (0, 0))
                    else:
                        screen.blit(menuWindow, (0, 0))
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if posNewGame.collidepoint(mousePos):
                            if level > 1:
                                cursor.execute("UPDATE player SET id_game_level = 1 WHERE ip = '" + ip + "'")
                                cnxn.commit()
                            mainMenu = False
                            level1.running()
                            run = False
                            break
                        elif posLoadGame.collidepoint(mousePos):
                            mainMenu = False
                            if level == 1:
                                level1.running()
                            if level == 2:
                                level2.running()
                            run = False
                            break
                        #elif posHelp.collidepoint(mousePos):
                        #    mainMenu = False
                        elif posExit.collidepoint(mousePos):
                            mainMenu = False
                            run = False
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and name != '':
                            newPlayer = False
                            request = "INSERT [dbo].[player] ([id_game_level], [ip], [username], [strength]) VALUES (" + str(level) + ", '" + str(ip) + "', '" + name + "', 'norm')"
                            cursor.execute(request)
                            cnxn.commit()
                            cursor.execute("SELECT id_player FROM player WHERE ip = '" + ip + "'")
                            id_player = cursor.fetchall()
                            id_player = id_player[0][0]
                            ###УРОВНИ СЛОЖНОСТИ
                            request = "INSERT [dbo].[player_state] ([id_player], [health_point], [experience], [max_experience]) VALUES (" + str(id_player) + ", 150, 0, 0)"
                            cursor.execute(request)
                            cnxn.commit()
                        elif event.key == pygame.K_BACKSPACE:
                            if name != '':
                                name = name[0:-1]
                        elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                            if len(name) < 8:
                                name += event.unicode
                        screen.blit(enterName, (0, 0))
                        text = textFont.render(str(name), True, (0, 0, 0))
                        place = text.get_rect(center=(530, 270))  # 420 168
                        screen.blit(text, place) #460 250
            if mainMenu == True:
                pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__=="__main__":
    running()