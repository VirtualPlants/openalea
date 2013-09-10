# -*- python -*-
#
#       Control classes for standard python types
# 
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2013 INRIA - CIRAD - INRA
#
#       File author(s): Julien Coste <julien.coste@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
__revision__ = ""

"""
Control classes for standard python types
"""

class Control(object):
    """ ABC for controls? """
    def __init__(self):
        super(Control, self).__init__() 
        self.name = ""
        self.value = ""
        
    def save(self):
        return repr(self.value)
    

class IntControl(Control):
    def __init__(self):
        super(IntControl, self).__init__() 
    
    @classmethod
    def default(cls):
        """
        Create a default control
        """
        self.name = "int"
        self.value = int()
  
    def edit(self):
        """
        Return a widget to edit object
        """
        pass
  
    def thumbnail(self):
        """
        Return a widget to visualize object
        """
        pass


class BoolControl(Control):
    def __init__(self):
        super(BoolControl, self).__init__() 
    
    @classmethod
    def default(self):
        """
        Create a default control
        """
        self.name = "bool"
        self.value = bool()
  
    def edit(self):
        """
        Return a widget to edit object
        """
        pass
  
    def thumbnail(self):
        """
        Return a widget to visualize object
        """
        pass

        
class FloatControl(Control):
    def __init__(self):
        super(FloatControl, self).__init__() 
    
    @classmethod
    def default(self):
        """
        Create a default control
        """
        self.name = "float"
        self.value = float()
  
    def edit(self):
        """
        Return a widget to edit object
        """
        pass
  
    def thumbnail(self):
        """
        Return a widget to visualize object
        """
        pass

        