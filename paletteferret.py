from __future__ import print_function, division

import json
from time import sleep
import random

import argparse

parser = argparse.ArgumentParser( description = 'Changes a random palette color periodically.' )
parser.add_argument( 'palette_size', type=int, help='The number of palette colors.' )
parser.add_argument( '--interval', type=float, default=1.0, help='How long to wait between palette changes (seconds).' )

args = parser.parse_args()

palette_size = args.palette_size
interval = args.interval

while True:
    palette_to_change = random.randint( 0, palette_size-1 )
    new_color = [ random.uniform(0,1), random.uniform(0,1), random.uniform(0,1) ]
    print( 'set-palette-colors ' + json.dumps( { palette_to_change: new_color } ) )
    sleep( interval )
