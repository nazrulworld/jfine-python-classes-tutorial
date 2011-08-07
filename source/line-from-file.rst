Exercise: A line from a file
============================

We want to read lines from one of more files.  We want each line to

* be a string 
* have a filename attribute
* have a linenumber attribute

Recall that we can already iterate over the lines of a file.

.. code-block: python
    
    f = open('myfile.txt')
    for line in f:
        do_something_with(line)

The interface I suggest is

.. code-block:: python

    filename = 'myfile.txt'
    f = open(filename)
    labelled_lines = LabelledLines(f, filename)


The behavior we'd like is for this code

.. code-block:: python

    for line in labelled_lines:
        print (line.filename, line.linenumber, line)

to produce output like

.. code-block:: python

    ('myfile.txt', 0, 'First line\n')
    ('myfile.txt', 1, 'Second line\n')
    ('myfile.txt', 2, 'Third line\n')
