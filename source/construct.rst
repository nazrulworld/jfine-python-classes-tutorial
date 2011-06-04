Constructing classes
====================

There are two basic ways of constructing classes in Python.  The best
known way is to use Python's :keyword:`class` keyword.  The other way
is to use Python's :func:`type` function.  This page covers the
keyword way. :doc:`using-type` is more powerful and sometimes more
convenient.  However, the keyword approach is the better way to get
started and in ordinary programming is the most convenient.

The empty class
---------------

We will start with the empty class, which is not as empty as it looks.

>>> class A(object):
...     pass

Like most Python objects, our empty class has a dictionary.  The
dictionary holds the attributes of the object.

>>> A.__dict__
<dictproxy object at 0x...>

Even though our class is empty, its dictionary (or more exactly
dictproxy) is not.

>>> sorted(A.__dict__.keys())
['__dict__', '__doc__', '__module__', '__weakref__']

Attributes __doc__ and __module__ are there for documentation, and to
give better error messages in tracebacks.  The other attributes are
there for system purposes.

In addition, our class two attributes that are not even listed in the
dictionary.  The __bases__ attribute is the list of base classes
provided in the original class statement.

>>> A.__bases__
(<type 'object'>,)

The method resolution order (mro) attribute __mro__ is computed from
the bases of the class.  It provides support for multiple inheritance.

>>> A.__mro__
(<class 'A'>, <type 'object'>)

For now the important thing is that even the empty class has
attributes.  (For IronPython and Jython the attributes are slightly
different.)

