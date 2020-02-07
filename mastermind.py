#!/usr/bin/python3
"""
This file cointain the mastermind game code
"""
import random

digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
input_range = ''

for i in range(4):
    input_candidate = random.choice(digits)
    # digit not repeated
    while input_candidate in input_range:
        input_candidate = random.choice(digits)
    input_range = input_range + input_candidate

# user iteration
print ("Welcome to MasterMind Game!")
print ("You have to guest a number with ", 4, "different digits")
proposal = input("What are your numbers?: ")

# attemps and coincidences
attemps = 1
while proposal != input_range:
    attemps = attemps + 1
    hits = 0
    coincidence = 0

    # verification of the input in the input_range
    if len(proposal) is not 4:
        print('You need 4 digits, try it again')
    else:
        for i in range(4):
            if proposal[i] == input_range[i]:
                hits = hits + 1
            elif proposal[i] in input_range:
                coincidence = coincidence + 1
        print ("Your proposal (", proposal, ") has", hits,
               "hits and ", coincidence, "coincidence.")
    # ask for the next proposal*
    proposal = input("Try it again: ")

print ("Congratulations ! You guess the numbers in ", attemps, "attemps.")
