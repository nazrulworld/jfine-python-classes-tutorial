JavaScript objects
==================

Like Python classes
-------------------

In JavaScript all objects are part of an inheritance tree.  The
**create** function adds a node to the inheritance tree.

.. code-block:: javascript

   // A JavaScript object.
   js> root = {}

   // Prototype inheritance.
   js> create = function (obj) {
           var f = function () {return this;};
           f.prototype = obj;
           return new f;
       }

   js> a = create(root)
   js> b = create(a)

   js> a.name = 5
   js> a.name
   5
   js> b.name
   5

In Python classes inherit in the same way.

.. doctest::

   >>> root = type              # Most classes are instance of type.
   >>> class a(root): pass
   >>> class b(a): pass         # Class inheritance.

   >>> a.name = 5               # Just like JavaScript.
   >>> a.name
   5
   >>> b.name
   5

class explanation
^^^^^^^^^^^^^^^^^

In Python we can subclass anything whose type is **type** (or a
subclass of type).  A subclass (and its instances) inherits properties
from the super-class.

   >>> type(root) == type(a) == type(b) == type
   True



Custom item methods
-------------------

In JavaScript attribute and item access are the same.

.. code-block:: javascript

   js> a = create(root)

   js> a.name = 5
   js> a['name']
   5

   js> a['key'] = 6
   js> a.key
   6

   js> a[1] = 6
   js> a['1']
   6

In Python we can defined our own item methods.  (The programmer owns
the dot.)

.. doctest::

   >>> class A(object):
   ...
   ...     def __getitem__(self, key):
   ...         return getattr(self, str(key))
   ...     def __setitem__(self, key, value):
   ...         return setattr(self, str(key), value)

   >>> a = A()
   >>> a.name = 5

   >>> a['name']
   5

   >>> a['key'] = 6
   >>> a.key
   6

   >>> a[1] = 6
   >>> a['1']
   6

Because **type(a)** is **A**, which has the special item methods, we
get the special item behaviour.

.. doctest::

   >>> type(a) is A
   True


On metaclass
------------

Using previous definition, we cannot subclass **a** to create **b**.

.. doctest::

   >>> class b(a): pass
   Traceback (most recent call last):
       class b(a): pass
   TypeError: Error when calling the metaclass bases
       object.__new__() takes no parameters

This is because **a** is not a type.  The solution involves Python
metaclasses (an advanced topic).

.. doctest::

   >>> isinstance(a, type)
   False


metaclass construction
^^^^^^^^^^^^^^^^^^^^^^
We will subclass type, not object, and add to it the special item
methods.


.. doctest::

   >>> class ObjectType(type):
   ...
   ...     def __getitem__(self, key):
   ...         return getattr(self, str(key))
   ...
   ...     def __setitem__(self, key, value):
   ...         return setattr(self, str(key), value)

Here is a fancy way of calling **ObjectType**.

  .. doctest::

   >>> class root(object):
   ...     __metaclass__ = ObjectType


Here is a more direct (and equivalent) construction (create an
instance of **ObjectType**, whose instances are objects).

.. doctest::

   >>> root = ObjectType('root', (object,), {})
   >>> isinstance(root(), object)
   True

metaclass demonstration
^^^^^^^^^^^^^^^^^^^^^^^
.. doctest::

   >>> class a(root): pass
   >>> class b(a): pass

   >>> a.name = 5
   >>> a.name
   5
   >>> b.name
   5
   >>> a['name']
   5
   >>> b['name']
   5

   >>> a[1] = 6
   >>> a['1']
   6


metaclass explanation
^^^^^^^^^^^^^^^^^^^^^

Because **type(root)** is a subclass of type we can subclass root.

.. doctest::

   >>> issubclass(type(root), type)
   True

Because the **type(root)** is **ObjectType**, which has special item
methods, we get the special item behaviour.

.. doctest::

   >>> type(root) == type(a) == type(b) == ObjectType
   True


Never instantiated
------------------

We can't call JavaScript objects (unless they are a function).  But
**create** creates ordinary JavaScript objects.

.. code-block:: javascript

   js> a = create(root)
   js> a(1, 2, 3)
   TypeError: a is not a function


We will monkey-patch the previous Python class, to provide custom
behaviour when called.

.. doctest::

   >>> def raise_not_a_function(obj, *argv, **kwargs):
   ...     raise TypeError, obj.__name__ + ' is not a function'

   >>> ObjectType.__call__ = raise_not_a_function

   >>> a(1, 2, 3)
   Traceback (most recent call last):
        a(1, 2, 3)
   TypeError: a is not a function


Conclusion
----------

JavaScript objects are like Python classes (because they inherit like
Python classes).

For JavaScript attribute and item access are the same.  This is
achieved in Python by providing custom item methods.

In Python the custom item methods must be placed on the type of the
object (or a superclass of its type).

Ordinary JavaScript objects are not functions and cannot be called.  A
Python class can be called (to create an instance of the object).  But
we can override this behaviour by supplying a custom method for call.

To summarize:
..

  **JavaScript objects are like Python classes with custom item
  methods (on the metaclass) that are never instantiated.**

It's worth saying again:

..

   **JavaScript objects are like Python classes with custom item
   methods (on the metaclass) that are never instantiated.**



