Class body decorators
=====================

When programming in Python, it's quite common to need a dictionary
whose keys are strings and whose values are functions.  However,
creating a dictionary of functions can be quite awkward, unless one
uses the class statement to do this.

This section shows how to create and use function values dictionaries,
by use of class body decorators.


.. testsetup::

   from jfine.classtools import dict_from_class

   # For use later.
   def class_body_decorator(fn):

      def wrapped_fn(cls):
          return fn(**dict_from_class(cls))

      return wrapped_fn


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

   @class_body_as_property
   class attrib(object):

       def fget(self):
          '''Code to get attribute goes here.'''

       def fset(self):
          '''Code to set attribute goes here.'''


We will now construct such a decorator.


:func:`class_body_as_property`
------------------------------

This function, designed to be used as a decorator, is applied to a
class and returns a property.  Notice how we pick up the doc-string as
a separate parameter.

>>> def class_body_as_property(cls):
...
...     return property(doc=cls.__doc__, **dict_from_class(cls))

Here is an example of its use.  We add a property called value, which
stores its data in _value (which by Python convention is private).  In
this example, we validate the data before it is stored (to ensure that
it is an integer).

>>> class B(object):
...    def __init__(self):
...        self._value = 0
...
...    @class_body_as_property
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

.. For later.
.. >>> class_body_as_property = class_body_decorator(property)

