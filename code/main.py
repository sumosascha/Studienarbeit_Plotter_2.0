from robot import *
from plotter import *


"""
IRRELEVANT MIT BENUTZTUNG DER GUI
Main-Klasse fuer eine Benutzung des Programms ohne GUI.
Von hier aus koennen Roboter Objekte und die 
dazugehoerigen Plotter Objekte erzeugt werden. 
"""

if __name__ == '__main__':
    """Hier Name des Roboters (derzeit irrelevant und kann auf "test_roboter" gesetzt bleiben)
    und JSON-Datei des Roboters angeben"""
    robot = Robot("test_roboter", "_extra_Kind.json")
    #robot = Robot("test_roboter", "example_robot_hexapod.json")
    #robot = Robot("test_roboter", "example_robot_dh_test_fuer_jonas.json")
    # Hier koennen Transformationsmatrizen ausgegeben werden, Beispiel:
    print(f"Beispiel: DH-Matrix von 'root' zu Beta1-Gelenk:\n{robot.generate_dh_matrix_from_to('root', 'Beta1-Gelenk')}")
    # example_trans_matrix = robot.generate_dh_matrix_from_to('root', 'Beta1-Gelenk')
    # print(f"Inverse:\n{robot.calc_inverse_dh_matrix(example_trans_matrix)}")

    # Plotter Objekt wird erzeugt, eingerichtet und angezeigt
    plotter = Plotter(robot)
    plotter.plot(plotter.robot.root, plotter.axes, root=True)
    plotter.plotter_show()
