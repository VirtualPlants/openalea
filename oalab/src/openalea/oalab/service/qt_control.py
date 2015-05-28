from openalea.core.control import Control
from openalea.core.control.manager import ControlContainer
from openalea.core.service.interface import interface_name
from openalea.core.plugin import iter_plugins
from openalea.vpltk.qt import QtGui
from openalea.oalab.gui.utils import ModalDialog

import weakref

"""
**preferred**: specify explicitly the name of the Qt control widget you want to use

**shape**: if None, tries to return a widget. 
If shape is a string, returns widget corresponding to this shape. 
If it's a list, search widget for first shape. If no widgets found, search for second shape and so on.
"""


def discover_qt_controls():
    # session = Session()
    # debug=session.debug_plugins
    # TODO: use plugin instance manager
    return [plugin for plugin in iter_plugins('oalab.qt_control')]


def qt_editor_class(iname, shape=None, preferred=None):
    iname = interface_name(iname)
    # Get all widget plugin for "iname" interface
    widget_plugins = qt_widget_plugins(iname)

    # If preferred widget(s) is/are specified, try to find it
    if isinstance(preferred, str):
        preferred_widgets = [preferred]
    else:
        preferred_widgets = preferred

    if preferred_widgets:
        for preferred in preferred_widgets:
            # Load widget specified with control
            for plugin in widget_plugins:
                if preferred == plugin.name:
                    widget_class = plugin.load()
                    return widget_class

    # No preferred widget specified or preferred widget not found.
    # We try to find a widget corresponding to shapes
    if shape is None:
        shapes = ['hline', 'large', 'small']
    elif isinstance(shape, str):
        shapes = [shape]
    else:
        shapes = list(shape)

    for shape in shapes:
        for plugin in widget_plugins:
            if shape in plugin.edit_shape or 'responsive' in plugin.edit_shape:
                widget_class = plugin.load()
                widget_class.shape = shape
                return widget_class
    return None


def widget(iname, value, shape=None, preferred=None):
    control = Control(iname.__class__.__name__, iname, value)
    return qt_editor(control, shape, preferred)


def qt_dialog(control=None, **kwds):
    """
    You can pass control factory arguments:
        - name: Control name
        - interface: Control interface
        - value: Control value

    You can also pass qt_editor factory arguments
        - shape: widget shape
        - preferred: preferred widget
    """
    autoapply = kwds.get('autoapply', False)
    if control is None:
        control = Control(**kwds)
    widget = qt_editor(control, **kwds)
    widget.autoapply(control, autoapply)
    dialog = ModalDialog(widget)
    if dialog.exec_() == QtGui.QDialog.Accepted:
        return widget.value()
    else:
        return None


def qt_editor(control, shape=None, preferred=None, **kwds):
    if preferred is None and control.widget:
        preferred = control.widget
    widget_class = qt_editor_class(control.interface, shape, preferred)
    # TODO: FIX THIS HACK
    if hasattr(widget_class, 'shape'):
        shape = widget_class.shape

    if widget_class:
        widget = None
        if issubclass(widget_class, QtGui.QWidget):
            widget = widget_class()
        else:
            widget = widget_class.edit(control, shape)
        if widget is not None:
            widget.set(control)
#             widget.show()
        return widget


def qt_container(container, **kwargs):
    widget = QtGui.QWidget()
    layout = QtGui.QFormLayout(widget)
    widget.editor = {}
    widget.control = {}
    for control in container.controls():
        editor = qt_editor(control, 'hline')
        if editor:
            widget.editor[control] = weakref.ref(editor)
            widget.control[control.name] = control
            layout.addRow(control.alias, editor)
    return widget


def qt_viewer(control, shape=None):
    pass


def qt_painter(control, shape=None, preferred=None):
    cname = control.interface.__class__.__name__
    widget_plugins = qt_widget_plugins(cname)
    widget_class = None
    if preferred:
        # Load widget specified with control
        for plugin in widget_plugins:
            if preferred == plugin.name and plugin.paint:
                widget_class = plugin.load()
                return widget_class.paint(control, shape)

    # Load first editor
    for plugin in widget_plugins:
        if plugin.paint:
            widget_class = plugin.load()
            return widget_class.paint(control, shape)


def edit(control):
    import sys
    if 'PyQt4.QtGui' in sys.modules or 'PySide.QtGui' in sys.modules:
        from openalea.vpltk.qt import QtGui
        if QtGui.QApplication.instance():
            if isinstance(control, Control):
                return qt_editor(control)
            elif isinstance(control, ControlContainer):
                return qt_container(control)
    else:
        raise NotImplementedError, 'Only Qt editors are supported'


def qt_widget_plugins(iname=None):
    """
    if iname is None, returns {'iname':[widget_plugin1, widget_plugin2, ...]}
    else: returns widget plugins for interface iname
    """
    if iname is None:
        plugins = discover_qt_controls()
        widget_plugins = {}
        for plugin in plugins:
            for iname in plugin.controls:
                widget_plugins.setdefault(iname, []).append(plugin)
        return widget_plugins
    else:
        widget_plugins = qt_widget_plugins()
        try:
            return widget_plugins[iname]
        except KeyError:
            return []
