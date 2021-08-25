"""
Create a custom UNIX tail function to read last N lines fomr file or stream
"""

def custom_tail(filename, N):
    tail = []
    with open(filename) as fd:
        for line in fd.readlines():
            tail.append(line.replace("\n", ""))
            if len(tail) > N:
                tail.pop(0)

    return tail 

# driver code
filename = "./words.txt"
print(custom_tail(filename, 10))