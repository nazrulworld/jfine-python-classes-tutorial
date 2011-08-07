Subclassing :class:`int`
========================

We subclass in order to create a new class whose behaviour is
inherited from the base classes, except that the new class can also
override and add behaviour.  Object creation is behaviour.  For most
classes it is enough to provide a different __init__ method, but for
immutable classes one often have to provide a different __new__
method.

In this section we explain why __new__ is needed, and give examples of
its use.  But first we review mutation.


Mutable and immutable types
---------------------------

Some objects in Python, such as dictionaries and lists, can be
changed.  We can change these objects after they have been made.  This
is called mutation.  The types :class:`dict` and :class:`list` are
called *mutable types*.

>>> x = []
>>> x.append(1)
>>> x
[1]

Some other objects, such as strings and tuples, cannot be changed.
Once made they cannot be changed.  They are called *immutable types*.

>>> y = 'abc'
>>> y[0] = 'A'
Traceback (most recent call last):
TypeError: 'str' object does not support item assignment


Enumerated integers and named tuples
------------------------------------

We will use enumerated integers as an example in this section.  In
Python, booleans are an example of an enumerated integer type.

However, our task in this section is not to use booleans but to
understand them.  This will allow us to create our own subclasses of
int and of immutable types.


The :class:`bool` type
----------------------

Here we review the :class:`bool` type in Python.

Comparisons return a boolean, which is either True or False.

>>> 1 < 2, 1 == 2
(True, False)

True and False are instance of the :class:`bool` type.
>>> type(True), type(False)
(<type 'bool'>, <type 'bool'>)

The :class:`bool` type inherits from :class:`int`.

>>> bool.__bases__
(<type 'int'>,)

Because True and False are (in the sense of inherit from) integers, we
can do arithmetic on them.

>>> True + True
2
>>> False * 10
0

We can even use boolean expressions as numbers (although doing so
might result in obscure code).

>>> a = 3; b = 4
>>> (a < b) * 10 + (a == b) * 20
10


Emulating :class:`bool` - the easy part
---------------------------------------

.. TODO Sphinx supports :class:`aaa` but not :type:`bbb`.

In this subsection, as preparation for enumerated integers, we will
start to code a subclass of :class:`int` that behave like
:class:`bool`.  We will start with string representation, which is
fairly easy.

>>> class MyBool(int):
...     def __repr__(self):
...         return 'MyBool.' + ['False', 'True'][self]

This give us the correct string representations.
>>> f = MyBool(0)
>>> f
MyBool.False

>>> t = MyBool(1)
>>> t
MyBool.True

But compare

>>> bool(2) == 1
True

with

>>> MyBool(2) == 1
False

In fact we have

>>> MyBool(2) == 2
True
>>> MyBool(2)
Traceback (most recent call last):
IndexError: list index out of range


Emulating :class:`bool` - what goes wrong
-----------------------------------------

In many classes we use __init__ to mutate the newly constructed
object, typically by storing or otherwise using the arguments to
__init__.  But we can't do this with a subclass of :class:`int` (or
any other immuatable) because they are immutable.

You might try

>>> class InitBool(int):
...    def __init__(self, value):
...        self = bool(value)

but it won't work.  Look at this - nothing has changed.

>>> x = InitBool(2)
>>> x == 2
True


This line of code

    .. code-block:: python

           self = bool(value)

is deceptive. It does change the value bound to the *self* in
__init__, but it does not change the object that was passed to
__init__.


You might also try

>>> class InitBool2(int):
...    def __init__(self, value):
...        return bool(value)

but when called it raises an exception

>>> x = InitBool2(2)
Traceback (most recent call last):
TypeError: __init__() should return None, not 'bool'


Emulating :class:`bool` - using __new__
---------------------------------------

The solution to the problem is to use __new__.  Here we will show that
it works, and later we will explain elsewhere exactly what
happens. [where?].

>>> class NewBool(int):
...    def __new__(cls, value):
...        return int.__new__(cls, bool(value))

This works - no exception and 2 is converted into 1.

>>> y = NewBool(2)
>>> y == 1
True

We'll go carefully through this definition of __new__.

1. We define __new__, which like __init__ has a special role in object
creation.  But it's role is to do with creation of a new object, and
not the initialisation of an already created object.

2. The function __new__ has *two* parameters.  The first parameter is
a class.  The way we've called it, it will be the NewBool class.

3. The function __new__ returns a value.

4.  The value returned is

    .. code-block:: python

           int.__new__(cls, bool(value))


Understanding *int.__new__*
---------------------------

Here's the docstring for _int.__new__.

>>> print int.__new__.__doc__
T.__new__(S, ...) -> a new object with type S, a subtype of T

Let's try it, with S and T equal.

>>> z = int.__new__(int, 5)  # (*)
>>> z == 5
True
>>> type(z)
<type 'int'>

Thus, we see that line (*) is very much like or perhaps the same as
*int(5)*.  Let's try another example.

>>> int('10')
10
>>> int.__new__(int, '21')
21

The docstring above says that S must be a subtype of T.  So let's create one.

>>> class SubInt(int): pass

And now let's use it as an argument to int.__new__.

>>> subint = int.__new__(SubInt, 11)

Now let's test the object we've just created.  We expect it to be an
instance of SubInt, and to be equal to 11.

>>> subint == 11
True
>>> type(subint)
<class 'SubInt'>

There we have it.  Success.  All that's required to complete the
emulation of :class:`bool` is to put all the pieces together.

.. note::

   The key to subclassing immutable types is to use __new__ for both
   object creation and initialisation.


**Exercise** Create a class EmulBool that behaves like the
:class:`bool` builtin.

**Exercise** (Hard).  Parameterize EmulBool.  In other words, create
an EnumInt such that

.. code-block:: python

   X = EnumInt(['False', 'True'])

creates a class X that behave like EmulBool.
