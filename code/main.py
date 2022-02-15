import matplotlib.pyplot as plt
import numpy as np
import math
from robot import *
from joint import *
from plotter import *
import json
from mpl_toolkits.mplot3d import Axes3D
import os
import time


"""
Hauptdatei, von hier aus können Roboter Objekte und die 
dazugehörigen Plotter Objekte erzeugt werden. 
"""

if __name__ == '__main__':
    robot2 = Robot("test_roboter", "example_robot_dh_fakechildren.json")

    # print(f"robot2: {robot2.root}")
    # print(f"dh to A: {robot2.generate_dh_matrix_from_to('root', 'Beta1-Gelenk')}")

    # robot2.set_joint("Alpha1-Gelenk", math.radians(45))

    # print(f"dh to A: {robot2.generate_dh_matrix_from_to('root', 'Beta1-Gelenk')}")
    plotter = Plotter(robot2)
    #plotter.update()


    plotter.plot(plotter.robot.root, plotter.axes, root=True)
    # plotter.set_joint_and_update()
    plotter.plotter_show()
    print("+n+n+n+n+n+")

    # while True:
    #     robot2.set_joint("Alpha1-Gelenk", math.radians(45))
    #     plotter.update()
    #     robot2.reset_joint_offsets("Alpha1-Gelenk")
    #     plotter.update()
    #     #plotter.plotter_show()
    #     #plotter.update()

    #funktioniert:
    #robot2.set_joint("Alpha1-Gelenk", math.radians(45))
    #plotter.update("bla")



    plotter.plotter_show()
    # time.sleep(3)
    # plotter.wait(3)
    #plotter.update()
    # counter = 0
    # direction = 1
    # plotter.fig.show()
    # while True:
    #     plotter.fig.show()

        #plotter.fig.canvas.draw()

    #     robot2.set_joint("Alpha1-Gelenk", math.radians(90)*counter)
    #     print(f"dh to A: {robot2.generate_dh_matrix_from_to('root', 'Beta1-Gelenk')}")
    #     plotter.update()
    #     counter = counter+(0.1*direction)
    #     if counter >= 1:
    #         direction = -1
    #     elif counter <= 0:
    #         direction = 1
    #     print(counter)