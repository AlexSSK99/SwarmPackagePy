import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.ca(40, tf.bohachevsky_function, -50, 50, 100, 50, mr=5)
animation(alh.get_agents(), tf.bohachevsky_function, -50, 50, True, filename + tf.bohachevsky_function.__name__)
