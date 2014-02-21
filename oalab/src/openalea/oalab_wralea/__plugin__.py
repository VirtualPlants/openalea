# This file has been automatically generated by pkg_builder

from openalea.core import *

__name__ = 'openalea.OALab'
__version__ = '1.0.0'
__license__ = 'CeCILL-C'
__author__ = 'Julien Coste, Christophe Pradal'
__institutes__ = 'CIRAD, INRIA'
__description__ = ''
__url__ = 'http://openalea.gforge.inria.fr'

__editable__ = 'True'
__icon__ = ''
__alias__ = []

__all__ = []

from openalea.vpltk.catalog.factories import InterfaceFactory, ObjectFactory
from openalea.oalab.interfaces.all import (IApplet, IParadigmApplet, 
                                           IQTextWidget)

interface_IApplet = InterfaceFactory(IApplet)
__all__.append('interface_IApplet')

interface_IParadigmApplet = InterfaceFactory(IParadigmApplet)
__all__.append('interface_IParadigmApplet')

interface_IQTextWidget = InterfaceFactory(IQTextWidget)
__all__.append('interface_IQTextWidget')

LPyApplet = ObjectFactory(name='openalea:LPyApplet', 
                          description="LPyApplet", 
                          category="applets", 
                          interfaces=["openalea:IParadigmApplet"], 
                          nodemodule="openalea.oalab.plugins.lpy", 
                          nodeclass="LPyApplet")
__all__.append('LPyApplet')


PythonApplet = ObjectFactory(name='openalea:PythonApplet', 
                          description="PythonApplet", 
                          category="applets", 
                          interfaces=["openalea:IParadigmApplet"], 
                          nodemodule="openalea.oalab.plugins.python", 
                          nodeclass="PythonApplet")
__all__.append('PythonApplet')


RApplet = ObjectFactory(name='openalea:RApplet', 
                          description="RApplet", 
                          category="applets", 
                          interfaces=["openalea:IParadigmApplet"], 
                          nodemodule="openalea.oalab.plugins.r", 
                          nodeclass="RApplet")
__all__.append('RApplet')


VisualeaApplet = ObjectFactory(name='openalea:VisualeaApplet', 
                          description="VisualeaApplet", 
                          category="applets", 
                          interfaces=["openalea:IParadigmApplet"], 
                          nodemodule="openalea.oalab.plugins.visualea", 
                          nodeclass="VisualeaApplet")
__all__.append('VisualeaApplet')

