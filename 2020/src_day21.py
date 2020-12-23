################################################
##### AdventOfCode 2020
#####
##### Day 21 - Allergen Assessment
#####
##### @author  Kim Sieber
##### @date    23.12.2020 
###################################################
### Parameter
FILENAME = "input.txt"

### Beispiel-Fall aufgelistet
### 
### dairy               fish                    soy
### =======     =====   =====   ====    ===     =====   =====
### mxmxvkd     kfcds   sqjhc   nhms                            (contains dairy, fish)
### mxmxvkd                             trh     fvjkl   sbzzf   (contains dairy)
###                     sqjhc                   fvjkl           (contains soy)
### mxmxvkd             sqjhc                           sbzzf   (contains fish)

### Dateistruktur Daten
### Liest Datei ein
### @file_name:    (str) Dateiname
### @return: food[0..n]['ing'][0..n]         = (str) Zutaten-Name  (ing=ingredients)
###                    ['all'][0..n]         = (str) Allergen-Name (all=allergens)
def readInput(file_name):
    food        = []
    input_file  = open(file_name, "r")
    food_list   = input_file.read().split("\n")
    for fo in food_list:
        ings, alls = fo.split(" (contains ")
        ing_list   = ings.split(" ")
        all_list   = alls.split(" ")
        for key, val in enumerate(all_list): all_list[key] = val[:-1]
        food.append({'ing': ing_list, 'all': all_list})
    input_file.close()
    return food

### Allergen-Liste erzeugen mit moegliche Zutaten, diese reduziert auf moegliche
### @food  :  [] Format s.o.
### @return:  alls[all_name][0..n] = (str) Zutaten-Name  (ing=ingredients)
def getAllergenList(food):
    alls = {}
    ### Setzt bei erster Liste alle Eintraege hinein
    ### ab 2. Liste werden alle uebereinstimmenden genommen, andere entfern
    def setIdentityEntries(list_base, list_in):
        if len(list_base) == 0:
            return list_in
        del_list = []
        for ent in (ent for ent in list_base if ent not in list_in):
            del_list.append(ent)
        for d in del_list:
            list_base.remove(d)
        return list_base

    ### Loescht Eintrag aus allen food_list_entries
    def delIng(del_ing):
        for a in (a for a in alls if len(alls[a]) > 1):
            if del_ing in alls[a]:
                alls[a].remove(del_ing)

    ### alle nicht-Moeglichen Ings aus Ing-Liste je Allergen entfernen
    for fo in food:
        for a in fo['all']:
            if a in alls.keys():
                alls[a] = setIdentityEntries(alls[a][:], fo['ing'][:])
            else:
                alls[a] = fo['ing']

    ### Eindeutige Ing-All - Zuordnungen aus allen anderen All-Listen entfernen 
    ### und wiederholen, bis alle eindeutig
    while sum(1 for a in alls if len(alls[a])>1) > 0:
        for a in alls:
            if len(alls[a]) == 1:
                delIng(alls[a][0])

    ### Liste innerhalb Dict entfernen
    for a in alls:
        alls[a] = alls[a][0]

    return alls

### Ermittelt alle Ingredients, die keine Allergene haben
### @food[0..n]['ing'][0..n]    = (str) Zutaten-Name  (ing=ingredients)
###            ['all'][0..n]    = (str) Allergen-Name (all=allergens)
### @alls{all_name}             = (str) zu Allergen zugehoeriges Ingredient
### @return  ing[0..n]          = (str) Liste Ingredients, die nicht in Allergen-Liste sind
def getIngNotInAllergensList(food, alls):
    ing = []
    for fo in food:
        for i in fo['ing']:
            if i not in alls.values():
                ing.append(i)
    return ing


food = readInput(FILENAME)

alls = getAllergenList(food)

ing = getIngNotInAllergensList(food, alls)

print()
print("PART I  : Number of ingredients, that do not containt allergens: ", len(ing))
print()

import collections
alls = collections.OrderedDict(sorted(alls.items()))
canonical_list = ""
for a in alls:
    if len(canonical_list)>0: canonical_list += ","
    canonical_list += alls[a]

print()
print("PART II : The canonical dangerous ingredient list is           : ", canonical_list)
print()

