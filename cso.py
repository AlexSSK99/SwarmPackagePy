import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.cso(50, tf.booth_function, -10, 10, 100, 20, pa=0.5, nest=10)
animation(alh.get_agents(), tf.booth_function, -10, 10, True, filename + tf.booth_function.__name__)
