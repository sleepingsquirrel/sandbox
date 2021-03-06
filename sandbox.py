import pygame,time,random,math
import numpy as np
h = 1000; w=h; d = 100; pw = int(w/d);run = True;barrow = 0;size = 7
pygame.init();window = pygame.display.set_mode((round(w*1.5),w ));clock = pygame.time.Clock();myfont = pygame.font.SysFont('Trebuchet MS', 30)
pixels = np.array([[0 for _ in range(d)]for _ in range(d)]); pixels[1][1] = 4;elm = {0:(0,0,0),1:(50,50,50),2:(0,0,200),3:(219, 211, 187),4:(247, 169, 73),5:(217, 217, 217),6:(25,25,25),7:(54, 63, 70),8:(237, 232, 231),9:(207, 129, 33),10:(151, 214, 190)}
def Reverse(tuples): return tuples[::-1]
def update():
    global pixels
    newpix = pixels.copy()
    for y in Reverse(range(len(pixels))):
        for x in range(len(pixels[0])):
            if pixels[y][x] == 3:
                if y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == 0 : newpix[y+1][x]        = 3;newpix[y][x] = 0
                    elif newpix[y+1][x+mod]    == 0 : newpix[y+1][x+mod]    = 3;newpix[y][x] = 0
                    elif newpix[y+1][x]        == 2: newpix[y+1][x]        = 3;newpix[y][x] = 2
            elif pixels[y][x] == 2:
                if y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == 0 : newpix[y+1][x]        = 2;newpix[y][x]  = 0
                    elif newpix[y+1][x+mod]    == 0 : newpix[y+1][x+mod]    = 2;newpix[y][x]  = 0
                    elif newpix[y][x+mod]      == 0 : newpix[y][x+mod]      = 2;newpix[y][x]  = 0
                    elif newpix[y][x+(mod*-1)] == 0 : newpix[y][x+(mod*-1)] = 2;newpix[y][x]  = 0
            elif pixels[y][x] == 1:
                if 1<y+1 < len(newpix)+1:
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     ==   1: mod*=-1
                    if random.randint(0,1) == 1: pass
                    elif newpix[y-1][x]        == 2 : newpix[y-1][x]        = 1;newpix[y][x] = 2
                    elif newpix[y-1][x]        == 0 : newpix[y-1][x]        = 1;newpix[y][x] = 0
                    elif newpix[y-1][x+mod]    == 0 : newpix[y-1][x+mod]    = 1;newpix[y][x] = 0
                    elif newpix[y][x+mod]      == 0 : newpix[y][x+mod]      = 1;newpix[y][x] = 0
                    elif newpix[y][x+(mod*-1)] == 0 : newpix[y][x+(mod*-1)] = 1;newpix[y][x] = 0
                else:
                    for z in range(3):
                        if x + (z-1) <= 99 and newpix[y][x+(z-2)] == 4: newpix[y][x] = 4
            elif pixels[y][x] == 4:
                if 2<=y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1) == 1: mod*=-1
                    if random.randint(0,2) == 1: pass
                    elif newpix[y-1][x+mod]    == 0 : newpix[y-1][x+mod]    = 4;newpix[y][x]  = 0;continue
                    elif random.randint(0,4) == 1: newpix[y][x] = 0;continue
                    for i in range(3):
                        for z in range(3):
                            temp1 = y+(i-1);temp2 = x+(z-1)
                            if   newpix[temp1][temp2] == 1 and random.randint(1,3)  == 1: newpix[temp1][temp2] = 4;pixels[temp1][temp2] = 4
                            elif newpix[temp1][temp2] == 2 and random.randint(1,3)  == 1: newpix[temp1][temp2] = 5
                            elif newpix[temp1][temp2] == 6 and random.randint(1,3)  == 1: newpix[temp1][temp2] = 4;pixels[temp1][temp2] = 4
                            elif newpix[temp1][temp2] == 7 and random.randint(1,20) == 1: newpix[temp1][temp2] = 9
                            elif newpix[temp1][temp2] == 3 and random.randint(1,20) == 1: newpix[temp1][temp2] = 10
                    if random.randint(0,10) == 1: newpix[y][x] = 0
                elif random.randint(0,3) == 1: newpix[y][x] = 0
            elif pixels[y][x] == 5:
                if 2<=y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     ==   1: mod*=-1
                    if random.randint(0,120) == 1:  newpix[y][x] = 2;continue
                    if random.randint(0,1) == 1:pass
                    elif newpix[y-1][x]           == 2 : newpix[y-1][x]       = 5;newpix[y][x] = 2
                    elif newpix[y-1][x+mod]       == 0 : newpix[y-1][x+mod]    = 5;newpix[y][x] = 0
                    elif newpix[y][x+mod]         == 0 : newpix[y][x+mod]      = 5;newpix[y][x] = 0
                    elif newpix[y][x+(mod*-1)]    == 0 : newpix[y][x+(mod*-1)] = 5;newpix[y][x] = 0
                elif random.randint(0,120) == 1:  newpix[y][x] = 2;continue
            elif pixels[y][x] == 6:
                if y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == 0 : newpix[y+1][x]        = 6;newpix[y][x] = 0
                    elif newpix[y+1][x+mod]    == 0 : newpix[y+1][x+mod]    = 6;newpix[y][x] = 0
                    elif newpix[y+1][x]        == 2: newpix[y+1][x]        = 6;newpix[y][x] = 2
            elif pixels[y][x] == 7:
                if y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y-1][x]         == 2 : newpix[y-1][x]        = 7;newpix[y][x] = 2
                    elif newpix[y+1][x]        == 0 : newpix[y+1][x]        = 7;newpix[y][x]  = 0
                    elif newpix[y+1][x+mod]    == 0 : newpix[y+1][x+mod]    = 7;newpix[y][x]  = 0
                    elif newpix[y][x+mod]      == 0 : newpix[y][x+mod]      = 7;newpix[y][x]  = 0
                    elif newpix[y][x+(mod*-1)] == 0 : newpix[y][x+(mod*-1)] = 7;newpix[y][x]  = 0
            elif pixels[y][x] == 9:
                if y+1 < len(newpix):
                    if x >= len(newpix)-1: x = -1
                    if newpix[y-1][x] != 9 or newpix[y+1][x] != 9 or newpix[y][x-1] != 9 or newpix[y][x+1] != 9:
                        mod = 1
                        if random.randint(0,1) == 1: mod*=-1
                        if random.randint(0,1) == 1: continue
                        elif newpix[y+1][x]    == 0 : newpix[y+1][x]    = 9;newpix[y][x]  = 0 ;continue
                        elif newpix[y+1][x+mod]    == 0 : newpix[y+1][x+mod]    = 9;newpix[y][x]  = 0 ;continue
                        elif random.randint(0,15)   == 1 and newpix[y-  1][x] != 9: newpix[y][x] = 8 ;continue
                        elif random.randint(0,15)   == 1 and newpix[y-  1][x] == 0: newpix[y-  1][x] = 4
                        for i in range(3):
                            for z in range(3):
                                temp1 = y+(i-1);temp2 = x+(z-1);ra =random.randint(1,3)
                                if newpix[temp1][temp2]   == 1 and ra == 1: newpix[temp1][temp2] = 4
                                elif newpix[temp1][temp2] == 2 and ra == 1:
                                    newpix[temp1][temp2] = 5
                                    if random.randint(0,5) == 1 and newpix[y-1][x+mod] != 9: newpix[y][x] = 8
                                elif newpix[temp1][temp2] == 6 and ra == 1: newpix[temp1][temp2] = 4
                                elif newpix[temp1][temp2] == 7 and random.randint(1,10) == 1: newpix[temp1][temp2] = 9
                                elif newpix[temp1][temp2] == 8 and random.randint(1,75) == 1: newpix[temp1][temp2] = 9
                                elif newpix[temp1][temp2] == 3 and random.randint(1,20) == 1: newpix[temp1][temp2] = 10
                elif random.randint(0,10)   == 1: newpix[y][x] = 8
    pixels = newpix.copy()
pixel_array = pygame.PixelArray(window)
for i,y in enumerate(elm): pixel_array[w+1:round(w*1.5),i*50:(i*50)+50] = elm[y]
pixel_array.close()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mode_click = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if mode_click[0]:
                if pos[0] <= w:
                    a = math.floor(pos[1]/pw)
                    b = math.floor(pos[0]/pw)
                    for i in range(size):
                        for l in range(size):
                            try: pixels[a - (i-math.floor(size/2))][b - (l-math.floor(size/2))]  = barrow
                            except: pass
                else:
                    for i,y in enumerate(elm):
                        if pos[1] < 50*i+50 and pos[1] > 50*i: barrow = y
            elif event.button == 4 and size > 1: size -=1
            elif event.button == 5: size +=1
    pixel_array = pygame.PixelArray(window); update()
    for y in range(len(pixels)):
        for x in range(len(pixels[0])): pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = elm[pixels[y][x]]
    pixel_array.close();window.blit(myfont.render(str(round(clock.get_fps())), False, (255, 0, 0) if clock.get_fps() < 10 else (0,255,0)),(w-50,h-50)); window.blit(myfont.render(str(size), False, (255, 0, 255)),(0,h-50)); pygame.display.flip(); clock.tick(30)
pygame.quit();exit()
