Exercise: Class to and from class data
======================================

Sometimes __metaclass__ is used to amend the operation of a class
statement.  However always the same change can be done with a
decorator function, and often this is clearer and easier.

The exercise here is to produce some class from class decorators.  The
first task is to produce two decorators whose composition is trivial.

In other words this

.. code-block:: python

    @class_from_class_data
    @class_data_from_class
    class MyClass(object):
          pass

should be equivalent to this

.. code-block:: python

    class MyClass(object):
          pass

Once we have done this, it's a lot easier to modify classes during
construction, because so to speak the input-output has already been
dealt with.  Simply write a function that changes or creates a class
data object.

The decorator function class_data_from_class should produce
class_data, which we can regard as a tuple.

The decorator function class_from_class_data should produce a class
from the class data.

.. note::
  
   Don't assume that the type of MyClass is type.  It could be a
   subclass of type.
