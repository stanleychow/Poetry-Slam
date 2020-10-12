import random

lines = []

def get_file_lines(filename):
    with open(filename) as f:
        for line in f:
            lines.append(line)
        return lines
    f.close()

get_file_lines('/Users/stanleychow/Poetry Slam/poem.txt')

reverse_lines = []
def lines_printed_backwards(lines_list):
    for i , item in enumerate(lines, start = 1):
        item = '{} {}'.format(i, item).strip()
        reverse_lines.append(item)
    reverse_lines.reverse()
    print(reverse_lines)

lines_printed_backwards('/Users/stanleychow/Poetry Slam/poem.txt')

def lines_printed_random(lines_list):
    with open(lines_list) as f:
        lines = f.readlines()
        for line in lines_list:
            print(random.choice(lines))
        f.close()

lines_printed_random('/Users/stanleychow/Poetry Slam/poem.txt')

def lines_printed_custom(lines_list):
    with open(lines_list) as f:
        lines = f.readlines()
        count = 0
        for line in f:
            count += 1
            if count % 2 == 0:
                print(line)
    f.close()
lines_printed_custom('/Users/stanleychow/Poetry Slam/poem.txt')

