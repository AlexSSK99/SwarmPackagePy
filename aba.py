import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.aba(60, tf.six_hump_camel_function, -5, 5, 100, 100)
animation(alh.get_agents(), tf.six_hump_camel_function, -5, 5, True, filename + tf.six_hump_camel_function.__name__)
