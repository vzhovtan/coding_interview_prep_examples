"""
Create a function to remove duplicated lines from file. As an example given file contains data captured from networking device
and some lines are slightly different and could be removed, like
- somehting
- something location blah-blah-blah
"""

def remove_duped_lines(filename, divider):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(line.split(divider)[0].strip())
    return set(data)  


# driver code
filename = "./interview/removing_duplicated_lines_file.txt"
divider = "location"
result = remove_duped_lines(filename, divider)
for item in result:
    print(item)
