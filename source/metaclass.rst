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

The metaclass of an object is the type of its type.

>>> def metaclass(obj):
...     return type(type(obj))

>>> metaclass(0)
<type 'type'>

>>> metaclass(metaclass)
<type 'type'>

It's quite hard to create an object whose metaclass is not type.
