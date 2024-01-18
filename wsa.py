import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.wsa(20, tf.sum_of_different_powers_function, -1, 1, 100, 20, 1, 0.01)
animation(alh.get_agents(), tf.sum_of_different_powers_function, -1, 1, True, filename + tf.sum_of_different_powers_function.__name__)
