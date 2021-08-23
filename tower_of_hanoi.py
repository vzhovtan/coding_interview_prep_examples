"""
Create a function for tower of hanoi problem
"""
def hanoi_1(n, rod_from, rod_mid, rod_to):
    #when n-1 plates are in the final position
    if n == 1:
        print(f'plate 1 from {rod_from} to {rod_to}')
        return

    #moving n-1 plates off the largest one
    hanoi_1(n-1, rod_from, rod_to, rod_mid)

    #moving the actual largest one
    print(f'Plate {n} from {rod_from} to {rod_to}')
    
    #placing n-1 plate on the top of the largest one
    hanoi_1(n-1, rod_mid, rod_from, rod_to)

def hanoi_2(start, end, aux, n):
    if n == 0:
        return
    hanoi_2(start, end, aux, n-1)
    print("Move disk{} from {} to {}".format(n, start, aux))
    hanoi_2(aux, end, start, n-1)

#driver code
hanoi_1(3, "A", "B", "C")
hanoi_2("start", "end", "aux", 14)
    