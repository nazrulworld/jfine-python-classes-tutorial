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


The __dict__ of the empty class
--------------------------------

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


The body of a class
-------------------

Here we define a function that copies the body, as a dictionary, out
of a class.  But first we must answer the question: Is the doc-string
part of the body of a class?

There is no completely satisfactory answer to this question, as there
are good arguments on both sides.  We choose NO as the answer, because
for example using the -OO command line option will *remove
doc-strings*, and so they are not an essential part of the body of the
class.  (However, -OO does *not* remove doc-strings produced
explicitly, by assigning to __doc__.)

The keys to be excluded are precisely the ones that the empty class
(which has an empty body) has.

>>> _excluded_keys = set(A.__dict__.keys())

The :func:`get_body` function simply filters the class dictionary,
copying only the items whose key is not excluded.

>>> def get_body(cls):
...     return dict(
...         (key, value)
...         for (key, value) in cls.__dict__.items()
...         if key not in _excluded_keys
...         )

As expected, the empty class has an empty body.

>>> get_body(A)
{}

Here's a class whose body is not empty.

>>> class B(object):
...     'This docstring is not part of the body.'''
...     s = 'a string'
...     def f(self): pass


We get what we expect for the body.  (See [somewhere] for why we need
the __func__.)

>>> get_body(B) == dict(s='a string', f=B.f.__func__)
True

Here's another way of expressing the same truth.

>>> sorted(get_body(B).items())
[('f', <function f at 0x...>), ('s', 'a string')]
