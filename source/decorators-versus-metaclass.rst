Decorators versus __metaclass__
===============================

Alex Martelli's excellent book *Python in a Nutshell* contains, as an
example of the use of the __metaclass__ attribute, the construction of
a metaclass (subclass of type) such that inheriting from this
metaclass produces what he calls a Bunch, which he rightly says is
similar to the struct type in C.

Here we give a construction based on the decorator point of view.

First we define a function, which can be used as a decorator, that
returns a bunch class.


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

We now need to implement the BaseBunch class, from which the return
bunch classes will inherit __repr__ and, if we wish, other attributes.

>>> class BaseBunch(object):
...    def __repr__(self):
...        body = ', '.join([
...            '%s=%r' % (key, getattr(self, key))
...            for key in self.__slots__
...        ])
...        return '%s(%s)' % (self.__class__.__name__, body)

Here's an example of the creation of a Point class.

>>> Point = bunch_from_dict(dict(x=0, y=0), 'Point')

And here are examples of its use.

>>> Point(x=1, y=3)
Point(x=1, y=3)
>>> Point()
Point(x=0, y=0)

We can also use bunch_from_dict as a decorator.

>>> from jfine.classtools import dict_from_class
>>> @bunch_from_dict
... @dict_from_class
... class RGB(object):
...      'This is a docstring.'
...      red = green = blue = 0

Here's an example of the use of the RGB class.  It shows that the name
of the class is not being properly picked up.  This is an interface
problem rather than a problem with the decorator approach.  The name
is available to be used, but the interface is not making it available.
Similar remarks apply to the docstring.

>>> RGB(blue=45, green=150)
a_bunch(blue=45, green=150, red=0)


[TODO] Provide a discussion.
