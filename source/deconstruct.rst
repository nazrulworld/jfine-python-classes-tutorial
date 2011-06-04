Deconstructing classes
======================

In :doc:`construct` we saw how to construct a class (by using the
**class** keyword).  In this section we see how to reverse the
process.

To use the **class** keyword you have to specify:

   #. A name for your class.

   #. A tuple of bases.

   #.  A class body.

In this section we see how to get this information back again.  Let's
do the easy stuff first.  Here's our empty class again:

>>> class A(object):
...     pass

Here's how to get the name of the class:

>>> A.__name__
'A'

And here's how to get the bases:

>>> A.__bases__
(<type 'object'>,)


The __dict__ of the empty class
--------------------------------

As seen in :doc:`construct`, even for the empty class its class
dictionary has entries.  Handling these always-there entries is a
nuisance when deconstructing classes.  Here, once again, is the list
of entries.

>>> sorted(A.__dict__.keys())
['__dict__', '__doc__', '__module__', '__weakref__']

The __dict__ and __weakref__ entries are there purely for system
purposes.  This makes them easier to deal with.

The class docstring __doc__ is None unless the user supplies a value.

>>> A.__doc__ is None
True

>>> class A2(object):
...     'This is the docstring'

>>> A2.__doc__
'This is the docstring'

Ordinarily, __module__ is the name of the module in which the class is
defined.  However, because of the way Sphinx uses doctest, it gets the
name of the module wrong.  Please don't worry about this.  Despite
what it says below, it's the name of the module.

>>> A.__module__
'__builtin__'

