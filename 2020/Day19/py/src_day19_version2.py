#################################################
##### AdventOfCode 2020
#####
##### Day 19 - Monster Messages
#####
##### @author  Kim Sieber
##### @date    20.12.2020 - 2. Versuch, da PART II nicht selbst geloest werden konnte
##### With frienly help from: https://dev.to/qviper/advent-of-code-2020-python-solution-day-19-4p9d
##### HINWEIS:  In Version 1 wurden alle gueltigen Optionen erzeugt und anschliessen Msgs gegen diese Liste geprueft
#####           In dieser Version 2 wird je Msg das Regelwerk angewendet, keine vorherige Listen-Generierung
###################################################
### Parameter
FILENAME = "input.txt"

### Liest Datei ein
### @fileName  :   (str) Dateiname
### @return(1) :   {ruleNo: [0..n][0..n]  = (int) referenzierte Regel   }
###                          +------------- Regel-Set
###                                +------- Zaehler für referenzierte Regeln
###         Bsp:   {0: [[64, 19], [50, 15]] , ...}
###                {ruleNo: a|b }         = (str) Buchstab a oder b, keine weitere Listen verschachtelt
###         Bsp:   {64: "a"}
### @return(2) :   [(str)] Liste Messages
def readInput(fileName):
    inputFile = open(fileName, "r")
    input_rules, input_messages = inputFile.read().split("\n\n")
    input_rule_lines = input_rules.splitlines()
    messages = input_messages.splitlines()
    rules = {}
    for input_rule_line in input_rule_lines:
        ruleKey, rules_str = input_rule_line.split(": ")
        if rules_str[:1] == '"':
            rules[int(ruleKey)] = rules_str[1:2]
        else:
            rule_sets = rules_str.split(" | ")
            temp_sets = []
            for rule_set in rule_sets:
                rule_list = rule_set.split(" ")
                temp_rules = []
                for rule in rule_list:
                    temp_rules.append(int(rule))
                temp_sets.append(temp_rules)
            rules[int(ruleKey)] = temp_sets
    inputFile.close()
    return rules, messages

### Druckt Regel-Liste formatiert aus
### @rules      : {} Liste der Regeln, Format s.o.
def printRules(rules):
    import collections
    rules_sorted = collections.OrderedDict(sorted(rules.items()))

    for ruleNo in rules_sorted:
        print("ruleNo: ", ruleNo, " -> " + str(rules[ruleNo]))
def printMessages(messages):
    for message in messages:
        print(message)

### Prueft die Gueltigkeit einer Message auf dem Regelset
### @rule_set   : [0..n][0..n] Liste an Regel-Sets, bspw. [[64, 19], [50, 15]]
### @message    : (str) Zeichenfolge einer Message
### @return1    : (bool) True=Message gueltig, False=Message nicht gueltig
### @return2    : [] Liste Regelwerke
def checkValid(rules, rule_list, message):
    if len(rule_list) > len(message):
        return False
    if len(rule_list) == 0 and len(message) == 0:
        return True
    elif len(rule_list) == 0 or len(message) == 0:
        return False
    if isinstance(rule_list, str):
        if message[0] == rule_list:
            return True
    else:
        ruleNo = rule_list.pop()
        if isinstance(ruleNo, str):
            if message[0] == ruleNo:
                return checkValid(rules, rule_list[:], message[1:])
        else:
            for rule_set in rules[ruleNo]:
                if checkValid(rules, rule_list[:] + list(rule_set), message):
                    return True
    return False

### Zaehlt die gueltigen Messages
### @rule_set   : [0..n][0..n] Liste an Regel-Sets, bspw. [[64, 19], [50, 15]]
### @message    : [0..n] Liste der Messages
### @return     : (int) Anzahl der gueltigen Messages
def countValidMessages(rules, messages):
    cnt = 0
    for message in messages:
        if checkValid(rules, rules[0][0][:], "".join(reversed(message))):
            cnt += 1
    return cnt


rules, messages = readInput(FILENAME)

#printRules(rules)
#print()
#printMessages(messages)
print()

print("PART I  : Messages completely match with rule 0                 : ",countValidMessages(rules, messages))
print()
rules[8]  = [[42],[42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print("PART II : Messages completely match with rule 0, after updating : ",countValidMessages(rules, messages))
print()
