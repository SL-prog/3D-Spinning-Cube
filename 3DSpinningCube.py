import pygame
from pygame.locals import *
from math import cos, sin
pygame.init()

fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("3D Spinning Cube")
done = False

SIZE = 40
SCALE = 1
ANGLEX = 0
ANGLEY = 0
ANGLEZ = 0
MOVEX = 0
MOVEY = 0
MOVEZ = 0
PIVX = 0
PIVY = 0
PIVZ = 0

I=60
X=[0]*8
Y=[0]*8
Z=[0]*8

X[0] = I
Y[0] = I
Z[0] =-I

X[1] = I
Y[1] = I
Z[1] = I

X[2] = I
Y[2] =-I
Z[2] =-I

X[3] = I
Y[3] =-I
Z[3] = I

X[4] =-I
Y[4] = I
Z[4] =-I

X[5] =-I
Y[5] = I
Z[5] = I

X[6] =-I
Y[6] =-I
Z[6] =-I

X[7] =-I
Y[7] =-I
Z[7] = I

pygame.key.set_repeat(100,1)
while not(done):
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
#--------------------------------------------
            if event.key == K_LEFT:
                MOVEX -= 2

            if event.key == K_RIGHT:
                MOVEX += 2

            if event.key == K_UP:
                MOVEY -= 2

            if event.key == K_DOWN:
                MOVEY += 2
#--------------------------------------------
            if event.key == K_v:
                SCALE = SCALE*1.02

            if event.key == K_b:
                SCALE = SCALE/1.02
#--------------------------------------------

            if event.key == K_f:
                PIVX -= 2

            if event.key == K_h:
                PIVX += 2

            if event.key == K_t:
                PIVY -= 2

            if event.key == K_g:
                PIVY += 2
#--------------------------------------------
            if event.key == K_1:
                ANGLEZ -= 1

            if event.key == K_2:
                ANGLEZ += 1

            if event.key == K_3:
                ANGLEY -= 1

            if event.key == K_4:
                ANGLEY += 1

            if event.key == K_5:
                ANGLEX -= 1

            if event.key == K_6:
                ANGLEX += 1

#--------------------------------------------
    pygame.draw.rect(fenetre, (0,0,0), (0,0,fenetre.get_width(),fenetre.get_height()), 0)

    for n in range (0,8):
        XD = X[n] - PIVX
        YD = Y[n] - PIVY
        ZD = Z[n] - PIVZ

        ZX = XD*cos(ANGLEZ) - YD*sin(ANGLEZ) - XD
        ZY = XD*sin(ANGLEZ) + YD*cos(ANGLEZ) - YD

        YX = (XD+ZX)*cos(ANGLEZ) - ZD*sin(ANGLEY) - (XD+ZX)
        YZ = (XD+ZX)*sin(ANGLEY) + ZD*cos(ANGLEY) - ZD

        XY = (YD+ZY)*cos(ANGLEX) - (ZD+YZ)*sin(ANGLEX) - (YD+ZY)
        XZ = (YD+ZY)*sin(ANGLEX) + (ZD+YZ)*cos(ANGLEX) - (ZD+YZ)

        XROTOFFSET = YX+ZX
        YROTOFFSET = ZY+XY
        ZROTOFFSET = XZ+YZ

        XDISP = (X[n]+XROTOFFSET)/SCALE + MOVEX
        YDISP = (Y[n]+YROTOFFSET)/SCALE + MOVEY

        pygame.draw.ellipse(fenetre, (255,255,255), (XDISP+400, YDISP+300, SIZE/SCALE, SIZE/SCALE), 0)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()