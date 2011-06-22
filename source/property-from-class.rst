Exercise: Property from class decorator
=======================================


A property is a way of providing a class with virtual or protected
attributes.  They can be a good way of hiding and protecting
implementation details.  The area property of a rectangle is a good
example of a read-only property.

Some properties are both read and write.  There may also be a case for
write-only properties.  One can also delete a property.  To help the
programmer, a property can have a docstring.

The signature for property is

.. code-block:: python

    property(fget=None, fset=None, fdel=None, doc=None)

The exercise is to make a decorator that simplifies the creation of
complex property attributes.  The interface I suggest is

.. code-block:: python

   class MyClass(object):

        @property_from_class
	class my_property(object):
	    '''This is to be the doc string for the property.'''

	    def fget(self):
	        pass	        # code goes here 

	    def fset(self):
	        pass	        # code goes here 

	    def fdel(self):
	        pass	        # code goes here 


Any or all of fget, fset, fdel can be omitted, as can the docstring.
It should be an error to 'use the wrong keyword'.
