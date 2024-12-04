#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
--- Advent of Code 2023                    ---
--- Day 12: Hot Springs                    ---
----------------------------------------------

Created: Tue Nov 19 21:55:44 2024
@author: Kim Sieber

Types of variables:
    records[0..n][0..1]
                  +----> [0]       = (str) spring-map, e.g. "????.#...#..."
                  +----> [1][0..n] = (int) spring-conditions, e.g. 4,1,1
    time_table{function-name: [0..1], ...}
                               +-----------> [0] Number of callings
                                             [1] Sum of working times in sec.

"""
import itertools
import time



def read_file(file_name: str) -> list:
        records = []
        lines   = [line.split(" ") for line in open(file_name, "r").read().splitlines()]
        for line in lines:
            records.append( [ line[0] + '.', [int(i) for i in line[1].split(",") ] ] )
        return records
            
def read_file_partII(file_name: str) -> list:
        ############ PART II ##############
        records_part_ii = []
        records = read_file(file_name)
        for record in records:
            records_part_ii.append([((record[0] + "?") * 5)[:-1], 
                                         (record[1] * 5)])
        return records_part_ii


def count_permutations(symbols, counts, group_loc=0):
        if not symbols:
            return not counts and not group_loc
        results = 0
        possibilities = ['.', '#'] if symbols[0] == '?' else symbols[0]
        for p in possibilities:
            if p == '#':
                results += count_permutations(symbols[1:], counts, group_loc + 1)
            else:
                if group_loc > 0:
                    if counts and counts[0] == group_loc:
                        results += count_permutations(symbols[1:], counts[1:])
                else:
                    results = results + count_permutations(symbols[1:], counts)
        return results
    
def get_all_count_permutation(records: list) -> int:
    return sum([count_permutations(s[0], s[1]) for s in records])
    
"""
                            
#################### NEW WAY  with more performance ###################################
    def get_number_of_combinations(self, spring_map, damaged_set):
        if not damaged_set:
            if "#" in spring_map: return 0
            else:                 return 1
    
        if not spring_map:
            if not damaged_set:   return 1
            else:                 return 0
    
        total_combinations = 0
    
        # if "." or "?"
        if spring_map[0] in [".", "?"]:
            total_combinations += self.get_number_of_combinations(spring_map[1:], 
                                                                  damaged_set)
    
        # if "#" or "?"
        if spring_map[0] in ["#", "?"]:
            if self.is_valid_condition(spring_map, damaged_set):
                total_combinations += self.get_number_of_combinations(
                                                spring_map[damaged_set[0] + 1:], 
                                                damaged_set[1:] )
    
        return total_combinations


    def is_valid_condition(self, spring_map, damaged_set):
        valid = ( damaged_set[0] <= len(spring_map)          and
                  "." not in spring_map[: damaged_set[0]]    and 
                  ( damaged_set[0] == len(spring_map)   or
                    spring_map[damaged_set[0]] != "#"     )      )
        return valid


    def get_all_total_combinations(self) -> int:
        count = 0
        for record in self.records:
            count += self.get_number_of_combinations(record[0], record[1])
        return count

    def get_all_total_combinations_unfold(self) -> int:
        count = 0
        for record in self.records_part_ii:
            count += self.get_number_of_combinations(record[0], record[1])
        return count





################################################################

    def get_sum_of_all_counts(self) -> int:
        count = 0
        for record in self.records:
            count += self.get_num_of_possible_combinations(record)
        return count
            
    
    def get_sum_of_all_counts_part_ii(self) -> int:
        count = 0
        return self.get_num_of_possible_combinations(self.records_part_ii[1])

        for record in self.records_part_ii:
            count += self.get_num_of_possible_combinations(record)
        return count
    
    
    def get_num_of_possible_combinations(self, record: list) -> int:
        qmp              = self.get_all_question_mark_positions(record[0])      #question_mark_positions
        combinations_bit = list(itertools.product(["0", "1"], repeat=len(qmp))) #Bit-Combinations, e.g. 001,010,011,...
        start_time = time.time()
        combinations     = 0                       
        new_comb         = ""
        place_holder     = ""
        for comb in combinations_bit:
            ### Additional check to reduze loops
            if sum(record[1]) == (comb.count("1") + record[0].count("#")):
                new_comb = record[0] 
                for i in range(len(comb)):
                    place_holder = "." if comb[i] == "0" else "#"
                    new_comb = new_comb[:qmp[i]] + place_holder + new_comb[qmp[i]+1:]
                if self.check_combination_to_spec(new_comb, record[1]):
                    combinations += 1
        time_table["get_possible_combinations"][0] += 1
        time_table["get_possible_combinations"][1] += time.time() - start_time
        return combinations
    

    def check_combination_to_spec(self, combination: str, specs: list) -> bool:
        start_time = time.time()
        specs_build = []
        cnt         = 0
        for i in range(len(combination)):
            if combination[i] == "#":
                cnt += 1
            else:
                if cnt > 0:
                    specs_build.append(cnt)
                cnt = 0
        if cnt > 0:
            specs_build.append(cnt)
        time_table["check_combination_to_spec"][0] += 1
        time_table["check_combination_to_spec"][1] += time.time() - start_time
        return specs == specs_build
        
    
    def get_all_question_mark_positions(self, string: str) -> list:
        start_time = time.time()
        positions = []
        for i in range(len(string)):
            if string[i] == "?":
                positions.append(i)
        time_table["get_all_question_mark_positions"][0] += 1
        time_table["get_all_question_mark_positions"][1] += time.time() - start_time
        return positions


    def print_records(self, records):
        for r in records:
            print(r)
        
        
################### S T A R T ###########################
#hs = hot_spring("#12 Test.txt")
hs = hot_spring("#12 Puzzle.txt")
        
start_time = time.time()
print(f"PART I a: The sum of all different arragements is {hs.get_sum_of_all_counts()}")
end_time  = time.time()
print (f"Laufzeit gesamt:  {end_time-start_time}")

#################### NEW WAY  with more performance ###################################
#print()
#start_time = time.time()
#print(f"PART IIb: The sum of all different arragements is {hs.get_all_total_combinations_unfold()}")
#end_time  = time.time()
#print (f"Laufzeit gesamt:  {end_time-start_time}")

#################### ANOTHER WAY  with most performance ###################################
hs2 = hot_spring("#12 Puzzle.txt")

print()
start_time = time.time()
print(f"PART IIb: The sum of all different arragements is {hs2.get_all_count_permutation()}")
end_time  = time.time()
print (f"Laufzeit gesamt:  {end_time-start_time}")

"""

start_time = time.time()
records = read_file("#12 Test.txt")
print(f"PART I : The sum of all different arragements is {get_all_count_permutation(records)}")
end_time  = time.time()
print (f"Laufzeit gesamt:  {end_time-start_time}")

start_time = time.time()
records = read_file_partII("#12 Test.txt")
print(f"PART II: The sum of all different arragements is {get_all_count_permutation(records)}")
end_time  = time.time()
print (f"Laufzeit gesamt:  {end_time-start_time}")