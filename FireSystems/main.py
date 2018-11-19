from Sanctuary import *
building = Sanctuary()

run = True
zoom = 10

while run:
    # building.OutPutDetectionTime()
    for frame in range(zoom):
        building.UpdateTime()
        print("Amount of alarms that went off at " + str(building.time) + " seconds: "+ str(building.detected))
        building.detected = 0

