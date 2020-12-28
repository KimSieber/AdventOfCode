###############################################
##### AdventOfCode 2020
#####
##### Day 24 - Lobby Layout
#####
##### @author  Kim Sieber
##### @date    27.12.2020 
###################################################
### Parameter
FILENAME = "input.txt"

### Speicher fuer Fliesen
###  grid[(y,x)]            = (int) 0/1  0=weiss (inital), 1=schwarz
###        +-+--------------- Koordinaten y und x der Fliese in einem Tuple
###
### Verstaendnis der Koordinaten:
### =============================
### Hinweis: Da Kachsel sechseckig (hex grid) sind, ist nicht an jeder Koordinate eine Fliese
###          -> e,w         = nach Osten oder Westen gibt der X-Koordinaten immer 2 Zaehler
###          -> se,sw,nw,nw = schraeg navigiert, ergibt eine Veraenderung der X- und Y-Koordinate
###                           um jeweils +/- 1
grid = {}

### Liest Datei ein und gibt eine Liste von Instruktionen zurueck
### @filen_name                = (str) Dateiname
### @return tile_list[0..n][0..n]   = (str) Instruktion (e, se, sw, w, nw, ne)
###                   +-------------- Zaehler fuer Anweisungszeilen (je Zeile eine Fliese)
###                         +-------- Zaehler fuer Anweisungen dieser einen Fliese
def readInput(file_name):
    tile_list   = []
    input_file  = open(file_name, "r")
    lines       = input_file.read().split("\n")
    rem         = ""
    for line in lines:
        orders      = []
        letters = list(line)
        for letter in letters:
            if letter in ("s", "n"):
                rem = letter
            else:
                if rem != "":
                    append = rem + letter
                    rem = ""
                else:
                    append = letter
                orders.append(append)
        tile_list.append(orders)
    input_file.close()
    return tile_list

### Eine Fliese aendern
### @insts[0..n]           = (str) Liste von Anweisungen (se, nw, e, w, ...)
### @grid[(y,x)]           = (int) Fliesenzustand an Koordinate Y,X
### @return grid[(y,x)]    = (int) 0/1  => Veraendertes Grid zurueck
def flipTile(insts, grid):
    x = y = 0
    for inst in insts:
        if inst == "e":
            x += 2
        elif inst == "w":
            x -= 2
        elif inst == "se":
            x += 1
            y += 1
        elif inst == "sw":
            x -= 1
            y += 1
        elif inst == "ne":
            x += 1
            y -= 1
        elif inst == "nw":
            x -= 1
            y -= 1
    if (y,x) not in grid.keys():
        grid[(y,x)] = 1
    else:
        if grid[(y,x)] == 0:
            grid[(y,x)] = 1
        else:
            grid[(y,x)] = 0
    return grid

### Ermittelt die Anzahl der schwarzen Fliesen auf dem Grid
### @grid[(y,x)]    : (int) Fliesenzustand an Koordinate Y,X
### @return         : (int) Anzahl schwarze Fliesen
def cntBlackTiles(grid):
    cnt = 0
    for key in grid:
        if grid[key] == 1:     cnt += 1
    return cnt


tile_list = readInput(FILENAME)

for tile_insts in tile_list:
    grid = flipTile(tile_insts, grid)


print()
print("PART I  : Number of tiles with the black side up : ", cntBlackTiles(grid))
print()


### Ermittelt die Koordinaten der angrenzenden Fliesen
### @pos            : (tuple) (y, x) - Koordinaten der Ausgangsfliese
### @return[0..5]   : (tuple) (y, x) - Koordinaten der 6 umliegenden Fliesen
def getTilesAdj(pos):
    ret = []
    y = pos[0]
    x = pos[1]
    ret.append((y  ,x+2))       #=> e
    ret.append((y  ,x-2))       #=> w
    ret.append((y+1,x+1))       #=> se
    ret.append((y+1,x-1))       #=> sw
    ret.append((y-1,x+1))       #=> ne
    ret.append((y-1,x-1))       #=> nw
    return ret

### Ermittelt die Anzahl der angrenzenden Fliesen, die schwarz sind
### @grid[(y,x)]    : (int) Fliesenzustand an Koordinate Y,X
### @pos            : (tuple) (y, x) - Koordinaten der Ausgangsfliese
### @return         : (int) Anzahl der schwarzen Fliesen drum herum
def getNumBlackTilesAdj(grid, pos):
    cnt_black = 0
    tiles_adj = getTilesAdj(pos)
    for tile in tiles_adj:
        if tile in grid.keys():
            if grid[tile] == 1:     
                cnt_black += 1
    return cnt_black

### Prueft Fliese und gibt (neue) Farbe zurueck
### @grid[(y,x)]    : (int) Fliesenzustand an Koordinate Y,X
### @pos            : (tuple) (y, x) - Koordinaten der Ausgangsfliese
def checkTileNewColor(grid, pos):
    cntBlackTiles = getNumBlackTilesAdj(grid,pos)
    if pos in grid.keys():          color = grid[pos]
    else:                           color = 0
    ret = color
    if color == 1 and (cntBlackTiles == 0 or cntBlackTiles > 2):
        ret = 0
    elif color == 0 and cntBlackTiles == 2:
        ret = 1
    return ret


### Durchlaeft alle Fliesen und bei Schwarz alle Nachbarfliesen und
### fruehrt Aenderungspruefung aus.
### Aenderungsbedarf wird gespeichert und anschliessend gesamthaft ausgefuert
### @grid[(y,x)]            = (int) Fliesenzustand an Koordinate Y,X
### @return     grid[(y,x)] = (int) Fliesenfarbe - aktualisiertes grid
def runOneDay(grid):
    chg_log = {}

    def getTileColor(pos):
        if pos in grid.keys():  return grid[pos]
        else:                   return 0

    ### Alle gespeicherten Tiles pruefen
    for tile in grid.keys():
        color     = grid[tile]
        new_color = checkTileNewColor(grid,tile)
        if color != new_color:
            chg_log[tile] = new_color
        ### von jeder umliegenden Fliese Zustand pruefen, wenn nicht in grid
        tiles_adj = getTilesAdj(tile)
        for tile_adj in tiles_adj:
            if tile_adj not in grid.keys():
                color_adj     = getTileColor(tile_adj)
                new_color_adj = checkTileNewColor(grid,tile_adj)
                if color_adj != new_color_adj:
                    chg_log[tile_adj] = new_color_adj

    ### Alle Aenderungen ausfuehren => weisse Fliesen loeschen
    for key in chg_log:
        if chg_log[key] == 1:
            grid[key] = 1
        else:
            if key in grid.keys():
                grid[key] = 0

    return grid


for i in range(100):
    grid = runOneDay(grid)

print()
print("PART II : Number of black tiles after 100 days   : ", cntBlackTiles(grid))
print()

