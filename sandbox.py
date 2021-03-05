import pygame,time,random
def Reverse(tuples): return tuples[::-1]
pygame.init();window = pygame.display.set_mode((1000, 1000));clock = pygame.time.Clock()
colors = {"blue":(0,0,200),"red":(200,0,0),"green":(0,200,200),"purple":(200,0,2),"yellow":(219, 211, 187),"grey":(50,50,50),"orange":(247, 169, 73)}
h,w = 1000,1000
d = 100; pw = int(w/d)
pixels = [['' for _ in range(d)]for _ in range(d)]
for i in range(60):
    for y in range(60):
        pixels[i][y] = 'w'
for i in range(30):
    for y in range(30):
        pixels[30+i][30+y] = 's'
for i in range(30):
    for y in range(30):
        pixels[i][y] = 'sm'
for i in range(20):
    pixels[70][70] = 'f'

run = True
def update():
    global pixels
    newpix = pixels.copy()
    for y in Reverse(range(len(pixels))):
        for x in range(len(pixels[0])):
            if pixels[y][x] == 's':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 0
                    while mod == 0:
                        mod = random.randint(-1,1)
                    if pixels[y+1][x] == '' :
                        newpix[y+1][x] = 's';newpix[y][x] = ''
                    elif pixels[y+1][x+mod] == '' :
                        newpix[y+1][x+mod] = 's';newpix[y][x] = ''
                    elif pixels[y+1][x] == 'w':
                        newpix[y+1][x] = 's';newpix[y][x] = 'w'
            elif pixels[y][x] == 'w':
                if y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 0
                    while mod == 0: mod = random.randint(-1,1)
                    if pixels[y+1][x] == '' :
                        newpix[y+1][x] = 'w';newpix[y][x] = ''
                    elif pixels[y+1][x+mod] == '' :
                        newpix[y+1][x+mod] = 'w';newpix[y][x] = ''
                    elif pixels[y][x+mod] == '' :
                        newpix[y][x+mod] = 'w';newpix[y][x] = ''
                    elif pixels[y][x+(mod*-1)] == '' :
                        newpix[y][x+(mod*-1)] = 'w';newpix[y][x] = ''
            elif pixels[y][x] == 'sm':
                if 2<y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 0
                    while mod == 0: mod = random.randint(-1,1)
                    if pixels[y-1][x] == '' :
                        newpix[y-1][x] = 'sm';newpix[y][x] = ''
                    elif pixels[y-1][x+mod] == '' :
                        newpix[y-1][x+mod] = 'sm';newpix[y][x] = ''
                    elif pixels[y][x+mod] == '' :
                        newpix[y][x+mod] = 'sm';newpix[y][x] = ''
                    elif pixels[y][x+(mod*-1)] == '' :
                        newpix[y][x+(mod*-1)] = 'sm';newpix[y][x] = ''
            elif pixels[y][x] == 'f':
                if 1<y+1 < len(pixels):
                    if x >= len(pixels)-1: x = -1
                    mod = 0
                    while mod == 0: mod = random.randint(-1,1)
                    if pixels[y-1][x] == '' :
                        newpix[y-1][x] = 'f';newpix[y][x] = ''
                    elif pixels[y-1][x+mod] == '' :
                        newpix[y-1][x+mod] = 'f';newpix[y][x] = ''
                    else: newpix[y][x] = ''
                    for i in range(3):
                        for z in range(3):
                            if pixels[y+(i-1)][x+(z-1)] == 'sm':
                                pixels[y+(i-1)][x+(z-1)] = 'f'


    pixels = newpix.copy()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)


    pixel_array = pygame.PixelArray(window)
    update()
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            if pixels[y][x] == 's': pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = colors["yellow"]
            if pixels[y][x] == 'w': pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = colors["blue"]
            if pixels[y][x] == 'sm': pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = colors["grey"]
            if pixels[y][x] == 'f': pixel_array[x*pw:(x*pw)+pw, y*pw:(y*pw)+pw] = colors["orange"]

    pixel_array.close()

    pygame.display.flip()

    clock.tick(120)
pygame.quit()
exit()
