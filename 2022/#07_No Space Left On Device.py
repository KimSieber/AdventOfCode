###################################################
### Advent of Code 2022
###
### Autor:    Kim Sieber
### Erstellt: 29.11.2023
###
### Tag 7: No Space Left On Device
###
### Zentrale Daten-Variable:
###   Aufbau:   Verzeichnis = [ {'prevDict': <Verzeichnisbaum>, 'type':<file oder dict>, 'name':<Dateiname>, 'size':<Größe Datei oder Summe Verzeichnis>  }, ... ]
###   Beispiel: Verzeichnis = [ {'prevDict':'/:a:e',            'type':'file',           'name':'l.txt',     'size':528                                   }      ]
####################################################

### Einlesen der Daten
###
### @return Verzeichnis:  [{...},...] Verzeichnisdaten, Format siehe oben
def DateiEinlesen():
    ### Auslesen der Datei, Abschnitt Stapeldefinition, Abschnitt Anweisungsliste
    VerzEingabe = open('#07 Input', 'r').read().split('\n')
    ### Verzeichnis einlesen
    Verzeichnis = []
    Tiefe       = []      # Temp. Speicher für Verzeichnistiefe = ['/', 'a','e']
    ### Durchlaufe alle Zeilen
    for Zeile in VerzEingabe:
        ### Verzeichniswechsel in Tiefe-Variablen verändern
        if Zeile[0:4] == '$ cd':
            if Zeile[4:].strip() == '..':
                Tiefe.pop()
            elif Zeile[4:].strip() == '/':
                Tiefe.append('/')
            else:
                Verzeichnis.append({'prevDict':':'.join(Tiefe)   , 'type':'dict', 'name':Zeile[4:].strip()    , 'size':0        })
                Tiefe.append(Zeile[4:].strip())
        ### Anzeige Verzeichnisinhalt ignorieren  "$ ls"
        elif Zeile == '$ ls':
            pass ### nichts tun
        ### Verzeichnisnamen ignorieren, wenn nicht reingegangen wird "dir ..."
        elif Zeile[0:3] == 'dir':
            pass ### nichts tun
        else:
            Size, Dateiname = Zeile.split(' ')
            Verzeichnis.append({'prevDict':':'.join(Tiefe)   , 'type':'file', 'name':Dateiname    , 'size':int(Size)        })
    return Verzeichnis


### Ermittle die Dateigröße eines Verzeichnisses und speichert dieses in der globalen Variablen "Verzeichnis"
### --> Ruft sich rekursiv auf
###
### @param  VName             = (str) Verzeichnisname, nachdem gesucht werden soll
### @return Size              = (int) Speichergröße der Datei / des Verzeichnisses
def ermittleSpeichergroesse(VName):
    SumSize = 0
    ### Ermittlung aller Inhalte des angegebenen Verzeichnisses
    for i in range(len(Verzeichnis)):
        if Verzeichnis[i]['prevDict'] == VName:            
            ### Wenn Verzeichnis gefunden, dann rekursiv Ermittlung aufrufen
            if Verzeichnis[i]['type'] == 'dict':
                Size = ermittleSpeichergroesse(Verzeichnis[i]['prevDict']+':'+Verzeichnis[i]['name'])
                Verzeichnis[i].update({'size': Size})
                ### Speichergröße setzen und Summe hinzufügen
                SumSize += Size
            else:
                ### Wenn Datei gefunden, dann Speichergröße addieren
                SumSize += Verzeichnis[i]['size']
    return SumSize

### Datei einlesen und formatieren
Verzeichnis = DateiEinlesen()

### Summen je Verzeichnis ermitteln und schreiben
GesamtGroesse = ermittleSpeichergroesse('/')

print ('**********************************')
print ('Anzahl Einträge        :', len(Verzeichnis))
print ('Anzahl Verzeichnisse   :', len([v for v in Verzeichnis if v['type']=='dict']))
print ('Anzahl Dateien         :', len([v for v in Verzeichnis if v['type']=='file']))
print ('**********************************')

### PART I: Speichersumme aller Verzeichnisse mit bis zu 100000
KleineVerz = [Vers['size'] for Vers in Verzeichnis if Vers['type']=='dict' and Vers['size'] <= 100000]

############### PART I ###############################
print ('PART I : The sum of the total size of the directories with at most 100000 size is :', sum(KleineVerz) )    

WeitererBedarf = 30000000- (70000000-GesamtGroesse)
print ('**********************************')
print ('Speicherplatz gesamt   : 70000000')
print ('Speicherplatz benötigt : 30000000')
print ('Gesamtgröße            :', GesamtGroesse)
print ('Fehlender Speicherplatz:', WeitererBedarf)
print ('**********************************')

### PART II: Ermittlung aller Verzeichnisse die Größer/gleich Speicherbedarf sind
VerzSize = [Vers['size'] for Vers in Verzeichnis if Vers['type']=='dict' and Vers['size'] >= WeitererBedarf]

############### PART II ###############################
print ('PART II: The size of the smallest directory to free up enough space is            :', min(VerzSize))    


