import random


class bot():
    def __init__(self, id_bot=0, node=0):
        self.id_bot = id_bot
        self.node = node
        self.fatigue = 0

    def __str__(self):
        return 'id_bot:{0}, node:{1}'.format(self.id_bot, self.node)

    def move_bot(self, neighbors, complexity):
        global delt_fatigue
        temp = self.node
        if neighbors:
            item = random.choice(range(len(neighbors)))
            node = neighbors[item]
            delt_fatigue = complexity[item]
            self.node = node
            self.fatigue += delt_fatigue
        else:
            print("Teleportation to start")
            self.node = 0
        print("{0} -> {1}(+{2} = {3})".format(temp, self.node, delt_fatigue, self.fatigue))



