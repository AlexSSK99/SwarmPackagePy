import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.chso(25, tf.cross_in_tray_function, -10, 10, 100, 100, FL=1)
animation(alh.get_agents(), tf.cross_in_tray_function, -10, 10, True, filename + tf.cross_in_tray_function.__name__)
