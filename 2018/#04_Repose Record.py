################################################
### Advent of Code 2018
###
### Day 04 - Repose Record
###
### author:  Kim Sieber
### create:  10.12.2021
################################################

reports = [report for report in open("#04 Input", "r")]
reports.sort()

### Extrahiert die einzelnen Guards aus den Reports
### mit Sub-Liste für Sleep-Times und Summen
### @return:  guards[0..n] = {'id':10, 'len':50, 'maxSleepMin': 24, 'maxSleepMinCnt': 2
###                           'sleeps':[0..n] = {'sleep':5, 'wakesup':25, 'len':20}}
def getGuards(reports):
    ### Ermittelt den Index zu einer Guard-ID
    ### @return: int idx
    def getIndexOfID(guards, id):
        for i in range(len(guards)):
            if guards[i]['id'] == id:    return i
        return False

    ### Ermittelt die Minute mit den meisten Schlaf-Momenten und deren Anzahl
    ### @return: int maxSleepMinute, int maxSleepMinCnt
    def getMaxSleepMinute(guard):
        minutes = [0 for _ in range(60)]
        for sleep in guard['sleeps']:
            for min in range(sleep['sleep'],sleep['wakesup']):
                minutes[min] += 1
        return minutes.index(max(minutes)), minutes[minutes.index(max(minutes))]

    guards = []
    sleep  = {}
    for report in reports:
        report  = report.strip()
        minute  = int(report.split('] ')[0][-2:])
        command = report.split('] ')[1].strip()
        if command[:5] == 'Guard':
            id  = int(report.split('#')[1].split(' ')[0].strip())
            idx = getIndexOfID(guards, id)
            if idx is False:     # Eintrag neu
                guard = {'id':id, 'len':0, 'maxSleepMin':0, 'maxSleepMinCnt':0, 'sleeps':[]}
                guards.append(guard)
                idx   = getIndexOfID(guards, id)
        else:
            if command == 'falls asleep': 
                sleep['sleep'] = minute
            elif command == 'wakes up': 
                sleep['wakesup'] = minute
                sleep['len']     = minute - sleep['sleep'] 
                guards[idx]['sleeps'].append(sleep)
                sleep            = {}
    for i in range(len(guards)):
        guards[i]['len']            = sum([sleep['len'] for sleep in guards[i]['sleeps']])
        maxSleepMin, maxSleepMinCnt = getMaxSleepMinute(guards[i])
        guards[i]['maxSleepMin']    = maxSleepMin
        guards[i]['maxSleepMinCnt'] = maxSleepMinCnt
    return guards

### Gibt die ID des Guards zurück, der die meiste Schlafdauer (höche 'len') hat
### @return:  int  maxIdx
def getGuardMostSleep(guards):
    maxLen = 0
    maxIdx = 0
    for i in range(len(guards)):
        if guards[i]['len'] > maxLen:
            maxLen = guards[i]['len']
            maxIdx = i
    return maxIdx

  
guards = getGuards(reports)


### PART I
maxIdx = getGuardMostSleep(guards)
print('Part I   : ', guards[maxIdx]['id'] * guards[maxIdx]['maxSleepMin']) 


### PART II
minutes_count  = [0 for _ in range(60)]
minutes_max_id = [0 for _ in range(60)]

for guard in guards:
    if guard['maxSleepMinCnt'] > minutes_count[guard['maxSleepMin']]:
        minutes_count[guard['maxSleepMin']]  =  guard['maxSleepMinCnt']
        minutes_max_id[guard['maxSleepMin']] =  guard['id']
maxSleepMinCnt = max(minutes_count)
maxSleepMin    = minutes_count.index(maxSleepMinCnt)
maxSleepMinId  = minutes_max_id[maxSleepMin]

print('PART II  : ', maxSleepMinId * maxSleepMin)