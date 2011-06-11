.. TODO :func:`type(name, bases, dict)` give extra parentheses

type(name, bases, dict)
=======================

According to its docstring, there are two ways to call the
:func:`type` builtin.

>>> print type.__doc__
type(object) -> the object's type
type(name, bases, dict) -> a new type

.. TOOD: difference between type and class.

In this section we explore how to use :func:`type` to construct new
classes.


Constructing the empty class
----------------------------

As usual, we start with the empty class.  The __name__ attribute of
the class need not be the same as the name of the variable in which we
store the class.  When at top-level (in the module context) the class
command binds the class to the module object, using the name of the
class as the key.

When we use type, there is no link between the __name__ and the
binding.

>>> cls = type('A', (object,), {})

The new class has the name we expect.

>>> cls.__name__
'A'

Its docstring is empty.

>>> cls.__doc__ is None
True

It does not have a __module__ attribute, which is surprising.

>>> cls.__module__
Traceback (most recent call last):
AttributeError: __module__

This class does not have a __module__ attribute because to the things
that Sphinx does when running the doctest.  Ordinarily, the class will
have a __module__ attribute.

>>> sorted(cls.__dict__.keys())
['__dict__', '__doc__', '__weakref__']

The lack of a __module__ attribute explains the string representation
of the class.

>>> cls
<class 'A'>


Constructing any class
----------------------

We obtained the empty class, whose __dict__ has only the system keys,
by passing the empty dictionary to :func:`type`.  We obtain more
interesting classes by passing a non-empty dictionary.  We can at the
same time pass more interesting bases, in order to achieve
inheritance.

.. TODO Give examples/exercises for this.


Specifying __doc__, __name__ and __module__
--------------------------------------------

Let's try to use the dict argument to specify these special
attributes.

>>> body = dict(__doc__='docstring', __name__='not_A', __module__='modname')
>>> cls2 = type('A', (object,), body)

We have set the __docstring__ and __module__ attributes, but the
__name__ is still **A**.

>>> cls2.__doc__, cls2.__name__, cls2.__module__
('docstring', 'A', 'modname')
