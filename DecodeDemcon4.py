# Demcon Challenge #4 – Festival Schedule Generator
# https://werkenbijdemcon.nl/challenge-4-festival-schedule-generator/
# 

import sys
import os
from operator import attrgetter

# Helper class to store the input
class Show:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

# Start the application by checking the input parameter
# The file name with the inputs is expected.
if len(sys.argv) == 1:
    sys.exit("Please provide the input file as application parameter.")

if not os.path.isfile(sys.argv[1]):
    sys.exit("Given file not found.")

# Read the given file and store the lines
inputStrings = open(sys.argv[1]).read().splitlines()

# For each input, create a 'Show' object and store it in the 'shows' list
shows = []
for inputString in inputStrings:
    inputPartStrings = inputString.split(' ')
    shows.append(Show(inputPartStrings[0], int(inputPartStrings[1]), int(inputPartStrings[2])))

# Sort the 'shows' list by 'start' time
shows = sorted(shows, key=attrgetter('start'))

# Iterate once over the 'shows' list.
# Goal is to create a 'schedule', being a list of list of Shows (yes, list of list)
# Each list in the schedule list represents a Stage, or parallel show.
schedule = []
for currShow in shows:
    # For each show, keep track of the potential best show to be planned next to
    addToStageIndex = -1
    bestEndTime = -1

    # Check the each list in the schedule, to see how well the last 'Show' connects with this one.
    for i in range(len(schedule)):
        currLastShow = schedule[i][-1]

        # The best 'Show' is the one with the least time between the end and start.
        if currLastShow.end < currShow.start and currLastShow.end > bestEndTime:
            addToStageIndex = i
            bestEndTime = currLastShow.end

    if addToStageIndex == -1:
        # It is possible that no fitting place is found for the current 'Show', eg. in case that it will overlap with all.
        # in that case, a new list (Stage) must be created to plan the 'Show'.
        schedule.append([currShow])
    else:
        # When a stage has been found where the current 'Show' can be planned after, add it to that list.
        schedule[addToStageIndex].append(currShow)

# When all 'Shows' have been divided, print the output to console.
for i in range(len(schedule)):
    print(f"Stage {i + 1}")
    for currShow in schedule[i]:
        print(f"\t{currShow.name} {currShow.start} {currShow.end}")
