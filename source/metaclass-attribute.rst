The :attr:`__metaclass__` attribute
===================================

The __metaclass__ attribute was introduced to give the programmer some
control over the semantics of the class statement.  In particular it
eases the transition from old-style classes (which are not covered in
this tutorial) and new-style classes (simply called classes in this
tutorial).


.. _automatic-subclassing-of-object:

Automatic subclassing of object
-------------------------------

If at the told of a module you write:

    .. code-block:: python

        __metaclass__ = type

then class statements of the form:

    .. code-block:: python

        class MyClass:
            pass

will automatically be new-style.  In other words, you don't have to
explicitly place object in the list of bases.  (This behaviour is a
consequence of the semantics of __metaclass__.)


Review of type(name, bases, body) and class statement
-----------------------------------------------------

Recall that the type command, called like so

    .. code-block:: python

        cls = type(name, bases, body)

constructs the class cls, as does the class statement

    .. code-block:: python

        class cls(...):

            # body statements go here

The __metaclass__ attribute provides a link between these two ways of
constructing classes.


The basic principle of the __metaclass__
----------------------------------------

Ordinarily, a class statement results in a call to type, with name,
bases and body as arguments.  However, this can be changed by

    1.  Assigning __metaclass__ as an class body attribute.

    2.  Assigning __metaclass__ as a module attribute.

    3.  Placing a suitable class in the bases of the class statement.

Method (1) is used above, in :ref:`automatic-subclassing-of-object`.
To explain (2) we will introduce a very silly example.


A very silly example
--------------------

It's not necessary for the __metaclass__ attribute to be type or a
subclass of type.  It could be any callable.

Here it is a function that returns a string.

>>> class very_silly(object):
...     def __metaclass__(*argv):
...         return 'This is very silly.'

The variable :data:`silly` bound by the class statement is a string.
In fact, it is the return value of the __metaclass__ attribute.

>>> very_silly
'This is very silly.'


A less silly example
--------------------

Here's a less silly example.  We define the __metaclass__ to return
the argument vector passed to it.  This consists of name, bases and body.

>>> class silly(object):
...     def __metaclass__(*argv):
...         return argv

The variable silly is now bound to the value of argv.  So it is a
tuple of length 3, and it can be unpacked into name, bases and body.

>>> type(silly), len(silly)
(<type 'tuple'>, 3)
>>> name, bases, body = silly

The name, and bases are much as we expect them.

>>> name == 'silly', bases ==(object,)
(True, True)

The body has, as could be expected, a __metaclass__ key, which has the
expected value.

>>> sorted(body.keys())
['__metaclass__', '__module__']
>>> silly[2]['__metaclass__']
<function __metaclass__ at 0x...>


A __metaclass__ gotcha
----------------------

A class statement, if it does not raise an exception, assigns a value
to a variable.  Ordinarily, this value is a direct instance of type, namely

    .. code-block:: python

        type(name, bases, body)

However, using __metaclass__ above allows the value assigned by a
class statement to be any object whatsover.  In the very silly example
the value assigned by the class statement was a string.  This is a
violates the principle of least surprise, and that is the main reason
why the example is very silly (and not that it does nothing useful).

With decorators, which are available on class statements since Python
2.6, the same effect as the silly example can be obtained without
resort to complex magic.


A decorator example
-------------------

Here we produce something similar to the silly example.  First we
define a decorator

>>> from jfine.classtools import dict_from_class
>>> def type_argv_from_class(cls):
...     d = cls.__dict__
...     name = cls.__name__
...     body = dict_from_class(cls)
...     bases = cls.__bases__
...     return name, bases, body

Now we use the decorator.  There is no magic.  The class statement
produces a class, and the decorator function
:func:`type_args_from_class` produces an argument vector from the
class.

>>> @type_argv_from_class
... class argv(object):
...      key = 'a value'


When we unpack :data:`argv` we get what we expect.

>>> name, bases, body = argv
>>> name
'argv'
>>> bases
(<type 'object'>,)
>>> body
{'key': 'a value'}
