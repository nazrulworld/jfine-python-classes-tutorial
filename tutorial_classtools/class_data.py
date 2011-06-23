'''Functions for converting a class to class data and vice versa.

Class data is a tuple from which a class can be reconstructed.
'''

special_keys = set([
        '__dict__', 
        '__doc__',
        '__metaclass__',
        '__module__', 
        '__slots__',
        '__weakref__',
])


about_keys = set([
        'doc',
        'name',
        'module',
        'slots',
])


def class_data_from_class(cls):

    metaclass = type(cls)
    bases = cls.__bases__

    body = dict(
        (key, value) 
        for (key, value) in cls.__dict__.items()
        if key not in special_keys
        )

    
    about = {}
    for key in about_keys:
        under_under_key = '__%s__' % key
        value = getattr(cls, under_under_key, None)
        if value is not None:
            about[key] = value

    return metaclass, bases, body, about


def class_from_class_data(data):

    metaclass, bases, body, about = data
    body_extras = {}

    for key in 'doc', 'slots':
        value = about.get(key)
        if value is not None:
            under_under_key = '__%s__' % key
            body_extras[under_under_key] = value

    name = about['name']
    cls = metaclass(name, bases, body)
    cls.__module__ = about['module']

    return cls


if __name__ == '__main__':

    cls = type('aaa', (), dict(a=3))
    cls.__module__ = 'anon'
    cd1 = class_data_from_class(cls)
    print cd1
    cls2 = class_from_class_data(cd1)

    cd2 =  class_data_from_class(cls2)
    if cd1 != cd2:
        print cd2
