import pygame
import sys
import random
pygame.init()

class myChick():
    def __init__(self, player, x, y, vel):
        self.player = player
        self.x = x
        self.y = y
        self.vel = vel

    def drawChick(self, win):
        win.blit(self.player, (self.x, self.y))

    def reset(self):
        self.x = 400
        self.y = 410

class vehicle():
    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.hitbox = (self.x-2, self.y+2, 33, 23)
    
    def drawVehicle(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        self.hitbox = (self.x-2, self.y+2, 33, 23)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        self.moveVehicle()

    def moveVehicle(self):
        if self.x > 0:
            self.x -= self.vel
        else:
            self.x = 500
    
    def reset(self, x, y):
        self.x = x
        self.y = y

def drawCenterLine(win, myCX1, myCX2, myY):
    for i in range(20):
        if ((myCX1 <= 500) and (myCX2 <= 500)):
            pygame.draw.line(win, (255,255,255), (myCX1,myY), (myCX2,myY), 7)
            myCX1 = myCX2 + 10
            myCX2 = myCX1 + 20

def redrawWindow(win):
    global winwidth,myT1V1,myT1V2,myT1V3,myT1V4,myT2V5,myT2V6,myT2V7,myT2V8,myT3V9,myT3V10,myT3V11,myT3V12,man,font,score
    win.fill((0,255,0))
    text = font.render("Score: " + str(score), 1, (0,0,0))
    win.blit(text, (390,10))
    pygame.draw.line(win, (0,0,0), (0,380), (500,380), 80)
    drawCenterLine(win, 0, 20, 380)
    pygame.draw.line(win, (0,0,0), (0,250), (500,250), 80)
    drawCenterLine(win, 0, 20, 250)
    pygame.draw.line(win, (0,0,0), (0,120), (500,120), 80)
    drawCenterLine(win, 0, 20, 120)

    myT1V1.drawVehicle(win)
    myT1V2.drawVehicle(win)
    myT1V3.drawVehicle(win)
    myT1V4.drawVehicle(win)
    myT2V5.drawVehicle(win)
    myT2V6.drawVehicle(win)
    myT2V7.drawVehicle(win)
    myT2V8.drawVehicle(win)
    myT3V9.drawVehicle(win)
    myT3V10.drawVehicle(win)
    myT3V11.drawVehicle(win)
    myT3V12.drawVehicle(win)
    #pygame.draw.rect(win, (255,0,0), (chick_x+17, chick_y+11, 29, 52), 2)
    man.drawChick(win)
    pygame.display.update() 




def main():
    global winwidth,myT1V1,myT1V2,myT1V3,myT1V4,myT2V5,myT2V6,myT2V7,myT2V8,myT3V9,myT3V10,myT3V11,myT3V12,man,font,score
    winWidth = 500
    #winHeight = 500
    roadThickness = 60
    v_width = 30
    v_height = 20
    vehicles = []
    score = 0
    global game_lost
    game_lost = False

    #chicken variables
    chicken = pygame.image.load('img/R1.png')
    chick_x = 360
    chick_y = 420
    chick_vel = 5
    #chick_hit_box = (chick_x+17, chick_y+11, 29, 52)

    #Track1 
    # color
    v1_color = (255,255,0)
    v2_color = (255,0,255)
    v3_color = (0,255,255)
    v4_color = (51,255,51)
    #x,y position
    v1_x, v1_y = round(random.uniform(400,600), 2), round(random.uniform(385,340), 2)
    v2_x, v2_y = round(random.uniform(400,600), 2), round(random.uniform(385,340), 2)
    v3_x, v3_y = round(random.uniform(400,600), 2), round(random.uniform(385,340), 2)
    v4_x, v4_y = round(random.uniform(400,600), 2), round(random.uniform(385,340), 2)

    #Track2 
    # color
    v5_color = (255,255,0)
    v6_color = (255,0,255)
    v7_color = (0,255,255)
    v8_color = (51,255,51)
    #x,y position
    v5_x, v5_y = round(random.uniform(400,600), 2), round(random.uniform(270,225), 2)
    v6_x, v6_y = round(random.uniform(400,600), 2), round(random.uniform(270,225), 2)
    v7_x, v7_y = round(random.uniform(400,600), 2), round(random.uniform(270,225), 2)
    v8_x, v8_y = round(random.uniform(400,600), 2), round(random.uniform(270,225), 2)

    #Track3 
    #x,y position
    v9_x, v9_y = round(random.uniform(400,600), 2), round(random.uniform(136,80), 2)
    v10_x, v10_y = round(random.uniform(400,600), 2), round(random.uniform(136,80), 2)
    v11_x, v11_y = round(random.uniform(400,600), 2), round(random.uniform(136,80), 2)
    v12_x, v12_y = round(random.uniform(400,600), 2), round(random.uniform(136,80), 2)

    font = pygame.font.SysFont("comicsans", 30, True)
    win = pygame.display.set_mode((winWidth, winWidth))
    pygame.display.set_caption("Road Crossing")

    clock = pygame.time.Clock()

    #Track1:vehicle1,2,3,4
    myT1V1 = vehicle(v1_x, v1_y, v_width, v_height, v1_color, 10)
    myT1V2 = vehicle(v2_x, v2_y, v_width, v_height, v2_color, 9)
    myT1V3 = vehicle(v3_x, v3_y, v_width, v_height, v3_color, 7)
    myT1V4 = vehicle(v4_x, v4_y, v_width, v_height, v4_color, 8)
    vehicles.append(myT1V1)
    vehicles.append(myT1V2)
    vehicles.append(myT1V3)
    vehicles.append(myT1V4)
    
    #Track2:vehicle5,6,7,8
    myT2V5 = vehicle(v5_x, v5_y, v_width, v_height, v5_color, 10)
    myT2V6 = vehicle(v6_x, v6_y, v_width, v_height, v6_color, 9)
    myT2V7 = vehicle(v7_x, v7_y, v_width, v_height, v7_color, 7)
    myT2V8 = vehicle(v8_x, v8_y, v_width, v_height, v8_color, 8)
    vehicles.append(myT2V5)
    vehicles.append(myT2V6)
    vehicles.append(myT2V7)
    vehicles.append(myT2V8)
    
    #Track3:vehicle9,10,11,12
    myT3V9 = vehicle(v9_x, v9_y, v_width, v_height, v1_color, 10)
    myT3V10 = vehicle(v10_x, v10_y, v_width, v_height, v2_color, 9)
    myT3V11 = vehicle(v11_x, v11_y, v_width, v_height, v3_color, 7)
    myT3V12 = vehicle(v12_x, v12_y, v_width, v_height, v4_color, 8)
    vehicles.append(myT3V9)
    vehicles.append(myT3V10)
    vehicles.append(myT3V11)
    vehicles.append(myT3V12)
    
    #chicken
    man = myChick(chicken, chick_x, chick_y, chick_vel)

    run = True
    while run:
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if ((keys[pygame.K_LEFT]) and (man.x > man.vel)):
            man.x -= man.vel
        elif ((keys[pygame.K_RIGHT]) and (man.x < 500 - man.vel - 64)):
            man.x += man.vel
        elif ((keys[pygame.K_UP]) and (man.y > man.vel)):
            man.y -= man.vel
        elif ((keys[pygame.K_DOWN]) and (man.y < 500 - man.vel - 64)):
            man.y += man.vel

        for veh in vehicles:
            if man.y <= veh.hitbox[1] and man.y + 55 >= veh.hitbox[1]:
                if man.x + 30 >= veh.hitbox[0] and man.x < veh.hitbox[0] + veh.hitbox[2]:
                    man.reset()
                    myT1V1.reset(v1_x + 20, v1_y)
                    myT1V2.reset(v2_x + 80, v2_y)
                    myT1V3.reset(v3_x + 10, v3_y)
                    myT1V4.reset(v4_x + 50, v4_y)
                    myT2V5.reset(v5_x + 20, v5_y)
                    myT2V6.reset(v6_x + 80, v6_y)
                    myT2V7.reset(v7_x + 10, v7_y)
                    myT2V8.reset(v8_x + 50, v8_y)
                    myT3V9.reset(v9_x + 20, v9_y)
                    myT3V10.reset(v10_x + 80, v10_y)
                    myT3V11.reset(v11_x + 10, v11_y)
                    myT3V12.reset(v12_x + 50, v12_y)
                    score = 0
                    pygame.time.delay(200)
                    break
        
        if man.y + 55 == 350:
            score += 1
        elif man.y + 55 == 230:
            score += 1
        elif man.y + 55 == 110:
            score += 1 

        redrawWindow(win)

main()