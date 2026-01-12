"""
EvoScriPy - A Python API for TECAN Freedom EVO robot protocol generation.

This module provides high-level abstractions for programming liquid-handling
protocols for TECAN Freedom EVO robots (EVO 75, 100, 200, etc.).

Main classes:
    - Protocol: Base class for defining robot protocols
    - Robot: Main interface for controlling the robot

Example usage:
    from robotevo.EvoScriPy import Protocol, Robot
    
    class MyProtocol(Protocol):
        def Run(self):
            # Protocol implementation
            pass
"""

__version__ = "0.1.0"
__author__ = "Ariel Vina-Rodriguez"
__license__ = "GPL-3.0"

# Import main classes for easier access
from .robot import Robot
from .protocol_steps import Protocol
from .labware import Labware
from .reagent import Reagent
from .instructions import Instruction

__all__ = [
    "Robot",
    "Protocol",
    "Labware",
    "Reagent",
    "Instruction",
]
