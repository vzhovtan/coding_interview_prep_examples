import random

class MSD:
    """
    test class
    """
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSD({}) : {}".format(self.num_sides, self.current_value)

# driver code
my_die = MSD(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSD(6), MSD(20)]
print(d_list)
