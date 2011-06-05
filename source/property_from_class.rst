:func:`property_from_class`
===========================

This section shows how using a class decorator, based upon
:doc:`dict_from_class`, can make it much easier to define complex
properties.  But first we review properties.

.. testsetup::

   from jfine.classtools import dict_from_class



About properties
----------------

The :func:`property` type is a way of 'owning the dot' so that
attribute getting, setting and deletion calls specified functions.

One adds a property to a class by adding to its a body a line such as
the following, but with suitable functions for some or all of fget,
fset and fdel.  One can also specify doc to give the property a
doc-string.

.. code-block:: python

   attrib = property(fget=None, fset=None, fdel=None, doc=None)

If all one wants is to specify fset (which is a common case) you can
use property as a decorator.  This works because fget is the first
argument.

For example, to make the area of a rectangle a read-only property you
could write:

.. code-block:: python

   @property
   def attrib(self):
       return self.width * self.length


Suppose now you have a property that you wish to both get and set.
Here's the syntax we'd like to use.

.. code-block:: python

   @property_from_class
   class attrib(object):
       '''Doc-string for property.'''

       def fget(self):
          '''Code to get attribute goes here.'''

       def fset(self):
          '''Code to set attribute goes here.'''


We will now construct such a decorator.


Definition of :func:`property_from_class`
-----------------------------------------

This function, designed to be used as a decorator, is applied to a
class and returns a property.  Notice how we pick up the doc-string as
a separate parameter.  We don't have to check for unwanted keys in the
class dictionary - :func:`property` will do that for us.

>>> def property_from_class(cls):
...
...     return property(doc=cls.__doc__, **dict_from_class(cls))


Using :func:`property_from_class`
---------------------------------

Here is an example of its use.  We add a property called value, which
stores its data in _value (which by Python convention is private).  In
this example, we validate the data before it is stored (to ensure that
it is an integer).

>>> class B(object):
...    def __init__(self):
...        self._value = 0
...
...    @property_from_class
...    class value(object):
...        '''The value must be an integer.'''
...        def fget(self):
...            return self._value
...        def fset(self, value):
...            # Ensure that value to be stored is an int.
...            assert isinstance(value, int), repr(value)
...            self._value = value


Here we show that :class:`B` has the required properties.

>>> b = B()
>>> b.value
0

>>> b.value = 3

>>> b.value
3

>>> B.value.__doc__
'The value must be an integer.'

>>> b.value = 'a string'
Traceback (most recent call last):
AssertionError: 'a string'


Unwanted keys
-------------

If the class body contains a key that property does not accept we for
no extra work get an exception (which admittedly could be a clearer).

>>> @property_from_class
... class value(object):
...    def get(self):
...        return self._value
Traceback (most recent call last):
TypeError: 'get' is an invalid keyword argument for this function

