installation: sudo python setup.py install

usage: greengraph.py [-h] [--from START] [--to END] [--steps STEPS]
                     [--out OUT] [--format FORMAT]

Generates a graph of the proportion of green pixels in a series of satellite
images between two points

optional arguments:
  -h, --help       shows this help message and exit
  --start START     Where to start, defaults is New York
  --end END         Where to end, defaults is Chicago
  --steps STEPS    How many steps between start and end, default is 20
