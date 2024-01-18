import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.ca(5, tf.sum_squares_function, -10, 10, 20, 10)
animation(alh.get_agents(), tf.sum_squares_function, -10, 10, True, filename + tf.sum_squares_function.__name__)
