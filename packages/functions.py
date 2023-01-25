import pygame,os,sys,io,numpy,cv2,tempfile

def readConfigFile():

    try:

        File = open("config/settings.ini","r")

        config_file = File.readlines()

        WIDTH = config_file[0].strip("WIDTH=\n")
        HEIGHT = config_file[1].strip("HEIGHT=\n")
        FPS = config_file[2].strip("FPS=\n")
        KEYBINDS = {config_file[6].strip("UP=\n"):"UP", config_file[7].strip("DOWN=\n"):"DOWN", config_file[8].strip("LEFT=\n"):"LEFT", config_file[9].strip("RIGHT=\n"):"RIGHT"}

        File.close()

        return int(WIDTH),int(HEIGHT),int(FPS),KEYBINDS

    except:

        print("error en la lectura del archivo")
    

def loadSprites(TILESIZE, TILEPATH, TEMPPATH):

    initial_count = 0

    print(os.path.exists(TEMPPATH))

    try:
        if(os.path.exists(TEMPPATH) == True):
            
            for path in os.listdir(TEMPPATH):
                if os.path.isfile(os.path.join(TEMPPATH, path)):
                    initial_count += 1

            print(initial_count)

        else:

            os.mkdir(TEMPPATH)

    except:
        print("NO SE PUDO CREAR LA CARPETA")

    image = cv2.imread(TILEPATH)
    dim = numpy.shape(image)

    for x in range(dim[0] - 1):
        for y in range(dim[1] - 1):
            if x % TILESIZE == 0 and y % TILESIZE == 0:
                cv2.imwrite(TEMPPATH+"/"+str(initial_count)+".png",image[x:x+TILESIZE,y:y+TILESIZE])
                initial_count += 1

def backgroundSprites(TEMPPATH):

    spr_default = pygame.image.load(TEMPPATH+"\\0.png")             #0
    spr_grass_0 = pygame.image.load(TEMPPATH+"\\1.png")             #1
    spr_grass_1 = pygame.image.load(TEMPPATH+"\\2.png")             #2
    spr_grass_2 = pygame.image.load(TEMPPATH+"\\3.png")             #3
    spr_grass_3 = pygame.image.load(TEMPPATH+"\\4.png")             #4
    spr_grass_4 = pygame.image.load(TEMPPATH+"\\5.png")             #5
    spr_grass_5 = pygame.image.load(TEMPPATH+"\\6.png")             #6
    spr_grass_6 = pygame.image.load(TEMPPATH+"\\7.png")             #7
    spr_grass_7 = pygame.image.load(TEMPPATH+"\\8.png")             #8
    spr_grass_8 = pygame.image.load(TEMPPATH+"\\9.png")             #9
    spr_block = pygame.image.load(TEMPPATH+"\\13.png")              #10
    spr_square = pygame.image.load(TEMPPATH+"\\15.png")             #11
    spr_square_block = pygame.image.load(TEMPPATH+"\\16.png")       #12
    spr_corner = pygame.image.load(TEMPPATH+"\\17.png")             #13
    spr_line = pygame.image.load(TEMPPATH+"\\18.png")               #14
    spr_u = pygame.image.load(TEMPPATH+"\\19.png")                  #15
    spr_paralelo = pygame.image.load(TEMPPATH+"\\20.png")           #16
    spr_line2 = pygame.image.load(TEMPPATH+"\\21.png")              #17
    spr_corner2 = pygame.image.load(TEMPPATH+"\\22.png")            #18
    spr_door = pygame.image.load(TEMPPATH+"\\23.png")               #19
    spr_exit = pygame.image.load(TEMPPATH+"\\24.png")               #20
    spr_stairs = pygame.image.load(TEMPPATH+"\\25.png")             #21
    spr_ladder = pygame.image.load(TEMPPATH+"\\26.png")             #22

    sprites = [spr_default, spr_grass_0, spr_grass_1, spr_grass_2, spr_grass_3, spr_grass_4, spr_grass_5, spr_grass_6, spr_grass_7, spr_grass_8, spr_block, spr_square, spr_square_block, spr_corner, spr_line, spr_u, spr_paralelo, spr_line2, spr_corner2, spr_door, spr_exit, spr_stairs, spr_ladder]
    
    return sprites

def readmap(mapDir):

    try:
    
        MAPFILE = open(mapDir)
        mapRAWInfo = MAPFILE.readlines()

        mapSize = int(mapRAWInfo[0].strip("size=\n"))
        mapName = mapRAWInfo[1].strip("name=\n")
        mapSpawn = mapRAWInfo[2].strip("playerSpawn=\n").split("x")
        mapForm = mapRAWInfo[9:mapSize+9]

        map = ""

        for i in range(mapSize):
            temp = mapForm[i].strip("\n")
            map += temp

        map = map.split("'")
        
        return mapSize,mapName,map,mapSpawn

    except:

        print("error al leer el mapa")

def drawMap(tileSize, sprites, map, size, path):

    display = pygame.display.get_surface()
    
    for i in range(size):
        for j in range(size):

            if map[(size*i)+j][0] != "e":

                if map[(size*i)+j][0] == "x":

                    display.blit(sprites[10],(j*tileSize,i*tileSize))

                if map[(size*i)+j][0] == "d":
                    
                    display.blit(pygame.transform.rotate(sprites[19],90*int(map[(size*i)+j][1])),(j*tileSize,i*tileSize))   ### --- VARIANTE PARA ROTAR SPRITES --- ### 
                
                if map[(size*i)+j][0] == "g":

                    display.blit(sprites[(1 + int(map[(size*i)+j][2]))],(j*tileSize,i*tileSize))                            ### --- VARIANTE DE SPRITE, MULTIPLES TIPOS --- ###
                
