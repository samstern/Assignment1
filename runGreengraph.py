from greengraph import Greengraph
import matplotlib.pyplot as plt

def runIt():
    mygraph=Greengraph('New York','Chicago')
    data = mygraph.green_between(20)
    plt.plot(data)
    plt.show()

if __name__=="__main__":
    runIt()