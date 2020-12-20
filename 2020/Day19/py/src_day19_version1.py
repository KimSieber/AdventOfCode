#################################################
##### AdventOfCode 2020
#####
##### Day 19 - Monster Messages
#####
##### @author  Kim Sieber
##### @date    19.12.2020
###################################################
### Parameter
#FILENAME = "input_test3.txt"
FILENAME = "input.txt"

### Regelwerke
### rules[RuleNo][('n n n')][0..n]      = (str) possib / possibs: Ein gueltiges Ergebnis dieser Regel-Kombination 
###       +------------------------------ (int) ruleNo          : Regel-Nummer gemaess Input
###                 +-------------------- (str) comb   / combs  : gueltige Regel-Kombination (idR. 2 Zahlen)
###                          +----------- (int) possibKey(s)    : Zaehler fuer die Regelkombinationen, 
###                                                               die sich daraus ergeben
### FALL-BEISPIELE:
### rules[   4  ][ ( 0 ) ][  0 ]        = a         -> Beispiel-Aufbau fuer Buchstaben-Werte
### rules[   0  ][(4 1 5)]              = ""        -> Beispiel-Aufbau, wenn noch keine Kombinations abgeleitet
### NOMENKLATUR:
### 1: 2 3 | 3 2                = Regelwerk aus Input-Datei (rule)    / (rules)
### +---------------------------- Regel-Nr                  (ruleNo)
###    +++---+++----------------- Regel-Kombinationen       (comb)    / (combs)
###    +------------------------- Quell-Regel               (srcRule) / (srcRules)
### -> abgeleitete Werte, bspw. die Kombinationen der Quell-Regeln haben ein vorangestelltes "src", bsw. "srcCombs"
rules = {}

### Nachrichten
### msg[0..n]       = Nachricht im Format: "abaabbabab..."
msg = []

### Liest Datei ein
### @fln    :   (str) Dateiname
### @return :   rules{}, msg[]    2 Rueckgaben, Formate s.o.
def readInputFile(fln):
    rulesInput = {}
    msgInput   = []
    part       = 0          # -> 0=rules, 1=messages
    inputFile = open(fln, "r")
    for line in inputFile:
        if line.strip() == "":
            part += 1
        else:
            if part == 0:
                ruleNo, rule = line.strip().split(":")
                ruleNo = int(ruleNo)
                rulesInput[ruleNo] = {}
                rules = rule.split("|")
                if rules[0].strip() in ('"a"', '"b"'):
                    rulesInput[ruleNo][('0')] = []
                    rulesInput[ruleNo][('0')].append(rules[0].strip()[1:2])
                else:
                    for r in rules:
                        rulesInput[ruleNo][(r.strip())] = ""

            elif part == 1:
                msgInput.append(line.strip())

    inputFile.close()
    return rulesInput, msgInput

### Regelwerke ausfuehren und Kombinationen ergaenzen
### Diese Funktion durchlaeuft nur 1x die Regelwerke und befuellt die, deren Quellen auch schon befuellt sind
### Zurueck gibt die Funktion die Anzahl der gesetzten Kombinationen.
### Diese Funktion muss solange ausgefuert werden, bis Rueckgabe = 0 ist, d.h. alle mgl. Kombinationen 
### gesetzt wurden
### @rules      : rules{}, Format s.o.
### @specRuleNo : optional:(int) fuer PART II - durchlaufe fuer genau eine Regel mit aussetzen der
###                                             Vollstaendigkeitspruefung der Quell-Regeln
### @return     : rules{}, (int) cnt    2 Rueckgaben, 1xFormat s.o., 1xZaehler der gesetzten Kombinationen
def generatePossibilities(rules, specRuleNo=None):
    ### prueft, Regel fertig ist, also alle Kombinationen in der Regel Possibs haben
    ### @ruleNo     : (int) Nr der Regel
    ### @return     : (bool) Alle Regel-Kombinationen gesetzt =True, sonst =False
    def checkRuleComplete(ruleNo):
        combs = rules[ruleNo]
        for combKey in combs:
            if not checkCombComplete(ruleNo, combKey):
                return False
        return True

    ### prueft, ob Kombination fertig ist, also Possibs vorhanden sind
    ### @ruleNo     : (int) Nr der Regel
    ### @combKey    : (str) Kombinations-Schluessel
    ### @return     : (bool)  Wenn Possibs gesetzt (Liste vorhanden), ist Comb bereits ausgefuert (=True),
    ###                       Wenn keine Possibs vorhanden, dann (=False)
    def checkCombComplete(ruleNo, combKey):
        if not isinstance(rules[ruleNo][combKey], list):
            return False
        else:
            return True

    ### prueft eine Liste von Regeln, alle Regeln zusammen fertig sind
    ### also alle Kombinationen aller Regeln Possibs haben
    ### @ruleKeys   : [(int)] Liste von Regel-Nummern
    ### @return     : (bool)  True=wenn alle Regeln erledigt, 
    ###                       False=wenn mind. 1 Kombination in einer Regel keine Possibs hat
    def checkListRulesComplete(ruleKeys):
        for ruleKey in ruleKeys:
            if not checkRuleComplete(ruleKey):
                return False
        return True

    ### Gibt alle Moeglichkeiten (possibs) einer Regel (rule) zurück
    ### @ruleNo     : (int) Nr. der Regel
    ### @return     : [possib] Liste der Moeglichkeiten, bspw ['aabba', 'abbba', ...]
    def getPossibsForRule(ruleNo):
        retPossibs = []        
        for combKey in rules[ruleNo]:
            possibs = rules[ruleNo][combKey]
            for possib in possibs:
                retPossibs.append(possib)
        return retPossibs

    ### Erzeugt aus zwei Listen alle moeglichen Kombinationen 
    ### und gibt diese als eine neue Liste zurueck
    ### Dabei wird die Reihenfolge der Listen eingehalten
    ### @lists      : [[str]]  mehrere Listen mit Zeichenketten
    ### @return     : [str]    eine Liste mit Zeichenketten
    def mergeLists(lists):
        if len(lists) == 1:
            return lists[0]
        list_temp = lists[0]
        for i in range(1,len(lists)):
            list_start = list_temp
            list_temp = []
            for val1 in list_start:
                for val2 in lists[i]:
                    list_temp.append(val1+val2)
        return list_temp

    ### Durchlaufe alle Regeln, die noch nicht komplett sind
    ### @return     : (int) Zaehler der gesetzten Kombinationen
    def generate():
        cntChg = 0
        for ruleKey in (ruleKeys for ruleKeys in rules if not checkRuleComplete(ruleKeys)): #rules:
            ### Durchlaufe alle Matches, die noch nicht gefuellt sind
            combs = rules[ruleKey]
            for combKey in (combKeys for combKeys in combs if not checkCombComplete(ruleKey, combKeys)):
                ### Extrahiere alle QuellRegeln im Match
                srcRules = list(map(int,combKey.split(" ")))
                ### Wenn alle Quell-Regeln fertig gefuellt sind, dann alle Kombinationen holen und kombinieren
                listPossibsForRules = []            #-> var[0..n][0..n]  = possib
                                                    #       +------------- counter rules
                                                    #             +------- counter possibs
                if checkListRulesComplete(srcRules):
                    for srcRuleKey in srcRules:
                        listPossibsForRules.append(getPossibsForRule(int(srcRuleKey))) 
                    ### Kombinationen erzeugen
                    listNewPossibs = mergeLists(listPossibsForRules)
                    ### Rueckgabewert hochzaehlen
                    cntChg += len(listNewPossibs)
                    ### Kombinationen zur Regel-Kombination speichern
                    rules[ruleKey][combKey] = listNewPossibs
        return cntChg

    ### Durchlaeuft genau eine vorgegebene Regel,
    ### dabei werden nur die gefuellten Combs der Quell-Regeln genommen
    ### Es mussen also nicht alls combs der Quell-Regeln belegt sein
    ### @ruleNo     : (int) Nr. der Regel
    ### @return     : (int) Zaehler der gesetzten Kombinationen
    def generateSpecRule(ruleNo):
        cntChg = 0
        ### Durchlaufe alle Matches, die noch nicht gefuellt sind
        combs = rules[ruleNo]
        for combKey in combs: #(combKeys for combKeys in combs if not checkCombComplete(ruleNo, combKeys)):
            ### Extrahiere alle QuellRegeln im Match
            srcRules = list(map(int,combKey.split(" ")))
            ### Alle Quell-Regeln durchlaufen und vorh. Kombinationen holen und kombinieren
            listPossibsForRules = []            #-> var[0..n][0..n]  = possib
                                                #       +------------- counter rules
                                                #             +------- counter possibs
            for srcRuleKey in srcRules:
                listPossibsForRules.append(getPossibsForRule(int(srcRuleKey))) 
            ### Kombinationen erzeugen
            listNewPossibs = mergeLists(listPossibsForRules)
            ### Rueckgabewert hochzaehlen
            cntChg += len(listNewPossibs)
            ### Kombinationen zur Regel-Kombination speichern
#            print("ruleNo:", ruleNo)
#            print("+--> rules[ruleNo][combKey]:",len(rules[ruleNo][combKey]))
#            print("+--> listNewPossibs        :",len(listNewPossibs))
            if len(rules[ruleNo][combKey]) > 0:
                rules[ruleNo][combKey] = rules[ruleNo][combKey] + listNewPossibs
            else:
                rules[ruleNo][combKey] = listNewPossibs
        return cntChg

    if isinstance(specRuleNo, int):
        cntChg = generateSpecRule(specRuleNo)       # -> PART II
    else:                  
        cntChg = generate()                         # -> PART I 

    return rules, cntChg
                    
### Druckt das Regelwerk lesbar aus
### @rules       : {} Regelwerke, Format s.o.
### @withPossibs : optional-(bool) gibt an, ob die Liste der gueltigen Werte auch mit angedruckt werden soll
###                                -> bei grossen Datenmengen sinnvoll auszuschalten
### @ruleNo      : optional-(int) Nummer, wenn nur eine Regel angedruckt werden soll, ansonsten leer (=None) lassen
def printRules(rules, withPossibs=True, ruleNo=None):
    import collections
    if ruleNo==None:
        rules_sorted = collections.OrderedDict(sorted(rules.items()))
    else:
        rules_sorted = {ruleNo: rules[ruleNo]}
    for ruleKey in rules_sorted:
        print("RULE: ", ruleKey, "  ----------------")
        combs = rules[ruleKey]
        for combKey in combs:
            if withPossibs:
                print ("      COMB:", combKey, " - ", rules[ruleKey][combKey])
            else:
                print ("      COMB:", combKey, " - Anzahl possibs:", len(rules[ruleKey][combKey]))

### Prueft, wieviele Nachrichten gueltig sind
### @rules       : {} Liste der Regeln, Format s.o.
### @msg         : [] Liste der Nachrichten
### @checkRuleNo : -optional (int) statt mit RuleNr. 0 zu pruefen, kann hier optional ein andere RuleNr. angegeb.
### @return      : Anzahl der Nachrichten, die gueltig sind
def cntValidMessages(rules, msgs, checkRuleNo=0):
    cntValid = 0
    mergedPossibs = []
    for combKey in rules[checkRuleNo]:
        mergedPossibs += rules[checkRuleNo][combKey]
    for msg in msgs:
        if msg in mergedPossibs:
            #print("-->valid msg: ", msg)
            cntValid += 1
    return cntValid



rules, msg = readInputFile(FILENAME)
print("... readInputFile completed.")

cntChg = 99
while cntChg > 0:
    rules, cntChg = generatePossibilities(rules)
print("... generatePossibilities completed.")
#printRules(rules, True)

print()
#print("PART I  : Number of messages completely match rule 0                         : ", \
#                                                                cntValidMessages(rules, msg))
print()


#### 
#printRules(rules, False)
#printRules(rules, False, 0)
#printRules(rules, False, 8)
#printRules(rules, False, 11)
#printRules(rules, True, 31)
#printRules(rules, True, 42)

### msgs pruefen, ob beginnen mit possibs aus rule=42,
### dann pruefen, ob weiter mit rule=42 oder rule = 32

### 1. Sammle alle possibs von rule=42 und rule=32
def collectPossibsOfRule(ruleNo):
    ret = []
    for combKey in rules[ruleNo]:
        for possibs in rules[ruleNo][combKey]:
                ret.append(possibs)
    return ret

possibs42 = collectPossibsOfRule(42)
#print("possibs42: "+ str(possibs42))
possibs31 = collectPossibsOfRule(31)
possibsAll = possibs42 + possibs31

print("len(possibs42) :", len(possibs42))
print("len(possibs31) :", len(possibs31))
print("len(possibsAll):", len(possibsAll))

### 2. reduziere msg-liste um alle, die nicht mit rule=42 anfangen und schneide vorne rule 42 ab
print("Runde 0: len(msg)       :", len(msg))
def reduceMsgList(msg_input, possibs):
    msg_output = []
    cntValid   = 0
    cntInvalid = 0
    for m in (msgs for msgs in msg_input if len(msg_input)>0):
        if m[:8] in possibs:
            if len(m[8:]) == 0:
                cntValid += 1
            else:
                msg_output.append(m[8:]) 
        else:
            cntInvalid += 1
    return cntValid, cntInvalid, msg_output

cntValid, cntInvalid, msg_output = reduceMsgList(msg, possibs42)
cntValidSum   = cntValid
cntInvalidSum = cntInvalid
print("Runde 0x: len(msg_output):", len(msg_output), " -cntValid:",cntValid, " -cntValidSum:",cntValidSum, \
                                              " -cntInvalid:", cntInvalid," - cntInvalidSum:", cntInvalidSum)
for i in range(1,13):
    cntValid, cntInvalid, msg_output = reduceMsgList(msg_output, possibs42)
    cntValidSum   += cntValid
    cntInvalidSum += cntInvalid
    print("Runde ",i,": len(msg_output):", len(msg_output), " -cntValid:",cntValid, " -cntValidSum:",cntValidSum, \
                                                  " -cntInvalid:", cntInvalid," - cntInvalidSum:", cntInvalidSum)


### rules[RuleNo][('n n n')][0..n]      = (str) possib / possibs: Ein gueltiges Ergebnis dieser Regel-Kombination 


print()
print("PART II : Number of messages completely match rule 0 after updating rule 8+11: ", 0)
print()
