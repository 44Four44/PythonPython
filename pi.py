import random

#setup
accuracy = 100000.0

inCircle = 0.0

for i in range (1, int(accuracy)):
    if (random.uniform(0, 1)**2 + random.uniform(0, 1)**2)**0.5 < 1:
        inCircle+=1

print(4*inCircle/accuracy)
