"""
Printing random line from large file and counting time for each option
"""

import random
import time

def get_random_line_1(filename):
    # reading the entire file - very slow
    start1 = time.time()
    res = []
    numb = random.randrange(1,100)
    with open(filename) as fd:
        for item in fd.readlines():
            res.append(item)
    print(res[numb], end="")
    end1 = time.time()
    print("Reading the entire file", "\n", end1-start1, "\n")

def get_random_line_2(filename):
    # using random.choice() function - slow
    """
    random.choice(seq)
    Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError
    readlines()
    Read and return a list of lines from the stream.
    """
    start = time.time()
    with open(filename) as fd:
        print(random.choice(fd.readlines()), end = "")
    end = time.time()
    print("using random.choice() and readlines()", "\n", end-start, "\n")

def get_random_line_3(filename):
    # enumerating fd to get the max amount of lines and selecting random line using file.seek() - slightly faster
    start = time.time()
    count = 0
    with open(filename) as fd:
        for i, _ in enumerate(fd):
            count = i
        choice = random.randint(0, count-1)
        fd.seek(choice)
        print(fd.readline(), end="")
    end = time.time()
    print("Enumerating file descriptor and using seek()", "\n", end-start, "\n")

def get_random_line_4(filename):
    # getting file size by file.seek(0, 2) in bytes, counting amount of lines assuming every line contains 100 bytes - fastes one
    """
    seek(offset, whence=SEEK_SET)
    Change the stream position to the given byte offset. offset is interpreted relative to the position 
    indicated by whence. The default value for whence is SEEK_SET. 
    Values for whence are:
    SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
    SEEK_CUR or 1 – current stream position; offset may be negative
    SEEK_END or 2 – end of the stream; offset is usually negative
    tell()
    Return the current stream position
    """
    start = time.time()
    count = 0
    with open(filename) as fd:
        fd.seek(0, 2)
        count = fd.tell()//100
        choice = random.randint(0, count-2)
        fd.seek(choice)
        fd.readline()
        line2 = fd.readline()
        print(line2, end="")
    end = time.time()
    print("Using seek() and tell() for I/O stream, assuming each line is 100 bytes", "\n", end-start, "\n")

def get_random_line_5(filename):
    # use reservoir sampling, edge case with resefvoir size = 1 is what we shoudl do
    """
    It can be solved in O(n) time. The solution also suits well for input in the form of stream. 
    The idea is similar to this post. Following are the steps.
    1) Create an array reservoir[0..k-1] and copy first k items of stream[] to it. 
    2) Now one by one consider all items from (k+1)th item to nth item. 
    …a) Generate a random number from 0 to i where i is the index of the current item in stream[]. Let the generated random number is j. 
    …b) If j is in range 0 to k-1, replace reservoir[j] with stream[i]
    The only challenge is we HAVE to KNOW n which is amount if entries in file
    """
    start = time.time()
    #An efficient Python3 program to randomly select k items from a stream of items
    #A function to randomly select k items from stream[0..n-1].
    def selectKItems(stream, n, k):
        i=0 #index for elements in stream[] 
        #create reservoir[] which is the output array. Initialize it with first k elements from stream[]
        reservoir = [0]*k
        for i in range(k):
            reservoir[i] = stream.__next__()
            
        #Iterate from the (k+1)thelement to nth element
        while(i < n):
            #Pick a random index from 0 to i.
            j = random.randrange(i+1)
            #If the randomly picked index is smaller than k, then replace the element present at the index with new element from stream
            if(j < k):
                reservoir[j] = stream.__next__()
            i+=1
        return reservoir    
                
    with open(filename) as fd:
        #assuming there are 5000 lines in the file and reservoir size is 1
        n = 5000
        k = 1
        res = selectKItems(fd, n, k)

    end = time.time()
    print("Following are k randomly selected items", res, "\n", end-start, "\n")

def get_random_line_6(filename):
    # modified version 4 getting file size by file.seek(0, 2) in bytes, 
    # taking random in filesize - 100 bytes assuming last 100 bytes are in last line
    # changing the offset to random number, reading the second line form offset 
    """
    fd.seek(0, 2) - change stream position to the end of the file
    fd.tell() Return the current stream position, which is file size at this time
    """
    start = time.time()
    with open(filename) as fd:
        fd.seek(0, 2)
        file_size = fd.tell() - 100
        cur_pos = random.randrange(file_size)
        fd.seek(cur_pos)
        fd.readline()
        line2 = fd.readline()
        print(line2, end="")
    end = time.time()
    print("Using seek() and tell() for I/O stream", "\n", end-start, "\n")

def get_random_line_7(filename):
    # from Python cookbook using the same resevoir sampling technic
    start = time.time()
    def randomLine(file_object):
        "Retrieve a random line from a file, reading through the file once"
        lineNum = 0
        selected_line = ''

        while True:
            aLine = file_object.readline()
            if not aLine: break
            lineNum = lineNum + 1
            # How likely is it that this is the last line of the file?
            if random.uniform(0,lineNum) < 1:
                selected_line = aLine
        fd.close()        
        return selected_line

    with open(filename) as fd:
        res = randomLine(fd)

    print(res)
    end = time.time()
    print("Python cookbook approach - slowest one", "\n", end-start, "\n")

def get_random_line_8(filename):
    # using random.choice() function and generator function
    """
    Using yiled to lazily iterate over fd
    """
    start = time.time()
    line_count = 0

    def get_gen(file_name):
        with open(file_name) as fd:
            for line in fd:
                yield line

    for _ in (get_gen(filename)):
        line_count += 1

    cur_pos = random.randrange(line_count)
    with open(filename) as fd:
        fd.seek(cur_pos)
        print(fd.readline(), end="")
    end = time.time()
    print("using generator", "\n", end-start, "\n")

# driver code
filename = "./interview/large_text_file.txt"
get_random_line_1(filename)
get_random_line_2(filename)
get_random_line_3(filename)
get_random_line_4(filename)
get_random_line_5(filename)
get_random_line_6(filename)
get_random_line_7(filename)
get_random_line_8(filename)