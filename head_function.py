"""
Create a custom UNIX head function to read first N lines fomr file or stream
"""

def custom_head(filename, N):
    head = []
    with open(filename) as fd:
        for line in fd.readlines():
            head.append(line.replace("\n", ""))
            if len(head) > N:
                head.pop()

    return head 

# driver code
filename = "./words.txt"
print(custom_head(filename, 10))