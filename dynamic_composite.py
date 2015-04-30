# -*- coding: utf-8 -*-

__all__ = ['DynamicComposite']


class DynamicComposite (object):
    def __init__(self, *subordinates):
        super(DynamicComposite, self).__setattr__(u'subordinates',
                                                  subordinates)

    def subordinate_with_attr(self, name):
        for sub in self.subordinates:
            if hasattr(sub, name):
                return sub
        raise AttributeError(u"'{}' object has no attribute '{}'".format(self.__class__, name))

    def __getattr__(self, name):
        return getattr(self.subordinate_with_attr(name),
                       name)

    def __setattr__(self, name, value):
        if name == u'subordinates':
            return super(DynamicComposite, self).__setattr__(name, value)
        return setattr(self.subordinate_with_attr(name),
                       name,
                       value)

