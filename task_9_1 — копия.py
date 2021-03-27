from time import sleep
class TrafficLights:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        sleep(7)
        print(self.__color[0])
        sleep(2)
        print(self.__color[1])
        sleep(1)
        print(self.__color[2])



a = TrafficLights()
a.running()

