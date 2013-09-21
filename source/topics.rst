Topics
======

Dispatch tables
---------------

We can use class to construct something that is not a class.

Sometimes we want a dictionary (or some other structure) whose values
are functions.  Each class has a __dict__ which contains the class
attributes.  We can use this.  (Another way route is to return
locals() within a function.)

Here's a use case for a dispatch table::
 
 for key, value in pairs:
     dispatch[key](value)


Dynamic classes
---------------

All instances of a class share the attributes of their class.
Sometimes we want to construct a class dynamically.  For example,
suppose we want all lines in a file (or object read from a stream) to
share data about the stream they came from.

We can do this using *type(name, bases, dict)*.


Subclassing immutable type
--------------------------

Lists and dicts are mutable types.  Numbers, strings and tuples are
immuatables.  Immutables can be used as keys in a dictionary,
immutables can't.

Sometimes we want to subclass an immutable type.  For example, see
namedtuple in the standard library.

There's a problem with initialising immutable objects, namely that
they are immutable and so can't be changed during __init__.  The
solution is to use __new__.


Don't use __metaclass__
-----------------------

This advice is too broad.  Don't use __metaclass__ unless you really
have to, or have at least considered the alternatives.  Sometimes it's
better to use a decorator.


Special methods
---------------

These are the dunder (double under) methods, such as __getitem__ and
__setitem__.  Lookup for implicit use of special methods goes directly
to the class of the object.


When to subclass type
---------------------

Subclassing type is the same as using a custom metaclass.  Sometimes,
for example to produces classes that act like collections, you have to
subclass type.  We'll explain this.


Introduction to tagtree
-----------------------

This is a nice syntax (I'm biased, I invented it) for creating trees
(such as XML) where each element in the tree has
* a head, which contains key-value attributes
* a body, which is a sequence of data items and other elements

The implementation of tagtree requires a custom metaclass.


Introduction to JavaScript objects
----------------------------------

This is my party piece.  I explain why Javascript object are
* like Python classes
* with custom item methods
* on the metaclass
* which are never instantiated

Knowing this really helps you understand the difference between
objects and classes in JavaScript and Python.




