Decorators versus __metaclass__
===============================

Whenever a __metaclass__ is used, one could also use a decorator to
get effectively the same result.  This section discusses this topic.

For an example we use the concept of a Bunch, as discussed in Alex
Martelli's excellent book *Python in a Nutshell*.  As he says, a Bunch
is similar to the struct type in C.


Bunch using __metaclass__
--------------------------

The code here is based on the __metaclass__ implementation of Bunch,
given in *Python in a Nutshell*.  The API is:

.. code-block:: python

    class Point(MetaBunch):

        x = 0.0
        y = 0.0

The base class :func:`MetaBunch` is defined by:

.. code-block:: python

    class MetaBunch(object):

        __metaclass__ = metaMetaBunch


The real work is done in

..  code-block:: python

    class metaMetaBunch(type):

        def __new__(cls, name, bases, body):

            new_body = ... # Computed from body

            return type.__new__(cls, name, bases, new_body)

where I've omitted the crucial code that computes the new_body from
the old.  (My focus here is on the logic of __metaclass_ and not the
construction of the new body.)


How __metaclass__ works
-----------------------

In Python the class statement creates the class body from the code you
have written, placing it in a dictionary.  It also picks up the name
and the bases in the first line of the class statement.  These three
arguments, (name, bases, body) are then passed to a function.

The __metaclass__ attribute is part of determining that function.  If
__metaclass__ is a key in the body dictionary then the value of that
key is used.  This value could be anything, although if not callable
an exception will be raised.

In the example above, the MetaBunch class body has a key
__metaclass__, and so its value metaMetaBunch is used.  It is
metaMetaBunch that is used to create the value that is stored at
MetaBunch.

What is that value?  When we instantiate metaMetaBunch we use its
__new__ method to create the instance, which is an instance of type.
In particular, the code that creates the new_body is run on the body
of MetaBunch.

Now what happens when we subclass MetaBunch.  One might think that

* because Point inherits from MetaBunch
* and because MetaBunch has a __metaclass__ in its body
* and that __metaclass__ has value metaMetaBunch

it follows that metaMetaBunch is use to construct the Point class.

But this is gotcha.  Even though the conclusion is correct the
reasoning is not.  What happens is that

* Python looks for __metaclass__ in the body of Point
* but it's not there so it looks at the bases of Point
* and in the bases it finds MetaBunch
* whose type is metaMetaBunch

and so it uses that instead of type when constructing Point.


Bunch using decorators
----------------------

Here we give a construction based on the decorator point of view.
First we define a function, which can be used as a decorator, that
returns a bunch class.


>>> def bunch_from_dict(a_dict, name='a_bunch'):
...
...     __slots__ = sorted(a_dict.keys())
...     defaults = dict(a_dict)
...     bases = (BaseBunch,)
...
...     def __init__(self, **kwargs):
...         for d in defaults, kwargs:
...             for key, value in d.items():
...                 setattr(self, key, value)
...
...     body = dict(__slots__=__slots__, __init__=__init__)
...     return type(name, bases, body)

We now need to implement the BaseBunch class, from which the return
bunch classes will inherit __repr__ and, if we wish, other attributes.

>>> class BaseBunch(object):
...    def __repr__(self):
...        body = ', '.join([
...            '%s=%r' % (key, getattr(self, key))
...            for key in self.__slots__
...        ])
...        return '%s(%s)' % (self.__class__.__name__, body)

Here's an example of the creation of a Point class.

>>> Point = bunch_from_dict(dict(x=0, y=0), 'Point')

And here are examples of its use.

>>> Point(x=1, y=3)
Point(x=1, y=3)
>>> Point()
Point(x=0, y=0)

We can also use bunch_from_dict as a decorator.

>>> from jfine.classtools import dict_from_class
>>> @bunch_from_dict
... @dict_from_class
... class RGB(object):
...      'This is a docstring.'
...      red = green = blue = 0

Here's an example of the use of the RGB class.  It shows that the name
of the class is not being properly picked up.  This is an interface
problem rather than a problem with the decorator approach.  The name
is available to be used, but the interface is not making it available.
Similar remarks apply to the docstring.

>>> RGB(blue=45, green=150)
a_bunch(blue=45, green=150, red=0)

