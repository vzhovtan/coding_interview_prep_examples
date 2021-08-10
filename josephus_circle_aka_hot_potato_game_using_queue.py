"""
In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 
At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.

This game is a modern-day equivalent of the famous Josephus problem. 
Based on a legend about the famous first-century historian Flavius Josephus, 
the story is told that in the Jewish revolt against Rome, Josephus and 39 of his comrades held out against the Romans in a cave.
With defeat imminent, they decided that they would rather die than be slaves to the Romans. 
They arranged themselves in a circle. One man was designated as number one, and proceeding clockwise they killed every seventh man. 
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist, num):
    hotqueue = Queue()
    for name in namelist:
        hotqueue.enqueue(name)

    while hotqueue.size() > 1:
        for _ in range(num):
            hotqueue.enqueue(hotqueue.dequeue())
        hotqueue.dequeue()

    return hotqueue.dequeue()

# driver code
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],2))
