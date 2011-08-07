Metaclass
=========


Every object has a type
-----------------------

In Python, every object has a type, and the type of an object is an
instance of type.

>>> type(0)
<type 'int'>
>>> isinstance(type(0), type)
True
>>> class A(object): pass
>>> type(A)
<type 'type'>
>>> a = A()
>>> type(a)
<class 'A'>

Even type has a type which is an instance of type (although it's a
little silly).

>>> type(type)
<type 'type'>
>>> isinstance(type, type)
True


The metaclass of an object
--------------------------

The metaclass of an object is defined to be the type of its type.

>>> def metaclass(obj):
...     return type(type(obj))

>>> metaclass(0)
<type 'type'>

>>> metaclass(metaclass)
<type 'type'>

It's quite hard to create an object whose metaclass is not type.


A trivial non-type metaclass
----------------------------

In Python anything that is a type can be subclassed.  So we can
subclass type itself.

>>> class subtype(type): pass

We can now use subtype in pretty much the same way as type itself.  In
particular we can use it to construct an empty class.

>>> cls = subtype('name', (object,), {})

Let's look at the type and metaclass of cls.

>>> type(cls), metaclass(cls)
(<class 'subtype'>, <type 'type'>)

Notice that type(cls) is not type.  This is our way in.  Here's an
instance of cls, followed by its type and metaclass.

>>> obj = cls()
>>> type(obj), metaclass(obj)
(<class 'name'>, <class 'subtype'>)

We have just constructed an object with a non-trivial metaclass.  The
metaclass of obj is subtype.


A non-trivial example
---------------------

When Python executes

    .. code-block:: python

        obj[key]

behind the scenes it executes

    .. code-block:: python

        obj.__getitem__[key]

Here's an example:

>>> class A(object):
...     def __getitem__(self, key):
...         return getattr(self, key)


>>> obj = A()
>>> obj['name']
Traceback (most recent call last):
AttributeError: 'A' object has no attribute 'name'

>>> obj.name = 'some value'
>>> obj['name']
'some value'


What's the point?
-----------------

There are two main reasons for introducing and using a metaclass, or
in other words a subclass of type.

1.  We wish to create classes whose behaviour requires special methods
    or other properties on the type of the class.  This sounds and is
    odd, but can useful.  In :doc:`javascript-objects` we use it to
    create an elegant and simple implementation in Python of
    JavaScript object semantics.

2.  We wish to make the class statement construct a class differently,
    somewhat as :func:`bool` construct a number differently from an
    :func:`int`.  This is described in :doc:`metaclass-attribute`,
    which is the next section.


