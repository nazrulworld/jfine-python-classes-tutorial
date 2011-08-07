Decorators
==========

This section cover *the decorator syntax* and the concept of a
decorator (or decorating) callable.

Decorators are a syntactic convenience, that allows a Python source
file to say what it is going to do with the result of a function or a
class statement before rather than after the statement.  Decorators on
function statements have been available since Python 2.4, and on
class statements since Python 2.6.

In this section we describe the decorator syntax and give examples of
its use.  In addition, we will discuss functions (and other callables)
that are specifically designed for use as decorators.  They are also
called decorators.

You can, and in medium sized or larger projects probably should, write
your own decorators.  The decorator code might, unfortunately, be a
little complex.  But it can greatly simplify the other code.


The decorator syntax
--------------------

The decorator syntax uses the *@* character.  For function statements
the following are equivalent:

.. code-block:: python

   # State, before defining f, that a_decorator will be applied to it.
   @a_decorator
   def f(...):
       ...

.. code-block:: python

   def f(...):
       ...

   # After defining f, apply a_decorator to it.
   f = a_decorator(f)

The benefits of using the decorator syntax are:

1.  The name of the function appears only once in the source file.

2.  The reader knows, before the possibly quite long definition of the
    function, that the decorator function will be applied to it.

The decorator syntax for a class statement is same, except of course
that it applies to a class statement.

Bound methods
-------------

Unless you tell it not to, Python will create what is called a bound
method when a function is an attribute of a class and you access it
via an instance of a class.  This may sound complicated but it does
exactly what you want.

>>> class A(object):
...     def method(*argv):
...         return argv
>>> a = A()
>>> a.method
<bound method A.method of <A object at 0x...>>

When we call the bound method the object *a* is passed as an argument.

>>> a.method('an arg')
(<A object at 0x...>, 'an arg')
>>> a.method('an arg')[0] is a
True


:func:`staticmethod`
--------------------

A static method is a way of suppressing the creation of a bound method
when accessing a function.

>>> class A(object):
...     @staticmethod
...     def method(*argv):
...         return argv
>>> a = A()
>>> a.method
<function method at 0x...>

When we call a static method we don't get any additional arguments.

>>> a.method('an arg')
('an arg',)


:func:`classmethod`
-------------------

A class method is like a bound method except that the class of the
instance is passed as an argument rather than the instance itself.

>>> class A(object):
...     @classmethod
...     def method(*argv):
...         return argv
>>> a = A()
>>> a.method
<bound method type.method of <class 'A'>>

When we call a class method the class of the instance is passed as an
additional argument.

>>> a.method('an arg')
(<class 'A'>, 'an arg')
>>> a.method('an arg')[0] is A
True

In addition, class methods can be called on the class itself.

>>> A.method('an arg')
(<class 'A'>, 'an arg')


The :func:`call` decorator
---------------------------

Suppose we want to construct a lookup table, say containing the
squares of positive integers for 0 to *n*.

For n small we can do it by hand:

>>> table = [0, 1, 4, 9, 16]
>>> len(table), table[3]
(5, 9)

Because the formula is simple, we could also use a list comprehension:

>>> table = [i * i for i in range(5)]
>>> len(table), table[3]
(5, 9)

Here's another way, that uses a helper function (which we will call
*table*).  For a table of squares list comprehension is better,
because we can write an expression that squares.  But for some tables
a complex sequence of statements is required.

>>> def table(n):
...     value = []
...     for i in range(n):
...         value.append(i*i)
...     return value
>>> table = table(5)

We call the helper function *table* for three related reasons

1.  It indicates the purpose of the function.

2.  It ensures that the helper function is removed from the namespace
    once the table has been constructed.

3.  It conforms to the decorator syntax.

As before, we test the table and find that it works.
>>> len(table), table[3]
(5, 9)


>>> def call(*argv, **kwargs):
...     def call_fn(fn):
...         return fn(*argv, **kwargs)
...     return call_fn


>>> @call(5)
... def table(n):
...     value = []
...     for i in range(n):
...         value.append(i*i)
...     return value

>>> len(table), table[3]
(5, 9)


Nesting decorators
------------------

The decorator syntax can be nested.  The following example is similar
to the list comprehension approach, except that it uses a generator
function rather than a generator expression.

>>> @list
... @call(5)
... def table(n):
...     for i in range(n):
...         yield i * i

We read this as saying:

   The value of *table* is the list obtained by iterating over the
   function evaluated at n equal to 5.

The purpose of this example is illustrate some of the concepts.  We
are not saying that it is, or is not good programming practice.  That
will depend, in part, on the context.

As before, we test the table and find that it works.

>>> len(table), table[3]
(5, 9)


Class decorators before Python 2.6
----------------------------------

Prior to Python 2.6 one could not write

.. code-block:: python

   @a_decorator
   class MyClass(...):

         # possibly many lines of code.

If you need to support earlier versions of Python, I recommend that
you develop in Python 2.6 or later.  This allows your mind and
keyboarding to use decorators.  Once the decorating code is stable
refactor it to support earlier versions of Python, as follows.

.. code-block:: python

   # @a_decorator
   class MyClass(...):

         # possibly many lines of code.

   MyClass = a_decorator(MyClass)   # if changed, change decorator comment.

This approach allows you to think and largely code using the class
decorator point of view, at the cost of having to keep the decorator
comment up to date when the decorator changes.
