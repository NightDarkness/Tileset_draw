import pygame,os,sys,io,numpy,cv2,tempfile
from pygame.locals import *
from packages.functions import *
from packages.player import *

### --- LECTURA DEL ARCHIVO DE CONFIGURACION Y ASIGNACION DE VARIABLES --- ###

WIDTH,HEIGHT,FPS,KEYBINDS = readConfigFile()
BACKGROUND = (24,20,37)
TILESIZE = 16
TEMPPATH = tempfile.TemporaryDirectory()                ### --- DIRECTORIO TEMPORAL --- ###

### --- TEMPORAL --- ###

MAPSIZE,MAPNAME,MAP,MAPSPAWN = readmap("assets\maps\\test.dat")

### --- FIN TEMP --- ###

#PLAYER = Player(loadSprites(TILESIZE, 'assets/graphics/sprites/player.png', TEMPPATH.name+"/player"), MAPSPAWN)

### --- FIN DE LA LECTUIRA Y ASIGNACION --- ###

loadSprites(TILESIZE, 'assets/graphics/sprites/tileset.png', TEMPPATH.name+"/tileset")          ### --- CARGA DEL TILESET Y CREACION DE SPRITES (tamaño del tile, localizacion del tile, localizacion de la descompresion) --- ###
#loadSprites(TILESIZE, 'assets/graphics/sprites/tileset.png', TEMPPATH.name+"/tileset")
bgSprites = backgroundSprites(TEMPPATH.name+"/tileset")                                         ### --- ASIGNACION DE SPRITES --- ###
print(TEMPPATH.name)                                    ###DEBUG###

pygame.init()                                           ### --- INICIALIZACION DE PYGAME --- ###

screen_size = (WIDTH,HEIGHT)                            ### --- RESOLUCION --- ###
screen = pygame.display.set_mode(screen_size)           ### --- CREACION DE LA VENTANA --- ###
pygame.display.set_caption("Pocket")                    ### --- NOMBRE DE LA VENTANA --- ###
clock = pygame.time.Clock()                             ### --- MANEJO DEL RELOJ DEL JUEGO (MANEJA LOS FPS) --- ###

### --- BUCLE PRINCIPAL --- ###

while True:                                             
    for event in pygame.event.get():                   ### --- BUCLE QUE MANEJA LOS EVENTOS EN LA APLICACION --- ###
        if event.type == pygame.QUIT:                   ### --- EVENTO DE CERRADO MEDIANTE CRUZ DE VENTANA --- ###
            pygame.quit()                               ### --- SE FINALIZA PYGAME --- ###
            TEMPPATH.cleanup()                          ### --- SE ELIMINAN LOS ARCHIVOS TEMPORALES --- ###
            sys.exit()
        
        if event.type == KEYDOWN:
            print("preionaste una tecla!")
            if event.unicode in KEYBINDS:
                print("y esta dentro de los keybinds! es " + event.unicode + "\n")                                ### --- SE CIERRA LA APLICACION DE RAIZ --- ###
    
    screen.fill(BACKGROUND)                             ### --- SE PINTA EL FONDO --- ###

### --- DETECCION DE TECLAS --- ###

### --- FIN DE TECLAS --- ###


### --- SELECCION DE ESTADOS --- ###

    #test = pygame.image.load(TEMPPATH.name+"\\tileset\\0.png")

    #screen.blit(test,(100,100))

    drawMap(TILESIZE, bgSprites, MAP,MAPSIZE,TEMPPATH.name)

### --- FIN DE LOS ESTADOS --- ###

### --- ACTUALIZACION DE PANTALLA --- ###

    pygame.display.update()
    clock.tick(FPS)

### --- FIN DE LA ACTUALIZACION --- ###

### --- FIN BUCLE PRINCIPAL --- ###