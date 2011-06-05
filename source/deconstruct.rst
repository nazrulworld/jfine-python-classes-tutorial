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
