import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.ba(10, tf.easom_function, -30, 30, 100, 100)
animation(alh.get_agents(),tf.easom_function, -30, 30, True, filename + tf.easom_function.__name__)
