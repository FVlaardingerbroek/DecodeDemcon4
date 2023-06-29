# Demcon Challenge #4 – Festival Schedule Generator
# https://werkenbijdemcon.nl/challenge-4-festival-schedule-generator/
# Author: FVlaardingerbroek
# Date: 2023-06-29

How to execute the code:
- Create a text file with on each line the data of a show, formatted like the example Input.txt (separate the data with a single space, and make sure the show name does not contain spaces):
  [show name] [show start time] [show end time]
- Make sure Python is installed
- Call the python script with the input file name as its parameter:
  python DecodeDemcon4.py Input.txt
- If the parameter is omitted, the file cannot be found or the contents are not according to the expected format, the application will return a message.
- The application will return the resulting schedule in the following format:
Stage 1
        show_9 1 9
        show_27 30 36
        show_15 37 44
Stage 2
        show_11 1 4
        show_14 5 10
        show_21 15 20
        show_13 26 29
        show_8 30 34
        show_19 35 44
Stage 3
        show_2 2 9
Stage 4
        show_7 2 9
Stage 5
        show_12 2 11
        show_5 15 20
        show_16 27 35
        show_17 36 39
        show_3 44 47
Stage 6
        show_18 4 10
        show_10 20 28
        ï»¿show_1 29 33
Stage 7
        show_29 5 13
        show_28 14 21
        show_20 22 30
        show_25 31 38
Stage 8
        show_23 6 9
Stage 9
        show_6 8 15
        show_24 19 23
        show_4 26 30
        show_30 33 36
        show_26 37 41
        show_22 42 46
