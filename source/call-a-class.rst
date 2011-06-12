What happens when you call a class?
===================================

In this section we describe, in some detail, what happens when you
call a class.


Creation and initialisation
---------------------------

Recall that every object has a type (sometimes known as a class).

>>> type(None), type(12), type(3.14), type([])
(<type 'NoneType'>, <type 'int'>, <type 'float'>, <type 'list'>)

The result of calling a class C is, ordinarily, an initialised object
whose type is C.  In Python this process is done by two functions

* __new__ returns an object that has the right type

* __init__ initialises the object created by __new__


To explain we will do the two steps one at a time.  This will also
clarify some details.  But before we begin, we need a simple class.

>>> class A(object):
...    def __init__(self, arg):
...       self.arg = arg


We will explain what happens when Python executes the following.

   .. code-block:: python

        a = A('an arg')


First, Python creates an object that has the right type.  (The
temporary *tmp* is introduced just to explain what happens. Python
stores its value at a nameless location.)

>>> tmp = A.__new__(A, 'an arg')
>>> type(tmp)
<class 'A'>

But it has not been initialised.

>>> tmp.arg
Traceback (most recent call last):
AttributeError: 'A' object has no attribute 'arg'

Second, Python runs our initialisation code.

>>> tmp.__init__('an arg')
>>> tmp.arg
'an arg'

Finally, Python stores the value at *a*.

>>> a = tmp


The default __new__
===================

We did not define a __new__ method for our class A, but all the same
Python was able to call A.__new__.  How is this possible?

For an instance of a class C, getting an attribute proceeds via the
method resolution order of C.  Something similar, but with important
differences, happens when getting an attribute from C itself (rather
than just an instance).

Here's proof that A.__new__ and object.__new__ are the same object.
We show this in two different, but equivalant, ways.

>>> A.__new__ is object.__new__
True
>>> id(A.__new__) == id(object.__new__)
True

This explains how it is that Python can call A.__new__ even though we
did not supply such a function ourselves.

For another example, we subclass *int*.

>>> class subint(int): pass
>>> subint.__new__ is int.__new__
True


Summary
=======

Suppose C is a class.  When you call, say

    .. code-block:: python

        C(*argv, **kwargs)

the following happens.

1.  C.__new__ is found.

2.  The result of the following call is stored, say in tmp.

    .. code-block:: python

       C.__new__(C, *argv, **kwargs)

3.  tmp.__init__ is found.

4.  The result of the following is return as the value of the class call.

    .. code-block:: python

       self.__init__(*argv, **kwargs)

5.  (Not discussed.)  If tmp is not an instance of C (which includes
    subclasses of C) then steps 3 and 4 are omitted.

