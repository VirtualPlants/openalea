import inspect
#from openalea.core.service.plugin import plugins, plugin, register_plugin

PLUGINS = dict()

def plugins(group, tags, criteria, **kwargs):
    if not group in PLUGINS:
        return []
    else:
        return [plg for plg in PLUGINS[group] if all(tag in plg.tags for tag in tags) and all(hasattr(plg, criterion) and getattr(plg, criterion) == criteria[criterion] for criterion in criteria)]

def plugin(group, name):
    try:
        for plugin_class in PLUGINS[group]:
            if plugin_class.identifier == name:
                return plugin_class
        raise NotImplementedError()
    except:
        raise NotImplementedError()

def register_plugin(group, plugin_class):
    #plugin_class.identifier = plugin_class.__module__ + ':' + plugin_class.__name__

    #class PluginMetaclass(type):

    #    @property
    #    def implementation(cls):
    #        exec 'from '+ cls.modulename + ' import ' + cls.objectname in locals()
    #	    return locals()[cls.objectname]

    #class PluginClass(plugin_class):

    #    __metaclass__ = PluginMetaclass

    #plugin_class = PluginClass

    #if not group in PLUGINS:
    #    PLUGINS[group] = list()

    if not hasattr(plugin_class, 'identifier'):
        def get_identifier(self):
            return self.__class__.__module__ + ':' + self.__class__.__name__
        plugin_class.identifier = property(get_identifier, doc = """Identifier of the plugin""")

    if not hasattr(plugin_class, 'implementation'):
        if not hasattr(plugin_class, 'modulename'):
            raise AttributeError('\'plugin_class\' has no attribute \'modulename\'')
        elif not hasattr(plugin_class, 'objectname'):
            raise AttributeError('\'plugin_class\' has no attribute \'objectname\'')
        else:
            def get_implementation(self):
                exec 'from '+ self.modulename + ' import ' + self.objectname in locals()
                return locals()[self.objectname]
            plugin_class.implementation = property(get_implementation, doc = """Implementation of the plugin""")
    if not group in PLUGINS:
        PLUGINS[group] = []
    plugin_instance = plugin_class()
    PLUGINS[group].append(plugin_instance)
    return plugin_instance

class PluginFunctor(object):

    @staticmethod
    def factory(group, *tags, **criteria):

        class PluginFunctorSingleton(PluginFunctor):
            _group = group
            _tags = tags
            _criteria = criteria
            _aliases = dict()

        return PluginFunctorSingleton()

    def __contains__(self, name):
        if not name in self._aliases:
            try:
                plugin(self._group, name)
            except:
                return False
            else:
                return True
        else:
            return True

    def __delitem__(self, name):
        if not name in self._aliases:
            raise KeyError('\'name\' parameter is not a plugin alias')
        del self._aliases[name]

    def __getitem__(self, name):
        if name in self._aliases:
            name = self._aliases[name]
        return plugin(self._group, name) # Get the plugin class

    def __setitem__(self, name, value):
        if isinstance(value, basestring):
            value = plugin(self._group, value).identifier
            self._aliases[name] = value
            self.__class__.plugin = property(get_plugin, set_plugin, plugin_doc(self))
        elif inspect.isclass(value):
            if len(self._tags) == 0 and not hasattr(value, 'tags'):
                value.tags = []
            for tag in self._tags:
                if tag not in value.tags:
                    raise ValueError('\'value\' parameter: missing tag \'' + tag + '\'')
            for criterion in self._criteria:
                if not hasattr(value, criterion):
                    raise ValueError('\'value\' parameter: missing criterion \'' + criterion + '\'')
                elif not getattr(value, criterion) == self._criteria[criterion]:
                    raise ValueError('\'value\' parameter: criterion \'' + criterion
                            + '\' not equal to \'' + self._criteria[criterion] + '\'')
            value = register_plugin(self._group, value).identifier # Add a plugin
            if name is not None:
                self[name] = value # Get the plugin unique name
            self.__class__.plugin = property(get_plugin, set_plugin, doc=plugin_doc(self))
        else:
            raise TypeError('\'plugin\' parameter')

def get_plugin(self):
    return self._plugin

def set_plugin(self, name):
    self._plugin = name
    self.__class__.__call__ = staticmethod(self[self._plugin].implementation)

def plugin_doc(plugin_func):
    __doc__ = ['Implemented plugins:']
    for plugin_class in plugins(plugin_func._group, plugin_func._tags, plugin_func._criteria):
        __doc__.append(' - `' + plugin_class.identifier + '`') # modulename and objectname
        if plugin_class.__doc__:
            __doc__[-1] += ' * ' + (" " * (len(__doc__[-1]) + 3)).join(line.strip() for line in plugin_class.__doc__.splitlines())
    __doc__.append('')
    __doc__.append('Defined aliases:')
    for alias in plugin_func._aliases:
        __doc__.append(' * `' + alias + '` - Alias for plugin `' + plugin_func._aliases[alias] + '`')
    return '\n'.join(__doc__)

PluginFunctor.plugin = property(get_plugin, set_plugin)
