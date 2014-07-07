#/usr/lib/python2.7
# GPL 2+; see LICENSE
# Copyright 2014 Frances Hocutt
#
# Random Stripe Generator - Create random 2-color stripe patterns
# Given the total number of rows and the desired percentage of Color 1, 
# generates a representation of random stripes. 
#
# Intended to facilitate easier design of knit and crochet patterns.


import random

#TODO: error-handling and input-sanitizing

#TODO: add options to use >2 colors

#TODO: make this into some sort of gui with a color-chooser so you can see 
#      what these patterns look like in your colors

#TODO: add an "about this" string here
rowcount = int(raw_input("How many rows in your pattern? \n"))
proportion = float(raw_input("What percent of these rows do you want to be Color 1? \n"))/100
rowscolor1 = int(round(rowcount * proportion))

rows = range(rowcount)

#randomly choosing without replacing which rows will be color1
color1 = random.sample(rows, rowscolor1)

# print the pattern on the command line with O for color1 and X for other color
# TODO: output a .png that you can save (can integrate w/gui someday)

for x in rows: 
    if x in color1: 
        print "1"
    else: 
        print "X" 

#TODO: Create a knitting pattern from this, like: 
#"Row 1: color 1. 
# Rows 2-4: color 2."
# etc.
