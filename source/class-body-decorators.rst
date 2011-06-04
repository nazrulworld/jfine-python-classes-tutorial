Class body decorators
=====================

When programming in Python, it's quite common to need a dictionary
whose keys are strings and whose values are functions.  However,
creating a dictionary of functions can be quite awkward, unless one
uses the class statement to do this.

This section shows how to create and use function values dictionaries,
by use of class body decorators.


.. testsetup::

   from jfine.classtools import get_body


Example: property
-----------------

Here is an example.  The :func:`property` type is a way of 'owning the
dot' so that attribute getting, setting and deletion calls specified
functions.

One adds a property to a class by adding to its a body a line such as
the following, but with suitable functions for some or all of fget,
fset and fdel.

.. code-block:: python

   attrib = property(fget=None, fset=None, fdel=None, doc=None)

If all one wants is to specify fset (which is a common case) you can
use property as a decorator.  For example, to make the area of a
rectangle a read-only property you could write:

.. code-block:: python

   @property
   def attrib(self):
       return self.width * self.length


Suppose now you have a property that you wish to both get and set.
Here's the syntax we'd like to use.

.. code-block:: python

   @class_as_property
   class attrib(object):

       def fget(self):
          '''Code to get attribute goes here.'''

       def fset(self):
          '''Code to set attribute goes here.'''


In this section we show how to construct such a decorator.
