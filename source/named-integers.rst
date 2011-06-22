Exercise: Named integers
------------------------

The bool type produces True and False, which are something like named
integers.  The exercise is to produce, from something like a mapping,
a subclass of int that provides named integers.

Just as True and False look nicer that 0 or 1 when a quantity is a
boolean, so named integers look nicer with symbolic constants.


The interface should be something like

.. code-block:: python

    my_items = [(0, 'zero'), (1, 'one'), (2, 'two')]
    OneTwoThree = whatsit(my_items)

The behavior should be something like

.. code-block:: python

    z = OneTwoThree('zero')
    str(z) == 'zero'

    t = OneTwoThree(2)
    str(t) == 'two'


Thus, any string or integer (within range) can be used to produce a
named integer.  Out of range values should produce an exception.
