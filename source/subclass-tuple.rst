Subclassing :class:`tuple`
==========================

Recall that with EmulBool in :doc:`subclass-int` we had to define a
__new__ method because we need to adjust the values passed to EmulBool
before the instance was created.


The desired properties of Point
--------------------------------

Since Python 2.6, :class:`namedtuple` has been part of the
:mod:`collections` module.  We can use it to provide an example of
what is required.

>>> from collections import namedtuple
>>> Point = namedtuple('Point', ('x', 'y'))

Here are some facts about the Point class.

1.  Point is a subclass of tuple.

    >>> Point.__bases__
    (<type 'tuple'>,)

2.  Two arguments are used to initialise a point.

    >>> p = Point(1, 2)

3.  A point has items at 0 and at 1.

    >>> p[0], p[1]
    (1, 2)

4.  We can access these items using the names *x* and *y*.

    >>> p.x, p.y
    (1, 2)


**Exercise** Write an implementation of Point, that satisfies the
above. (Please use the hints - they are there to help you.)

**Hint** To pass 1, 2 and 3 only three lines of code are required.

**Hint** To pass 4 use *property*, which replaces getting an attribute
by a function call.

**Hint** The elegant way to pass 4 is to use
:func:`operator.itemgetter`.  Use this, and you'll need only
another 3 lines of code in order to pass 4.


Answer
------

1. Point is a subclass of tuple.

   >>> class Point(tuple):
   ...    def __new__(self, x, y):
   ...        return tuple.__new__(Point, (x, y))

   >>> Point.__bases__
   (<type 'tuple'>,)


2.  Two arguments are used to initialise a point.

    >>> p = Point(1, 2)

3.  A point has items at 0 and at 1.

    >>> p[0], p[1]
    (1, 2)

4.  We can access these items using the names *x* and *y*.

    >>> import operator

    >>> Point.x = property(operator.itemgetter(0))
    >>> Point.y = property(operator.itemgetter(1))

    >>> p.x, p.y
    (1, 2)
