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

    
# lines_printed_backwards('/Users/stanleychow/Poetry Slam/poem.txt')

# def lines_printed_random(lines_list):
#     for lines in lines_list:
#         index = random.randint(0, len(lines_list)-1)
#         print(lines_list[index])

# lines_printed_random('/Users/stanleychow/Poetry Slam/poem.txt')

# def lines_printed_custom(lines_list):
#     for count, line in enumerate(lines_list, start = 1):
#         if count % 2 == 0:
#             print(line)

# lines_printed_custom('/Users/stanleychow/Poetry Slam/poem.txt')

