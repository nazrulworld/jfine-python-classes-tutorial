Class body decorators
=====================

TODO: This needs a rewrite.

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

.. For later.
.. >>> class_body_as_property = class_body_decorator(property)

