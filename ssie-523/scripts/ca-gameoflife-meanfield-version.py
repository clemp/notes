import pycxsimulator
from pylab import *

width = 50
height = 50
initProb = 0.2

def initialize():
    global time, config, nextConfig, density
    density = [initProb]

    time = 0
    
    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            if random() < initProb:
                state = 1
            else:
                state = 0
            config[y, x] = state

    nextConfig = zeros([height, width])

def observe():
    subplot(1, 2, 1)
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    axis('image')
    title('t = ' + str(time))
    subplot(1, 2, 2)
    cla()
    plot(density)

def update():
    global time, config, nextConfig, density

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            numberOfAlive = 0
            #for dx in range(-1, 2):
            #    for dy in range(-1, 2):
            #        numberOfAlive += config[(y+dy)%height, (x+dx)%width]
            for i in range(8):
                numberOfAlive += config[randint(height), randint(width)]
            if state == 0 and numberOfAlive == 3:
                state = 1
            elif state == 1 and (numberOfAlive < 2 or numberOfAlive > 3):
                state = 0
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config
    
    # Calculate the percent of "on" cells within the grid
    density.append(sum(config)/(height*width))

pycxsimulator.GUI().start(func=[initialize, observe, update])
