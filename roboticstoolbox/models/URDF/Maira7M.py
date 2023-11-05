#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.Robot import Robot
from spatialmath import SE3


class Maira7M(Robot):
    """
    Class that imports a Panda URDF model

    ``Maira7M()`` is a class which imports a Neura Robotics Maira7M robot definition
    from a URDF file.  The model describes its kinematic and graphical
    characteristics.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.Maira7M()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration
    - qs, arm is stretched out in the x-direction
    - qn, arm is at a nominal non-singular configuration

    .. codeauthor:: Jens Temminghoff
    .. adapted from panda code
    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "neura_description/robots/maira7M.urdf.xacro"
        )

        super().__init__(
            links,
            name=name,
            manufacturer="Neura Robotics",
            gripper_links=links[9],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.grippers[0].tool = SE3(0, 0, 0)

        self.qdlim = np.array(
            [2.1750, 2.1750, 2.1750, 2.1750, 2.6100, 2.6100, 2.6100, 3.0, 3.0]
        )

        self.qr = np.array([0, -0.3, 0, -2.2, 0, 2.0, np.pi / 4])
        self.qz = np.zeros(7)

        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover

    r = Maira7M()

    r.qz

    for link in r.grippers[0].links:
        print(link)
