################################################
##### AdventOfCode 2020
#####
##### Day 20 - 
#####
##### @author  Kim Sieber
##### @date    20.12.2020 
###################################################
### Parameter
FILENAME = "input.txt"

### Liest Datei ein
### @file_name:    (str) Dateiname
### @return   : tiles[tile_id]['img'][y][x]  = (str) pic     : Zeichen im Bild, '#'/'.', an Koordinate y/x
###                           ['pos'][0,1]   = (int, int) Position relativ zur Start-Pos [0,0]=[y,x]
###                                                  Initial=0, wenn noch keine Position
###                                                  bei 9 Tiles werden diese von links nach rechts
###                                                  und oben nach unten gezaehlt
###                                                  Bsp:   1 2 3 
###                                                         4 5 6 
###                                                         7 8 9 
def readInput(file_name):
    tiles = {}
    input_file  = open(file_name, "r")
    input_tiles = input_file.read().split("\n\n")
    for input_tile in input_tiles:
        temp_tile, pic     = input_tile.split(":")
        temp     , tile_id = temp_tile.split(" ")
        pic_lines          = pic.strip().split("\n")
        pics = []
        for pic_line in pic_lines:
            pics.append(list(pic_line.strip()))
        tiles[int(tile_id)] = {'img': pics, 'pos': 0 }
    return tiles

### Druckt ein Tile aus
### @img      : Tile-Liste mit allen Daten, Format s.o.
### @tile_id  : ID des gewuenschten Tiles, leer lassen wenn Druck aller Tiles gewuenscht
def printTiles(tiles, tile_id=None):
    for tileKey in (tileKey for tileKey in tiles if tile_id==None or tileKey==tile_id) :
        print("Tile " + str(tileKey) + ":   (pos:"+str(tiles[tileKey]['pos']))
        printImage(tiles[tileKey]['img'])
def printImage(img):
    for line in img:
        print("".join(line))
    print()

### Tile um 90 Grad nach rechts drehen
### @img       : [x][y] = "#"/"."    Bild-Daten eines Tiles
### @direction : (int) 1 fuer Uhrzeigerrichtung, -1 fuer gegen den Uhrzeiger
### @return    : [x][y] = "#"/"."    um 90-Grad gedreht Bilddaten des vorgegebenen Tiles
def rotate(img, direction=1):
    if direction ==  1 : return list(zip(*img[::-1]))
    if direction == -1 : return list(zip(*reversed(list(zip(*reversed(list(zip(*reversed(img)))))))))
    return False

### Tile oben/unten spiegeln
### @img    : [x][y] = "#"/"."    Bild-Daten eines Tiles
### @return : [x][y] = "#"/"."    horizontal gespiegelte Bilddaten des vorgegebenen Tiles
def flipHorizontal(img):
    img.reverse()
    return img

### Tile rechts/links spiegeln
### @img    : [x][y] = "#"/"."    Bild-Daten eines Tiles
### @return : [x][y] = "#"/"."    vertikal gespiegelte Bilddaten des vorgegebenen Tiles
def flipVertical(img):
    img_out = []
    for line in img:
        line = list(line)
        line.reverse()
        img_out.append(line)
    return img_out

### gibt eine Seite als Zeile zurueck, im Uhrzeigersinn gelesen
### dienst des normierten Vergleichs zwischen zwei Tiles
### @img    : [x][y] = "#"/"."    Bild-Daten eines Tiles
### @side   : 0..3  Seite angeben, dabei 0=Nord, 1=Ost, 2=Sued, 3=West
### @return : edge: (str) Zeile der gewuensten Kante, bspw. "..##.#..#."
def getEdge(img, side):
    for i in range(side):
        img = rotate(img, -1)
    return "".join(img[0])

### Sucht für eine vorgegebene Seite das passende Gegenstueck
### und gibt die ID des passenden Tile zurueck, sowie Seite und Anzahl Spiegelungen (horizont/vertikal)
### @tiles              : {} Liste aller Tiles -> Format s.o.
### @searched_side      : 0..3  Seite angeben, dabei 0=Nord, 1=Ost, 2=Sued, 3=West
### @searched_edge      : (str) gesuchte Kombination, bspw. ".##...##.#"
### @return     : tile_id, imgage  (in richtiger Drehung)       -> wenn nichts gefunden, beides=False
def findFittingTile(tiles, searched_side, searched_edge):
    #print("searched_side:",searched_side," _edge:",searched_edge)
    ### Drehen, da spiegelverkehrt zu suchen
    searched_edge = "".join(list(reversed(searched_edge)))
    searched_side = [2,3,0,1][searched_side]
    #print("searched_side:",searched_side," _edge:",searched_edge)

    def getKeyForValue(dictionary, value):
        for key in dictionary:
            if dictionary[key] == value:
                return key

    for tile_id in (tile for tile in tiles if tiles[tile]['pos']==0):
        img = tiles[tile_id]['img']
        for i in range(2):          #-> vertical flip
            for j in range(2):      #-> horizontal flip
                for k in range(4):  #-> rotation
                    if getEdge(img, searched_side) == searched_edge:
                        return tile_id, img
                    img = rotate(img, 1)
                img = flipHorizontal(img)
            img = flipVertical(img)
    return False, False

### Ermittelt die relativen Positionen der Tiles zu einander
### Es wird das erste, zufaellige Tile genommen und danebenliegende gesucht
### Die Funktion befuellt den Wert in ['pos'] mit der Position [rY,rX],
### wobei rX und rY hier die relativen Bezuege sind
### @tiles              : {} Liste aller Tiles -> Format s.o.
### @tiles              : {} Liste aller Tiles mit befuellten Werten bei ['pos'] -> Format s.o.
def detectRelativePosition(tiles):
    tile_id_start   = list(tiles.keys())[0]             #-> erste tile_id (beliebig) als Start-Position setzen

    ### Start-Parameter setzen
    tile_id               = tile_id_start               #-> Start-Tile merken fuer Wiederholung
    direction             = 1                           #-> Werte: 0=nord, 1=ost, 2=sued, 3=weste
    pos                   = [0,0]                       
    tiles[tile_id]['pos'] = pos[:]                      #-> Relative Position des Start-Tiles immer [0,0]
    direction_loops       = 0                           #-> Zahler zur Pruefung, ob keine Richtung mehr mgl
    while True: 
        tile_id_out, img = findFittingTile(tiles, direction, getEdge(tiles[tile_id]['img'],direction))
        if tile_id_out:
            direction_loops       = 0
            tile_id               = tile_id_out
            tiles[tile_id]['img'] = img
            pos[0] = pos[0] + int([-1, 0, 1, 0][direction])
            pos[1] = pos[1] + int([ 0, 1, 0,-1][direction])
            tiles[tile_id]['pos'] = pos[:]
        else:
            direction          += 1                      #-> wenn nicht weiter, dann Richtung drehen
            if direction           == 4: 
                direction      -= 4
            direction_loops    += 1                      #-> wenn nicht weiter, dann erneut Start-Position
            if direction_loops     == 4:
                if tile_id     == tile_id_start:         #-> Wenn ab Start nicht mehr weiter, dann ende
                    break
                direction_loops = 0
                tile_id         = tile_id_start
                pos             = [0,0]
    return tiles

### Tiles-Array nach Position sortieren und mit [0][0] beginnen
### @tiles      : {} Liste aller Tiles -> Format s.o.
### @return     : Map[rY][rX]['img'][y][x]   = (str) '#' / '.'
###                   +---+------------------- Position des gesamten Tiles auf der Map, Zeile x Spalte
###                                  +--+----- Position des Pics (Zeichens) innerhalb des Img
###                          ['tid']         = (int) Tile-ID
def getMap(tiles):
    Map = {}
    corr_y = corr_x = 0
    ### Minimalste POS ermitteln
    for tile_id in tiles:
        if tiles[tile_id]['pos'][0] < corr_y: corr_y = tiles[tile_id]['pos'][0]
        if tiles[tile_id]['pos'][1] < corr_x: corr_x = tiles[tile_id]['pos'][1]
    for tile_id in tiles:
        Map[tiles[tile_id]['pos'][0]-corr_y] = {}
    for tile_id in tiles:
        Map[tiles[tile_id]['pos'][0]-corr_y][tiles[tile_id]['pos'][1]-corr_x] = {}
    for tile_id in tiles:
        Map[tiles[tile_id]['pos'][0]-corr_y][tiles[tile_id]['pos'][1]-corr_x]['img'] = tiles[tile_id]['img']
        Map[tiles[tile_id]['pos'][0]-corr_y][tiles[tile_id]['pos'][1]-corr_x]['tid'] = tile_id

    import collections
    Map = collections.OrderedDict(sorted(Map.items()))
    for Map_y in Map:
        Map[Map_y] = collections.OrderedDict(sorted(Map[Map_y].items()))
    return Map

### Ermittelt die 4 Ecken und gibt eine Liste der Tile-IDs der Eck-Tiles zurueck
### @Map    : Map[rY][rX]['img'][y][x]   = (str) '#' / '.'
###                      ['tid']         = (int) Tile-ID
### @return : corners[0..n] = (int) tile_id
def getCorners(Map):
    corners = []
    max_y = max(Map.keys())
    max_x = max(Map[0].keys())
    corners.append(Map[  0  ][  0  ]['tid'])
    corners.append(Map[  0  ][max_x]['tid'])
    corners.append(Map[max_y][  0  ]['tid'])
    corners.append(Map[max_y][max_x]['tid'])
    return corners

### Bildet ein gesamtes Bild, schneidet aber die Kanten ab (x=0,y=0,max(x.key),max(y.key))
### @Map    : Map[rY][rX]['img'][y][x]   = (str) '#' / '.'
### @return : image[y]                   = (str) '#' / '.'
def buildTotalImage(Map):
    image = []
    lines = []
    for Map_y in Map:
        lines = [""] * (len(Map[0][0]['img'])-2)
        for Map_x in Map[Map_y]:
            i = 0
            for y in range(1, len(Map[Map_y][Map_x]['img'])-1):
                lines[y-1] += str("".join(Map[Map_y][Map_x]['img'][y]))[1:len(Map[Map_y][Map_x]['img'][y])-1]
                i += 1
        for line in lines:
            image.append(line)
        lines = []
    return image

### prueft SeeMonster und gibt Image mit entfernen SeeMonstern zurueck
### Das zu suchende SeeMonster:        0123456789+123456789
###                                                      # 
###                                    #    ##    ##    ###
###                                     #  #  #  #  #  #   
###              Gesamt-Feld 1:        0123456789+123456789+123456
###              Gesamt-Feld 2:    0123456789+123456789+123
### @image   : image[y]               = (str) '#' / '.'
### @return  : cntMonsters            = (int) Anzahl gefundene SeeMonster
###            imgWithoutMonsters[y]  = (str) '#' / '.'
def getImageWithoutSeeMonsters(image):
    cntMonsters        = 0
    imgWithoutMonsters = image[:]
    OFFSET             = len(image[0])-19
    monsterModel       = [[18],[0,5,6,11,12,17,18,19],[1,4,7,10,13,16]]

    ### Gibt definierte Zeichen einer Kette zurueck inkl Versatz
    ### @lines[0-2]       : (str)  '#' / '.'
    ### @model[0-2][0..n] : (int) Position, an der ein '#' sein soll
    ### @offset           : (int) Versatz
    ### @return           : (bool/int) False, wenn kein Mosnter gefunden, sonst Zahl fuer offset 
    def checkMonster(lines, model, offset):
        for corr_y in range(0,offset):
            flag = True
            for line, mod in enumerate(model):
                for m in mod:
                    if lines[line][m+corr_y] != "#":
                        flag = False
            if flag == True:
                return corr_y
        return False

    ### Loescht das Monster und gibt Zeile mit geloeschtem Monster zurueck
    ### @line:                  (str)  '#' / '.'
    ### @model[0..n]:           (int) Position, an der ein '#' sein soll
    ### @offset:                (int) Versatz
    ### @return:                (str)  '#' / '.'
    def removeMonster(line, model, offset):
        line = "".join(line)
        for mod in model:
            line = line[:(mod+offset)] + '.' + line[(mod+offset)+1:]
        return "".join(line)


    for y in range(0,len(image)-2):
        ret_offset = True
        while ret_offset:                                           #-> Wichtig, da in einer Zeile mehrere sein 
            check_line = [image[y], image[y+1], image[y+2]]         #   koennen
            ret_offset = checkMonster(check_line, monsterModel, OFFSET)
            if ret_offset:
                image[y]   = removeMonster(image[y]  ,monsterModel[0],ret_offset) 
                image[y+1] = removeMonster(image[y+1],monsterModel[1],ret_offset)
                image[y+2] = removeMonster(image[y+2],monsterModel[2],ret_offset)
                cntMonsters += 1

    for key, line in enumerate(image):
        image[key] = "".join(line)

    return cntMonsters, image

### Sucht die Monster durch drehen und flippen des Bildes
### gibt Anzahl Monster und Bild zurueck
### @image   : image[y]               = (str) '#' / '.'
### @return  : cntMonsters            = (int) Anzahl gefundene SeeMonster
###            image[y]               = (str) '#' / '.', nur ohne Monster
def killMonster(image):
    for h in range(0,2):
        for v in range(0,2):
            for r in range(0,4):
                cnt_monsters, image_without_monsters = getImageWithoutSeeMonsters(image)
                if cnt_monsters > 0:
                    return cnt_monsters, image_without_monsters
                image = rotate(image)
            image = flipVertical(image)
        image = flipHorizontal(image)
    return False

### Zaehlt alle '#'-Zeichen in einem Bild
### @image[y] = (str) '#' / '.'
### @return   = (int) Anzahl
def cntHash(image):
    cnt = 0
    for i in image:
        cnt += i.count("#")
    return cnt





tiles   = readInput(FILENAME)

tiles   = detectRelativePosition(tiles)

Map     = getMap(tiles)

corners = getCorners(Map)

product = 1
for corner in corners:
    product *= corner
print()
print("PART I  : The product of the tile-IDs in the corners is : ", product)
print()


image = buildTotalImage(Map)

cnt_monsters, image_without_monsters = killMonster(image)
print()
print("PART II : Number of # are note part of a sea monster is : ", cntHash(image_without_monsters))
print()


