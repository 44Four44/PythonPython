from Fire import *
class Sanctuary:
    def __init__(self):
        self.alarms = []
        self.fires = []

        # Fires
        with open ('/Users/EthanWang/Python/FireSystems/ethan-fires.txt', 'r') as file:
            data = file.readlines()
            for i in range (len(data)):
                info = data[i].split(',')
                self.fires.append(Fire(int(info[0]), int(info[1]), int(info[3]), int(info[4])))

        # Alarms
        with open ('/Users/EthanWang/Python/FireSystems/ethan-alarms.txt', 'r') as file:
            data = file.readlines()
            for i in range (len(data)):
                info = data[i].split(',')
                self.alarms.append(Alarm(int(info[0]), int(info[1]), int(info[2]), self))

        self.time = 0
        self.detected = 0

    # def OutPutDetectionTime(self):

    def UpdateTime(self):

        for fire in self.fires:
            fire.grow()

        for alarm in self.alarms:
            t = alarm.triggerTime()
            if t != -1 and not alarm.on:
                # print(t)
                alarm.on = True
                self.detected +=1

        self.time += 1
