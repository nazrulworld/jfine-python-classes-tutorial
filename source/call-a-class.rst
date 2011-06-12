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
stores the value at a nameless location.)

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
