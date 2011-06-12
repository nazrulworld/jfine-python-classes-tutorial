Decorators versus __metaclass__
===============================


>>> def bunch_from_dict(a_dict, name='a_bunch'):
...
...     __slots__ = sorted(a_dict.keys())
...     defaults = dict(a_dict)
...     bases = (BaseBunch,)
...
...     def __init__(self, **kwargs):
...         for d in defaults, kwargs:
...             for key, value in d.items():
...                 setattr(self, key, value)
...
...     body = dict(__slots__=__slots__, __init__=__init__)
...     return type(name, bases, body)



>>> class BaseBunch(object):
...    def __repr__(self):
...        body = ', '.join([
...            '%s=%r' % (key, getattr(self, key))
...            for key in self.__slots__
...        ])
...        return '%s(%s)' % (self.__class__.__name__, body)



>>> Point = bunch_from_dict(dict(x=0, y=0), 'Point')

>>> Point(x=1, y=3)
Point(x=1, y=3)

>>> Point()
Point(x=0, y=0)
