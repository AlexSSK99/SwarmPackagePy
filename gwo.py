import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.gwo(12, tf.three_hump_camel_function, -5, 5, 100, 20)
animation(alh.get_agents(), tf.three_hump_camel_function, -5, 5, True, filename + tf.three_hump_camel_function.__name__)
