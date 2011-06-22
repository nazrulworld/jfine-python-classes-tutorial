Exercise: Your own class to class decorator
===========================================

This is an open exercise.  The task is to find a situation where you
need to change a class during its construction via a class statement,
and then to write a class to class decorator that does this.

Please use the class_to_class_data and class_data_to_class decorators,
either the ones supplied by the tutorial or your own (if you think
they are better).

Here's a template, to get you started.

.. code-block:: python

   def my_class_decorator(cls):

       class_data = class_data_from_class(cls)
       new_class_data = whatever_you_want_it_to_be
       new_cls = class_from_class_data(new_class_data)
       return new_cls


Here are some ideas

* Check that the class supplies certain methods

* Perform other checks on the class

* Change methods so all calls are logged

* Supply extra utility methods to the class

* Refactor existing code that depends on __metaclass__
