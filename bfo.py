import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.bfo(50, tf.sphere_function, -5.12, 5.12, 100, 100)#, 1, 1, 0.75, 1.2)
animation(alh.get_agents(), tf.sphere_function, -6, 6, True, filename + tf.sphere_function.__name__)
