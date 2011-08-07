Exercise: Subset of a set
=========================


The task here is to produce a memory efficient way of representing a
subset of a given base set.  We will use bytes, and for simplicity we
assume that the base set has at most eight elements.

In Python 2.6 bytes is an alternative name for string, and in Python 3
it is a separate type in its own right (with a somewhat different
interface).  Please do the exercise in Python 2.6 (or earlier, with
bytes equal to str).

The interface I suggest is something like

.. code-block:: python

   all_vowels = 'aeiou'
   SubsetOfVowels = SubsetClassFactory(all_vowels)

   my_vowels = SubsetOfVowels('ie')
   set(my_vowels) == set(['i', 'e'])
   ord(my_vowels[0]) == 2 + 4

Don't deal with set operations, such as intersection or complement.
   
By the way, an application would be dealing with large numbers of
subsets of a largish set (set 255 elements), using numpy to store the
data and do the hard work.  So set operation details would have to fit
in with numpy.

