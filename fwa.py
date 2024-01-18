import os
import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation

filename = os.path.basename(__file__)

alh = SwarmPackagePy.fwa(50, tf.matyas_function, -10, 10, 100, 20, m1=2, m2=1, amp=1)
animation(alh.get_agents(), tf.matyas_function, -10, 10, True, filename + tf.matyas_function.__name__)
