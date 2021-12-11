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

commands = []
guard_ids = []
for report in reports:
        minute  = int(report.split('] ')[0][-2:])
        command = report.split('] ')[1].strip()
        if command[:5] == 'Guard':
            id  = int(report.split('#')[1].split(' ')[0].strip())
            if id not in guard_ids: 
                guard_ids.append(id)
        elif command == 'falls asleep': 
            sleep = minute
        elif command == 'wakes up': 
            commands.append({'id':id, 'sleep':sleep, 'wakeup':minute})
    
guard_minutes = [[0 for _ in range(60)] for _ in range(len(guard_ids))]
for command in commands:
    idx = guard_ids.index(command['id'])
    for min in range(command['sleep'], command['wakeup']):
        guard_minutes[idx][min] += 1

### PART I
maxSleep = 0
maxIdx    = 0
for i in range(len(guard_ids)):
    if sum(guard_minutes[i]) > maxSleep: 
        maxSleep = sum(guard_minutes[i])
        maxIdx    = i

maxMin = guard_minutes[maxIdx].index(max(guard_minutes[maxIdx]))

print('Part I    : ', guard_ids[maxIdx] * maxMin)

### PART II
maxSleepCnt = 0
maxSleepMin = 0
maxSleepIdx = 0
for i in range(len(guard_ids)):
    if max(guard_minutes[i]) > maxSleepCnt: 
        maxSleepCnt = max(guard_minutes[i])
        maxSleepMin = guard_minutes[i].index(maxSleepCnt)
        maxSleepIdx = i

print('Part II   : ', guard_ids[maxSleepIdx] * maxSleepMin)