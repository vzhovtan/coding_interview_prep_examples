"""
Merge sort
"""

def merge_sort(a_list):
    print(f"Splitting {a_list}")
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print(f"Merging {a_list}")

def merge_sort_pythonic(array):
    size = len(array)
    if size < 2:
        return array
    else:
        middle = size // 2
        left = merge_sort_pythonic(array[:middle])
        right = merge_sort_pythonic(array[middle:])

        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result 

# driver code
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
b_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("a_list", a_list)

merge_sort(a_list)
print("sorted with first func", a_list)

print("sorted with pythonic func", merge_sort_pythonic(a_list))

