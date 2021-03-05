import pygame,time,random,math
#Hi
h = 1000; w=h; d = 100; pw = int(w/d);run = True;barrow = '';size = 7
pygame.init();window = pygame.display.set_mode((round(w*1.5),w ));clock = pygame.time.Clock()
colors = {"blue":(0,0,200),"red":(200,0,0),"green":(0,200,200),"purple":(200,0,2),"yellow":(219, 211, 187),"grey":(50,50,50),"orange":(247, 169, 73),"white":(217, 217, 217),"grey2":(25,25,25),"oil":(54, 63, 70)}
pixels = [['' for _ in range(d)]for _ in range(d)]; elm = {"g":"grey","w":"blue","s":"yellow","f":"orange","t":"white","p":"grey2","o":"oil"}
def Reverse(tuples): return tuples[::-1]
def update():
    global pixels
    newpix = [i for i in (pixels)]
    for y in Reverse(range(len(pixels))):
        for x in range(len(pixels[0])):
            if pixels[y][x] == 's':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == '' : newpix[y+1][x]        = 's';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y+1][x+mod]    == '' : newpix[y+1][x+mod]    = 's';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y+1][x]        == 'w': newpix[y+1][x]        = 's';newpix[y][x] = 'w';pixels[y][x] = 'w'
            elif pixels[y][x] == 'w':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == '' : newpix[y+1][x]        = 'w';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y+1][x+mod]    == '' : newpix[y+1][x+mod]    = 'w';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y][x+mod]      == '' : newpix[y][x+mod]      = 'w';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y][x+(mod*-1)] == '' : newpix[y][x+(mod*-1)] = 'w';newpix[y][x]  = '';pixels[y][x] = ''
            elif pixels[y][x] == 'g':
                if 1<y+1 < len(pixels)+1:
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     ==   1: mod*=-1
                    if random.randint(0,1) == 1: pass
                    elif newpix[y-1][x]          == 'w' : newpix[y-1][x]        = 'g';newpix[y][x] = 'w';pixels[y][x] = 'w'
                    elif newpix[y-1][x]          == '' : newpix[y-1][x]        = 'g';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y-1][x+mod]    == '' : newpix[y-1][x+mod]    = 'g';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y][x+mod]      == '' : newpix[y][x+mod]      = 'g';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y][x+(mod*-1)] == '' : newpix[y][x+(mod*-1)] = 'g';newpix[y][x] = '';pixels[y][x] = ''
                else:
                    for z in range(3):
                        if x + (z-1) <= 99 and pixels[y][x+(z-2)] == 'f': pixels[y][x] = 'f'
            elif pixels[y][x] == 'f':
                if 2<=y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1) == 1: mod*=-1
                    if random.randint(0,1) == 1: pass
                    elif newpix[y-1][x+mod]    == '' : newpix[y-1][x+mod]    = 'f';newpix[y][x]  = '';pixels[y][x] = ''
                    else: newpix[y][x] = ''
                    for i in range(3):
                        for z in range(3):
                            if pixels[y+(i-1)][x+(z-1)] == 'g' and random.randint(1,3) == 1: pixels[y+(i-1)][x+(z-1)] = 'f'
                            elif pixels[y+(i-1)][x+(z-1)] == 'w' and random.randint(1,3) == 1: pixels[y+(i-1)][x+(z-1)] = 't'
                            elif pixels[y+(i-1)][x+(z-1)] == 'p' and random.randint(1,3) == 1: pixels[y+(i-1)][x+(z-1)] = 'f'
                            elif pixels[y+(i-1)][x+(z-1)] == 'o' and random.randint(1,3) == 1: pixels[y+(i-1)][x+(z-1)] = 'f'
                    if random.randint(0,10) == 1: newpix[y][x] = ''
                elif random.randint(0,3) == 1: newpix[y][x] = ''
            elif pixels[y][x] == 't':
                if 2<=y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     ==   1: mod*=-1
                    if random.randint(0,120) == 1:  pixels[y][x] = 'w';continue
                    if random.randint(0,1) == 1:pass
                    elif newpix[y-1][x]          == 'w' : newpix[y-1][x]        = 't';newpix[y][x] = 'w';pixels[y][x] = 'w'
                    elif newpix[y-1][x+mod]    == '' : newpix[y-1][x+mod]    = 't';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y][x+mod]      == '' : newpix[y][x+mod]      = 't';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y][x+(mod*-1)] == '' : newpix[y][x+(mod*-1)] = 't';newpix[y][x] = '';pixels[y][x] = ''
                elif random.randint(0,120) == 1:  pixels[y][x] = 'w';continue
            elif pixels[y][x] == 'p':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y+1][x]          == '' : newpix[y+1][x]        = 'p';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y+1][x+mod]    == '' : newpix[y+1][x+mod]    = 'p';newpix[y][x] = '';pixels[y][x] = ''
                    elif newpix[y+1][x]        == 'w': newpix[y+1][x]        = 'p';newpix[y][x] = 'w';pixels[y][x] = 'w'
            elif pixels[y][x] == 'o':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 1
                    if random.randint(0,1)     == 1: mod*=-1
                    if newpix[y-1][x]         == 'w' : newpix[y-1][x]        = 'o';newpix[y][x] = 'w';pixels[y][x] = 'w'
                    elif newpix[y+1][x]        == '' : newpix[y+1][x]        = 'o';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y+1][x+mod]    == '' : newpix[y+1][x+mod]    = 'o';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y][x+mod]      == '' : newpix[y][x+mod]      = 'o';newpix[y][x]  = '';pixels[y][x] = ''
                    elif newpix[y][x+(mod*-1)] == '' : newpix[y][x+(mod*-1)] = 'o';newpix[y][x]  = '';pixels[y][x] = ''
    pixels = newpix.copy()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] <= w:
                a = math.floor(pos[1]/10)
                b = math.floor(pos[0]/10)
                for i in range(size):
                    for l in range(size):
                        try:
                            pixels[a - (i-math.floor(size/2))][b - (l-math.floor(size/2))]  = barrow
                        except: pass

            else:
                for i,y in enumerate(elm):
                    if pos[1] < 50*i+50 and pos[1] > 50*i: barrow = y
    window.fill(0); pixel_array = pygame.PixelArray(window); update()
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            for i in elm:
                if pixels[y][x] == i: pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = colors[elm[i]]
    for i,y in enumerate(elm): pixel_array[w+1:round(w*1.5),i*50:(i*50)+50] = colors[elm[y]]
    pixel_array.close(); pygame.display.flip(); clock.tick(30)
pygame.quit();exit()
