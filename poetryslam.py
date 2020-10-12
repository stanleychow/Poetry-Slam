import random

lines = []

def get_file_lines(filename):
    with open(filename) as f:
        for line in f:
            lines.append(line)
        return lines

get_file_lines('/Users/stanleychow/Poetry Slam/poem.txt')

def lines_printed_backwards(lines_list):
    (lines.reverse())
    for i , item in enumerate(lines, start = 1):
        print(i, item)
    


lines_printed_backwards('/Users/stanleychow/Poetry Slam/poem.txt')
    
