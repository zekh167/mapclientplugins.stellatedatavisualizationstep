
"""
MAP Client Plugin
"""

__version__ = '0.1.0'
__author__ = 'Zohreh Ekhlasi'
__stepname__ = 'Stellate Data Visualization'
__location__ = ''

# import class that derives itself from the step mountpoint.
from mapclientplugins.stellatedatavisualizationstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc