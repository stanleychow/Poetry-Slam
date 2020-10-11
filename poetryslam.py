# def get_file_lines(filename):
    # with open(filename) as f:
    #     content = f.readlines()
    #     content = [x.strip() for x in content]
lines = []
def get_file_lines(filename):
    with open(filename) as f:
        # lines = []
        for line in f:
            lines.append(line)
        return lines

get_file_lines('/Users/stanleychow/Poetry Slam/poem.txt')

def lines_printed_backwards(lines_list):
# (lines.reverse())
# for i , item in enumerate(lines, start = 1):
#     print(i, item)
enumerate_lines = enumerate(lines, 1)
enumerate_lines_list = list(enumerate_lines)
# enumerate_lines.reverse()
print(enumerate_lines_list[::-1])

# def lines_printed_backwards(lines_list):
#     file = open()
#     file.close()

# def lines_printed_random(lines_list):

# def lines_printed_custom(lines_list):
    
# get_file_lines('./words.txt')



# print(lines)