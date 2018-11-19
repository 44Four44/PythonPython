import math
class Alarm:
    def __init__(self, x, y, detection_radius, Sanctuary):
        self.x = x
        self.y = y
        self.detection_radius = detection_radius
        self.Sanctuary = Sanctuary
        self.on = False

    def triggerTime(self):
        for fire in self.Sanctuary.fires:
            if math.hypot(fire.x - self.x, fire.y - self.y) < self.detection_radius + fire.r_smoke and not self.on:
                return str("Alarm detected at " + str(self.Sanctuary.time) + " seconds!")
            else:
                return -1
