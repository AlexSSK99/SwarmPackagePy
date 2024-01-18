import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.pso(100, tf.bohachevsky_function, -10, 10, 100, 50, w=0.95, c1=1.5)
animation(alh.get_agents(), tf.bohachevsky_function, -10, 10, True, filename + tf.bohachevsky_function.__name__)
