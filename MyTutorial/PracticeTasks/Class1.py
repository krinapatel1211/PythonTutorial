class Robot:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} can run".format(self.name))

    def eat(self):
        print("{} cannot eat".format(self.name))

    def walk(self):
        print("{} can walk".format(self.name))


def main():
    robotkrina = Robot("Robot Krina", 60, 27)
    robotkrina.run()


main()