crabs = [int(f) for f in open("#07 Input", "r").readline().split(',')]
print('Part I    : ', min([sum([abs(i-crab) for crab in crabs]) for i in range(max(crabs)+1)] ),'    ||   Part II   : ', min([sum([sum(range(abs(i-crab)+1)) for crab in crabs]) for i in range(max(crabs)+1)]))
