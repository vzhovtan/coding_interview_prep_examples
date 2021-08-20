"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
"""

def longest_subsring_with_k_distinct_element(str, k):
    start = 0
    max_len = 0
    item_freq = {}

    for end in range(len(str)):
        right_item = str[end]
        if right_item not in item_freq.keys():
            item_freq[right_item] = 0
        item_freq[right_item] += 1


        while len(item_freq) > k:
            left_item = str[start]
            item_freq[left_item] -= 1
            if item_freq[left_item] == 0:
                del item_freq[left_item]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

# driver code
print(longest_subsring_with_k_distinct_element("araaaaci", 2))