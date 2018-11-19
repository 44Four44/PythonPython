from Alarm import *
class Fire:
    def __init__(self, x, y, r_smoke, rate_growth):
        self.x = x
        self.y = y
        self.r_smoke = r_smoke
        self.rate_growth = rate_growth

    def grow(self):
        self.r_smoke += self.rate_growth

    def print(self):
        print("LOL")
