"""
Find the Levenshtein distance between two given strings
The Levenshtein distance between two words is the 
minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other
"""

class Solution:
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)
        
        distance = [i for i in range(len(word2) + 1)]
        
        for i in range(1, len(word1) + 1):
            pre_distance_i_j = distance[0]
            distance[0] = i
            for j in range(1, len(word2) + 1):
                insert = distance[j - 1] + 1
                delete = distance[j] + 1
                replace = pre_distance_i_j
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                pre_distance_i_j = distance[j]
                distance[j] = min(insert, delete, replace)

        return distance[-1]

# driver code
print(Solution().minDistance("Rabbit", "Racket"))
