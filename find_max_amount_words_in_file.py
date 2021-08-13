"""
Load the text file, count all words and print first N most often words
"""

# small example how to sort dict by value without collection.counter
# dict1 = {"a": 1, "b": 9, "c": 4}
# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
# print(sorted_tuples)
# sorted_dict = {k: v for k, v in sorted_tuples}
# print(sorted_dict)

def max_words(file, n):
    dict_result = {}
    with open (file) as fd:
        for line in fd.readlines():
            if line.split():
                for word in line.split():
                    if word.lower() in dict_result.keys():
                        dict_result[word.lower()] += 1
                    else:
                        dict_result[word.lower()] = 1

    sorted_tuples = sorted(dict_result.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}  
    for k, v in sorted_dict.items():
        if n != 0:
            print(k, v)
            n -= 1

# dirver code
given_text_file = "./words.txt"
max_words(given_text_file, 10)

