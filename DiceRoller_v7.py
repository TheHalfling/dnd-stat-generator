import random, sys, pygame, time
from pygame.locals import *

pygame.init()

FPS = 30
WINDOWWIDTH = 900
WINDOWHEIGHT = 550
RESULTSHEIGHT = 50
RESULTSWIDTH = 75
STATHEIGHT = 50
STATWIDTH = 175
CHOICEBUTTONHEIGHT = 75
CHOICEBUTTONWIDTH = 150
GAPSIZE = 15
XMARGIN = 25
YMARGIN = 75
CHOICE = 0

pygame.font.init()
BASICFONT = pygame.font.SysFont('braddon', 18)
TITLEFONT = pygame.font.SysFont('braddon', 30, bold=True)


# Colors
#                  R    G    B
White          = (255, 255, 255)
Black          = (  0,   0,   0)
RoyalBlue      = ( 65, 105, 225)
DarkBlue       = (  0,  50, 255)
Green          = (  0, 205,   0)
Red            = (200,   0,  50)
bgColor = RoyalBlue


# Rect objects for the dice results & Buttons
RESULTRECT1 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN, RESULTSWIDTH,
                          RESULTSHEIGHT)
RESULTRECT2 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN + RESULTSHEIGHT +
                          GAPSIZE, RESULTSWIDTH, RESULTSHEIGHT)
RESULTRECT3 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN + (2 * RESULTSHEIGHT) +
                          (2 * GAPSIZE), RESULTSWIDTH, RESULTSHEIGHT)
RESULTRECT4 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN + (3 * RESULTSHEIGHT) +
                          (3 * GAPSIZE), RESULTSWIDTH, RESULTSHEIGHT)
RESULTRECT5 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN + (4 * RESULTSHEIGHT) +
                          (4 * GAPSIZE), RESULTSWIDTH, RESULTSHEIGHT)
RESULTRECT6 = pygame.Rect(XMARGIN + STATWIDTH + GAPSIZE, YMARGIN + (5 * RESULTSHEIGHT) +
                          (5 * GAPSIZE), RESULTSWIDTH, RESULTSHEIGHT)
BUTTON1 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN,
                      CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
BUTTON2 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN +
                      GAPSIZE + CHOICEBUTTONHEIGHT, CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
BUTTON3 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN +
                      (2 * GAPSIZE) + (2 * CHOICEBUTTONHEIGHT), CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
BORDER = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, CHOICE

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dice Roller')
    mousex = 0
    mousey = 0
    STAT1 = []
    STAT2 = []
    STAT3 = []
    STAT4 = []
    STAT5 = []
    STAT6 = []
   

    #General & Instruction text 
    infoSurf = BASICFONT.render('Select a rolling method on the right and see your results', 1, Black)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (20, WINDOWHEIGHT - 50)
    titleSurf = TITLEFONT.render('Character Dice Rolling Program', 2, Black)
    titleRect = titleSurf.get_rect()
    titleRect.midleft = (WINDOWHEIGHT / 2, YMARGIN / 2)
    opt1Text = BASICFONT.render('6x - 3d6', 1, Black)
    opt1Rect = opt1Text.get_rect()
    opt1Rect.midleft = (XMARGIN + STATWIDTH + RESULTSWIDTH + CHOICEBUTTONWIDTH + (6.5 * GAPSIZE),
                        YMARGIN + (CHOICEBUTTONHEIGHT / 2))
    opt2Text = BASICFONT.render('6x - 4d6 drop lowest die roll', 1, Black)
    opt2Rect = opt2Text.get_rect()
    opt2Rect.midleft = (XMARGIN + STATWIDTH + RESULTSWIDTH + CHOICEBUTTONWIDTH + (6.5 * GAPSIZE),
                        YMARGIN + CHOICEBUTTONHEIGHT + GAPSIZE +(CHOICEBUTTONHEIGHT / 2))
    opt3Text = BASICFONT.render('7x - 4d6 drop lowest roll and total', 1, Black)
    opt3Rect = opt3Text.get_rect()
    opt3Rect.midleft = (XMARGIN + STATWIDTH + RESULTSWIDTH + CHOICEBUTTONWIDTH + (6.5 * GAPSIZE), YMARGIN +
                        (2 * CHOICEBUTTONHEIGHT) + (2 * GAPSIZE) +(CHOICEBUTTONHEIGHT / 2))
    

    #Stat text
    statText1 = BASICFONT.render('Strength', 1, Black)
    statText1Rect = statText1.get_rect()
    statText1Rect.midleft = (XMARGIN, YMARGIN + (STATHEIGHT / 2))
    statText2 = BASICFONT.render('Dexterity', 1, Black)
    statText2Rect = statText2.get_rect()
    statText2Rect.midleft = (XMARGIN, YMARGIN + STATHEIGHT + GAPSIZE + (STATHEIGHT / 2))
    statText3 = BASICFONT.render('Constitution', 1, Black)
    statText3Rect = statText3.get_rect()
    statText3Rect.midleft = (XMARGIN, YMARGIN + (2 * STATHEIGHT) + (2 * GAPSIZE) + (STATHEIGHT / 2))
    statText4 = BASICFONT.render('Intelligence', 1, Black)
    statText4Rect = statText4.get_rect()
    statText4Rect.midleft = (XMARGIN, YMARGIN + (3 * STATHEIGHT) + (3 * GAPSIZE) + (STATHEIGHT / 2))
    statText5 = BASICFONT.render('Wisdom', 1, Black)
    statText5Rect = statText5.get_rect()
    statText5Rect.midleft = (XMARGIN, YMARGIN + (4 * STATHEIGHT) + (4 * GAPSIZE) + (STATHEIGHT / 2))
    statText6 = BASICFONT.render('Charisma', 1, Black)
    statText6Rect = statText6.get_rect()
    statText6Rect.midleft = (XMARGIN, YMARGIN + (5 * STATHEIGHT) + (5 * GAPSIZE) + (STATHEIGHT / 2))

 
    #Button text
    buttonText1 = BASICFONT.render('Option 1', 1, Black)
    buttonText1Rect = buttonText1.get_rect()
    buttonText1Rect.center = (XMARGIN + STATWIDTH +(2 * RESULTSWIDTH) + (5 * GAPSIZE), YMARGIN + (
                               CHOICEBUTTONHEIGHT / 2))
    buttonText2 = BASICFONT.render('Option 2', 1, Black)
    buttonText2Rect = buttonText1.get_rect()
    buttonText2Rect.center = (XMARGIN + STATWIDTH + (2 * RESULTSWIDTH) + (5 * GAPSIZE), YMARGIN +
                               CHOICEBUTTONHEIGHT + GAPSIZE + (CHOICEBUTTONHEIGHT / 2))
    buttonText3 = BASICFONT.render('Option 3', 1, Black)
    buttonText3Rect = buttonText3.get_rect()
    buttonText3Rect.center = (XMARGIN + STATWIDTH + (2 * RESULTSWIDTH) + (5 * GAPSIZE), YMARGIN +
                               (2 * CHOICEBUTTONHEIGHT) + (2 * GAPSIZE) + (CHOICEBUTTONHEIGHT / 2))
    

    while True: # main program loop
        clickedButton = None #method choice
        DISPLAYSURF.fill(bgColor)
        drawButtons()
        checkForQuit()
        
        for event in pygame.event.get(): #event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
                CHOICE = clickedButton
                      
                if CHOICE == 0:
                    STAT1 = []
                    STAT2 = []
                    STAT3 = []
                    STAT4 = []
                    STAT5 = []
                    STAT6 = []

                elif CHOICE == 1:
                    STAT1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT2 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT3 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT4 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT5 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]

                elif CHOICE == 2:
                    STAT1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT1.remove(min(STAT1))
                    STAT2 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT2.remove(min(STAT2))
                    STAT3 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT3.remove(min(STAT3))
                    STAT4 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT4.remove(min(STAT4))
                    STAT5 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT5.remove(min(STAT5))
                    STAT6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT6.remove(min(STAT6))

                elif CHOICE == 3:
                    STAT1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT1.remove(min(STAT1))
                    STAT2 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT2.remove(min(STAT2))
                    STAT3 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT3.remove(min(STAT3))
                    STAT4 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT4.remove(min(STAT4))
                    STAT5 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT5.remove(min(STAT5))
                    STAT6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT6.remove(min(STAT6))
                    STAT7 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
                    STAT7.remove(min(STAT7))
                    STATLIST = [STAT1, STAT2, STAT3, STAT4, STAT5, STAT6, STAT7]
                    STATLIST.remove(min(STATLIST))
                    STAT1 = STATLIST[0]
                    STAT2 = STATLIST[1]
                    STAT3 = STATLIST[2]
                    STAT4 = STATLIST[3]
                    STAT5 = STATLIST[4]
                    STAT6 = STATLIST[5]

                    
                    

  
            #result text
            if sum(STAT1)!=0:
                color1 = Black
            else:
                color1 = White
                
            resultText1 = BASICFONT.render(str(sum(STAT1)), 1, color1)
            resultText1Rect = resultText1.get_rect()
            resultText1Posx = resultText1Rect.centerx
            resultText1Posy = resultText1Rect.centery
            resultText1Rect.bottomright = (resultText1Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText1Posy + YMARGIN + (RESULTSHEIGHT / 2))
            resultText2 = BASICFONT.render(str(sum(STAT2)), 1, color1)
            resultText2Rect = resultText2.get_rect()
            resultText2Posx = resultText2Rect.centerx
            resultText2Posy = resultText2Rect.centery
            resultText2Rect.bottomright = (resultText2Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText2Posy + YMARGIN + GAPSIZE + STATHEIGHT +(RESULTSHEIGHT / 2))
            resultText3 = BASICFONT.render(str(sum(STAT3)), 1, color1)
            resultText3Rect = resultText3.get_rect()
            resultText3Posx = resultText3Rect.centerx
            resultText3Posy = resultText3Rect.centery
            resultText3Rect.bottomright = (resultText3Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText3Posy + YMARGIN + (GAPSIZE * 2) + (STATHEIGHT * 2) + (RESULTSHEIGHT / 2))
            resultText4 = BASICFONT.render(str(sum(STAT4)), 1, color1)
            resultText4Rect = resultText4.get_rect()
            resultText4Posx = resultText4Rect.centerx
            resultText4Posy = resultText4Rect.centery
            resultText4Rect.bottomright = (resultText4Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText4Posy + YMARGIN + (GAPSIZE * 3) + (STATHEIGHT * 3) + (RESULTSHEIGHT / 2))
            resultText5 = BASICFONT.render(str(sum(STAT5)), 1, color1)
            resultText5Rect = resultText5.get_rect()
            resultText5Posx = resultText5Rect.centerx
            resultText5Posy = resultText5Rect.centery
            resultText5Rect.bottomright = (resultText5Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText5Posy + YMARGIN + (GAPSIZE * 4) + (STATHEIGHT * 4) + (RESULTSHEIGHT / 2))
            resultText6 = BASICFONT.render(str(sum(STAT6)), 1, color1)
            resultText6Rect = resultText6.get_rect()
            resultText6Posx = resultText6Rect.centerx
            resultText6Posy = resultText6Rect.centery
            resultText6Rect.bottomright = (resultText6Posx + XMARGIN + STATWIDTH + GAPSIZE + (RESULTSWIDTH / 2),
                                           resultText6Posy + YMARGIN + (GAPSIZE * 5) + (STATHEIGHT * 5) + (RESULTSHEIGHT / 2))

        # Print text to screen
        DISPLAYSURF.blit(infoSurf, infoRect)
        DISPLAYSURF.blit(statText1, statText1Rect)
        DISPLAYSURF.blit(statText2, statText2Rect)
        DISPLAYSURF.blit(statText3, statText3Rect)
        DISPLAYSURF.blit(statText4, statText4Rect)
        DISPLAYSURF.blit(statText5, statText5Rect)
        DISPLAYSURF.blit(statText6, statText6Rect)
        DISPLAYSURF.blit(buttonText1, buttonText1Rect)
        DISPLAYSURF.blit(buttonText2, buttonText2Rect)
        DISPLAYSURF.blit(buttonText3, buttonText3Rect)
        DISPLAYSURF.blit(titleSurf, titleRect)
        DISPLAYSURF.blit(resultText1, resultText1Rect)
        DISPLAYSURF.blit(resultText2, resultText2Rect)
        DISPLAYSURF.blit(resultText3, resultText3Rect)
        DISPLAYSURF.blit(resultText4, resultText4Rect)
        DISPLAYSURF.blit(resultText5, resultText5Rect)
        DISPLAYSURF.blit(resultText6, resultText6Rect)
        DISPLAYSURF.blit(opt1Text, opt1Rect)
        DISPLAYSURF.blit(opt2Text, opt2Rect)
        DISPLAYSURF.blit(opt3Text, opt3Rect)
        redBoxes(CHOICE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def drawButtons():
    pygame.draw.rect(DISPLAYSURF, DarkBlue, BORDER, 20)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT1)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT2)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT3)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT4)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT5)
    pygame.draw.rect(DISPLAYSURF, White, RESULTRECT6)
    pygame.draw.rect(DISPLAYSURF, Green, BUTTON1)
    pygame.draw.rect(DISPLAYSURF, Green, BUTTON2)                    
    pygame.draw.rect(DISPLAYSURF, Green, BUTTON3)


def getButtonClicked(x, y):
    if BUTTON1.collidepoint( (x, y) ):
        return 1
    elif BUTTON2.collidepoint( (x, y) ):
        return 2
    elif BUTTON3.collidepoint( (x, y) ):
        return 3
    else:
        return 0

def redBoxes(CHOICE):
        if CHOICE == 1:
            BORDER1 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN,
                      CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
            pygame.draw.rect(DISPLAYSURF, Red, BORDER1, 2)
        if CHOICE == 2:
            BORDER2 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN +
                      GAPSIZE + CHOICEBUTTONHEIGHT, CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
            pygame.draw.rect(DISPLAYSURF, Red, BORDER2, 2)
        if CHOICE == 3:
            BORDER3 = pygame.Rect(XMARGIN + STATWIDTH + RESULTSWIDTH + (5 * GAPSIZE), YMARGIN +
                      (2 * GAPSIZE) + (2 * CHOICEBUTTONHEIGHT), CHOICEBUTTONWIDTH, CHOICEBUTTONHEIGHT)
            pygame.draw.rect(DISPLAYSURF, Red, BORDER3, 2)
        else:
            None

if __name__ == '__main__':
    main()
        
