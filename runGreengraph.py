from greengraph import Greengraph
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def runIt():

    parser = ArgumentParser(description = "Plot the proportion of green pixels in the series of Google Maps satellite images between two locations")
    parser.add_argument('--start', dest='start', default='New York', help='Where to start, defaults is New York')
    parser.add_argument('--end', dest='end', default='Chicago', help='Where to end, defaults is Chicago')
    parser.add_argument('--steps', default=20, help='How many steps between start and end, default is 20')
    arguments=parser.parse_args()

    mygraph=Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    runIt()