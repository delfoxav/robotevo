"""
RobotEvo - Python library for TECAN Freedom EVO robot control.

A Python library for generating human-readable protocols and Freedom EVOware
scripts for TECAN Freedom EVO universal pipetting robots (EVO 75, 100, 200).

Main subpackages:
    - robotevo.EvoScriPy: Core API for protocol programming
    - robotevo.protocols: Example protocols and templates

Example usage:
    from robotevo.EvoScriPy import Protocol, Robot
    
    class MyProtocol(Protocol):
        def Run(self):
            # Protocol implementation
            pass

For more information, see: https://robotevo.readthedocs.io/
"""

__version__ = "0.1.0"
__author__ = "Ariel Vina-Rodriguez"
__license__ = "GPL-3.0"

__all__ = [
    "EvoScriPy",
    "protocols",
]
