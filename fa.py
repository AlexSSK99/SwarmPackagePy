import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.fa(5, tf.cross_in_tray_function, -10, 10, 100, 100, alpha1=0.5, csi=0.8, psi=1.2)
animation(alh.get_agents(), tf.cross_in_tray_function, -10, 10, True, filename + tf.cross_in_tray_function.__name__)
