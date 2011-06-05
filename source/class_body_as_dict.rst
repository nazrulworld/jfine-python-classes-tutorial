:func:`class_body_as_dict`
==============================

In this section we define a functions that gets a dictionary from a
class.  This dictionary contains all the information supplied in the
body of a class statement, except for the doc-string.


The __dict__ of the empty class
--------------------------------

Here's our empty class again:

>>> class A(object):
...     pass


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


Is the doc-string part of the body?
-----------------------------------

Soon we will define a function that copies the body, as a dictionary,
out of a class.  But first we must answer the question: Is the
doc-string part of the body of a class?

There is no completely satisfactory answer to this question, as there
are good arguments on both sides.  We choose NO, because for example
using the -OO command line option will *remove doc-strings*, and so
they are not an essential part of the body of the class.  (However,
-OO does *not* remove doc-strings produced explicitly, by assigning to
__doc__.)

The keys to be excluded are precisely the ones that the empty class
(which has an empty body) has.

>>> _excluded_keys = set(A.__dict__.keys())

Definition of :func:`class_body_as_dict`
----------------------------------------

This function simply filters the class dictionary, copying only the
items whose key is not excluded.

>>> def class_body_as_dict(cls):
...     return dict(
...         (key, value)
...         for (key, value) in cls.__dict__.items()
...         if key not in _excluded_keys
...         )

As expected, the empty class has an empty body.

>>> class_body_as_dict(A)
{}

Here's a class whose body is not empty.

>>> class B(object):
...     'This docstring is not part of the body.'''
...     s = 'a string'
...     def f(self): pass


We get what we expect for the body.  (See [somewhere] for why we need
the __func__.)

>>> class_body_as_dict(B) == dict(s='a string', f=B.f.__func__)
True

Here's another way of expressing the same truth.

>>> sorted(class_body_as_dict(B).items())
[('f', <function f at 0x...>), ('s', 'a string')]
