# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2014 INRIA - CIRAD - INRA
#
#       File author(s):
#            Julien Diener <julien.diener@inria.fr>
#            Guillaume Baty <guillaume.baty@inria.fr>
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

from openalea.vpltk.qt import QtGui, QtCore

import matplotlib
from matplotlib import pyplot

from matplotlib.backends import backend_qt4agg
from matplotlib.backends import backend_qt4

from matplotlib.backend_bases import FigureManagerBase
from matplotlib._pylab_helpers import Gcf

try:
    import matplotlib.backends.qt4_editor.figureoptions as figureoptions
except ImportError:
    figureoptions = None

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from matplotlib import _pylab_helpers

all_widgets = []


class MplFigure(Figure):

    def __getattribute__(self, *args, **kwargs):
        return Figure.__getattribute__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        print args
        return Figure.__setattr__(self, *args, **kwargs)


class MplCanvas(FigureCanvasQTAgg):

    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None):
        fig = MplFigure()
        FigureCanvasQTAgg.__init__(self, fig)
        self.figure.add_axobserver(self._on_axes_changed)

    def _on_axes_changed(self, *args):
        print 'redraw'
        self.draw()
        self.draw_idle()


class FigureManagerQT(FigureManagerBase):

    """
    Public attributes

    canvas      : The FigureCanvas instance
    num         : The Figure number
    toolbar     : The qt.QToolBar
    window      : The qt.QMainWindow
    """

    def __getattribute__(self, *args, **kwargs):
        return FigureManagerBase.__getattribute__(self, *args, **kwargs)

    def __init__(self, canvas, num):
        FigureManagerBase.__init__(self, canvas, num)
        self.canvas = canvas
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)


class MatplotlibWidget(QtGui.QFrame):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.canvas = MplCanvas()
        self.manager = FigureManagerQT(self.canvas, 0)
        all_widgets.append(self)
        self.activate()

        self.setFrameShape(QtGui.QFrame.Box)
        self.setFrameShadow(QtGui.QFrame.Plain)

        self._layout = QtGui.QVBoxLayout(self)
        self._layout.addWidget(self.canvas)

    def show_active(self):
        self.setFrameShape(QtGui.QFrame.Box)
        self.setStyleSheet("background-color: rgb(255, 0, 0);")

    def show_inactive(self):
        self.setStyleSheet("")
        self.setFrameShape(QtGui.QFrame.NoFrame)

    def hold(self, state=True):
        for axe in self.canvas.figure.axes:
            axe.hold(state)

    def set_num(self, num):
        if num == self.manager.num:
            return
        else:
            self.manager.num = num
            Gcf.figs[num] = self.manager

    def activate(self):
        def make_active(event):
            for widget in all_widgets:
                if widget.manager is self.manager:
                    _pylab_helpers.Gcf.set_active(self.manager)
                    widget.show_active()
                else:
                    widget.show_inactive()

        pyplot.ion()

        cid = self.manager.canvas.mpl_connect('button_press_event', make_active)
        self.manager._cidgcf = cid

        _pylab_helpers.Gcf.set_active(self.manager)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = MplCanvas(figure)
    return FigureManagerQT(canvas, num)


def draw_if_interactive():
    """
    Is called after every pylab drawing command
    """
    # if matplotlib.is_interactive():
    figManager = Gcf.get_active()
    if figManager is not None:
        figManager.canvas.draw_idle()

pyplot.switch_backend('qt4agg')
backend_qt4.draw_if_interactive = draw_if_interactive
backend_qt4agg.draw_if_interactive = draw_if_interactive

backend_qt4.new_figure_manager_given_figure = new_figure_manager_given_figure
backend_qt4agg.new_figure_manager_given_figure = new_figure_manager_given_figure
